#!/usr/bin/env python3
"""案例编码的统计：理论文档里手写的数字（案例数、多结构数、来源数、流派数、留一法正确率）都从这里来。
新增或改动案例后运行一遍，和文档里的数字对一下；能用 build.py 生成块表达的数字（`casestats`、`schoolcount`、`schoolloo` 等）不要手抄。
留一法的平局规则：取其余案例里整体更常见的流派，结果与案例顺序无关。
"""
import yaml, collections as C, itertools, json
from pathlib import Path
R=str(Path(__file__).resolve().parent.parent)+'/'
cl=yaml.safe_load(open(R+'catalog/cases.yaml')); cl=cl if isinstance(cl,list) else cl['cases']
N=len(cl)
print('N',N,'project',sum(c['origin']=='project' for c in cl),'external',sum(c['origin']=='external' for c in cl))
print('multi-structure',sum(len(c['structure'])>1 for c in cl))
print('primary structure',C.Counter(c['structure'][0] for c in cl).most_common())
print('any structure',C.Counter(s for c in cl for s in c['structure']).most_common())
pairs=C.defaultdict(list)
for c in cl:
    for a,b in itertools.combinations(sorted(set(c['structure'])),2): pairs[(a,b)].append(c['id'])
print('pairs',[(k,len(v)) for k,v in sorted(pairs.items(), key=lambda t:-len(t[1]))][:10])
print('school any',C.Counter(s for c in cl for s in c['schools']).most_common())
print('school primary',C.Counter(c['schools'][0] for c in cl if c['schools']).most_common())
print('n schools',C.Counter(len(c['schools']) for c in cl), 'multi',sum(len(c['schools'])>1 for c in cl))
print('source any',C.Counter(s for c in cl for s in c['source']).most_common())
print('source primary',C.Counter(c['source'][0] for c in cl).most_common())
print('separate-views',sum('separate-views' in c['abstraction'] for c in cl))
print('thinking',sum(bool(c.get('thinking')) for c in cl),'alternative',sum(any(r.startswith('alternative:') for r in c.get('thinking',[])) for c in cl))
for o in ('project','external'):
    print(o,'link',sum(1 for c in cl if c['origin']==o and 'link' in c['schools']),sum(c['origin']==o for c in cl), C.Counter(s for c in cl if c['origin']==o for s in c['schools']).most_common())
rows=[c for c in cl if c['schools'] and c.get('focus') and c.get('issue_types')]
def loo(keyf):
    groups=C.defaultdict(list)
    for i,c in enumerate(rows): groups[keyf(c)].append(i)
    hit=0
    for i,c in enumerate(rows):
        others=[rows[j]['schools'][0] for j in groups[keyf(c)] if j!=i] or [r['schools'][0] for j,r in enumerate(rows) if j!=i]
        cnt=C.Counter(others); base=C.Counter(r['schools'][0] for j,r in enumerate(rows) if j!=i)
        pred=max(cnt, key=lambda s:(cnt[s], base[s]))   # 平局时取其余案例里整体更常见的流派，和案例顺序无关
        hit+= pred==c['schools'][0]
    return round(hit/len(rows),2)
print('LOO n',len(rows),{k:loo(f) for k,f in {'baseline':lambda c:'x','issue':lambda c:c['issue_types'][0],'source':lambda c:c['source'][0],'focus':lambda c:c['focus'][0],'structure':lambda c:c['structure'][0],'str+src':lambda c:(c['structure'][0],c['source'][0]),'focus+issue':lambda c:(c['focus'][0],c['issue_types'][0]),'str+issue':lambda c:(c['structure'][0],c['issue_types'][0])}.items()})
by=C.defaultdict(C.Counter)
for c in rows: by[c['focus'][0]][c['schools'][0]]+=1
for f,cn in sorted(by.items(), key=lambda t:-sum(t[1].values())): print(' focus',f,sum(cn.values()),dict(cn.most_common()))
rel={'connectivity','precedence','cycle','cluster'}
print('relation focus->link',sum(1 for c in rows if c['focus'][0] in rel and c['schools'][0]=='link'),sum(1 for c in rows if c['focus'][0] in rel))
g=[c for c in cl if c['structure'][0]=='graph' and c['schools']]
byg=C.defaultdict(C.Counter)
for c in g: byg[c['focus'][0]][c['schools'][0]]+=1
print('graph by focus',{k:dict(v) for k,v in byg.items()})
for s in ['hierarchy','dag','graph','propositional','table','set','sequence','spatial','causal','flow']:
    rr=[c for c in cl if c['structure'][0]==s]
    print(s,len(rr),'issue',C.Counter(c['issue_types'][0] for c in rr if c.get('issue_types')).most_common(4),'focus',C.Counter(c['focus'][0] for c in rr if c.get('focus')).most_common(4))
