// 用无头 Chromium 真实渲染展示页：确认页面打开后有内容（标题、文字量、canvas/svg/img 数量），并截图。
// 需要全局安装的 playwright 和预装的 Chromium；会话里的出站代理由 HTTPS_PROXY 指定，CA 已在浏览器证书库里。
// 用法: NODE_PATH=$(npm root -g) node scripts/render_check.js urls.json out.json [截图目录]
//   urls.json: [{"id":"…","url":"…","wait":4000}]；out.json：每条的渲染结果。截图只留在本地，不进仓库。
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const out = [];
  const browser = await chromium.launch({ headless: true, proxy: { server: process.env.HTTPS_PROXY } });
  for (const it of items) {
    const rec = { id: it.id, url: it.url };
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 }, userAgent: 'Mozilla/5.0 (compatible; awesome-structural-sensemaking-render-check/1.0)' });
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push(String(e).slice(0, 120)));
    try {
      const resp = await page.goto(it.url, { timeout: 40000, waitUntil: 'load' });
      await page.waitForTimeout(it.wait || 4000);
      rec.status = resp ? resp.status() : null;
      rec.final = page.url();
      rec.title = (await page.title()).slice(0, 120);
      rec.text_len = await page.evaluate(() => (document.body ? document.body.innerText.length : 0));
      rec.canvas = await page.evaluate(() => document.querySelectorAll('canvas').length);
      rec.svg = await page.evaluate(() => document.querySelectorAll('svg').length);
      rec.img = await page.evaluate(() => document.querySelectorAll('img').length);
      rec.shot = `${process.argv[4] || 'shots'}/${it.id}.png`;
      await page.screenshot({ path: rec.shot, fullPage: false });
    } catch (e) {
      rec.error = String(e).slice(0, 160);
    }
    rec.page_errors = errs.length;
    await ctx.close();
    out.push(rec);
    console.log(JSON.stringify(rec));
    fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
  }
  await browser.close();
  fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
})();
