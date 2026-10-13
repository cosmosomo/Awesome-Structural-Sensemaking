# 案例证据

> 本文件由 `scripts/build.py` 根据 `catalog/cases.yaml` 和 `catalog/case-evidence.json` 生成，请改数据，不要直接改这里。

每个案例先列出编码所依据的原文，后面可以展开看读到的其他摘录。摘录由子智能体从官方页面逐字抄下，`scripts/check_quotes.py` 再把每一条拿到页面文字里做子串比对：✓ 表示页面文字里找到了这段话；？表示没找到或页面读不到（不等于抄错：页面可能由 JS 渲染，或在检查时临时读不到）。

<!-- gen:caseevidence: -->
<a id="dependency-cruiser"></a>

### dependency-cruiser

- 领域：软件工程；议题：找出项目里不该有的、奇怪的模块依赖
- 编码：一般图与网络；重点：连通与邻域、先后与依赖方向；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 回答的问题：“To help you find the weird ones. To root out the unwanted ones.” [✓](https://sverweij.github.io/dependency-cruiser/)
  - 关系：“insight in the dependencies within your JavaScript, TypeScript and other alt-js projects” [✓](https://sverweij.github.io/dependency-cruiser/)
  - 视图：“Demo: 3D graph reporter plugin for dependency-cruiser (issue #458)” [✓](https://sverweij.github.io/dependency-cruiser-repro-repo/458/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“insight in the dependencies within your JavaScript, TypeScript and other alt-js projects” [✓](https://sverweij.github.io/dependency-cruiser/)
- 对象：“dependency-cruiser’s internal graph - nodes are text labels” [✓](https://sverweij.github.io/dependency-cruiser-repro-repo/458/)
- 视图：“Results (interactive html):” [✓](https://sverweij.github.io/dependency-cruiser-repro-repo/458/)
- 交互：“graphically explore dependency-cruiser's dependency graph and source code” [✓](https://sverweij.github.io/dependency-cruiser/)

</details>
- 没读到：attributes；encodings；abstraction

<a id="madge"></a>

### Madge

- 领域：软件工程；议题：生成模块依赖图，发现循环依赖
- 编码：一般图与网络；重点：环与反馈、连通与邻域；把握：证据很少
- 说明：子智能体读 npm 页面被 403 拒绝，案例证据文件里没有摘录；说明来自此前对 registry.npmjs.org/madge README 的核对（“generating a visual graph of your module dependencies, finding circular dependencies”）。
- 没读到：input_material；entities；relations；attributes；views；encodings；interactions；questions；abstraction；（没读到：https://www.npmjs.com/package/madge 返回 403，没有其他可读的官方页面；WebSearch 摘要不作依据）

<a id="pydeps"></a>

### pydeps

- 领域：软件工程；议题：在大型 Python 项目里发现循环导入，并只看某个模块周围的依赖
- 编码：一般图与网络；重点：环与反馈、连通与邻域；把握：官方页面直接写了
- 编码所依据的原文：
  - 回答的问题：“which is useful for spotting cyclic imports in large projects” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
  - 关系：“--show-cycles show only import cycles” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
  - 属性与度量：“exclude nodes that are more than n hops away (default=2, 0 -> infinite)” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
  - 抽象与层级：“coalesce deep modules to at most n levels” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
  - 编码：“any cycles in the dependency graph are highlighted as blue boxes by default” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“pydeps finds imports by looking for import-opcodes in python bytecodes (think .pyc files)” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 对象：“only imported files will be found” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 对象：“nodes participating in an import cycle” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 关系：“the edges between them” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 属性与度量：“exclude sources or sinks with degree greater than noise-level” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 属性与度量：“pydeps also contains an Erdős-like scoring function” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 视图：“To create graphs with pydeps you also need to install Graphviz” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 视图：“gives the following graph” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 视图：“drawing external dependencies as clusters” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 视图：“The direction of the graph can be specified using the --rankdir flag” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 编码：“the arrowheads now have the color of the source node” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 抽象与层级：“drawing external dependencies as clusters” [✓](https://pydeps.readthedocs.io/en/latest/index.html)
- 抽象与层级：“Collapsing target package” [✓](https://pydeps.readthedocs.io/en/latest/index.html)

</details>
- 没读到：interactions（页面只写了命令行参数，没有交互操作）；（没读到：https://pypi.org/project/pydeps/ 返回 Client Challenge 页面，未读）

<a id="codeboarding"></a>

### CodeBoarding

- 领域：软件工程；议题：合并之前看清一个 PR 改了系统的哪些部分、影响哪里
- 编码：层级与树 + 一般图与网络；重点：包含与层次、连通与邻域、时间与演化；把握：官方页面直接写了
- 说明：用颜色编码“变更状态”（新增、修改、删除），同时标在组件和关系上——比较（compare）直接叠加在结构图上。
- 编码所依据的原文：
  - 回答的问题：“See what a pull request does to your system before you merge it.” [✓](https://codeboarding.org/)
  - 抽象与层级：“Pan, zoom, click a component for its details, and drill into sub-components.” [✓](https://codeboarding.org/getting-started#github-action)
  - 编码：“green is added, yellow is modified, red dashed is deleted” [✓](https://codeboarding.org/getting-started#github-action)
  - 交互：“compare two refs side by side” [✓](https://codeboarding.org/getting-started#github-action)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Five public codebases, drawn by the engine from their code.” [✓](https://codeboarding.org/)
- 处理的材料：“See what a pull request does to your system before you merge it.” [✓](https://codeboarding.org/)
- 对象：“Pan, zoom, click a component for its details, and drill into sub-components.” [✓](https://codeboarding.org/getting-started#github-action)
- 对象：“changed components and edges are coloured against the target branch” [✓](https://codeboarding.org/getting-started#github-action)
- 关系：“The diff legend marks what changed (green is added, yellow is modified, red dashed is deleted) for both components and relationships.” [✓](https://codeboarding.org/getting-started#github-action)
- 关系：“See the changed components and new connections without leaving GitHub” [✓](https://codeboarding.org/)
- 属性与度量：“the panel summarises what the PR adds, modifies, and removes” [✓](https://codeboarding.org/getting-started#github-action)
- 视图：“The Action posts a Mermaid change diagram on the pull request itself.” [✓](https://codeboarding.org/)
- 视图：“The interactive diagram below is the real webview, embedded right here.” [✓](https://codeboarding.org/getting-started#github-action)
- 视图：“The diagram beside your code, and components as context for your agent.” [✓](https://codeboarding.org/getting-started#github-action)
- 编码：“changed components and edges are coloured against the target branch” [✓](https://codeboarding.org/getting-started#github-action)
- 交互：“Pan, zoom, click a component for its details, and drill into sub-components.” [✓](https://codeboarding.org/getting-started#github-action)
- 回答的问题：“What changed, what it affects, where to look first.” [✓](https://codeboarding.org/)

</details>

<a id="understand-anything"></a>

### Understand Anything

- 领域：软件工程；议题：接手代码库时弄懂它由什么组成、怎么连接，并把代码对应到业务领域
- 编码：一般图与网络 + 层级与树；重点：连通与邻域、包含与层次、群落与相似；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 抽象与层级：“Explorable graph with hierarchical drill-down, smart layout, and community clustering.” [✓](https://understand-anything.com/)
  - 抽象与层级：“or switch to business knowledge mode and watch your code transform” [✓](https://understand-anything.com/)
  - 属性与度量：“Filter by type, complexity, or layer.” [✓](https://understand-anything.com/)
  - 关系：“Shortest path between any two components. See how your system connects.” [✓](https://understand-anything.com/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Dockerfiles, Terraform, SQL, Markdown, and 26+ file types in one unified graph.” [✓](https://understand-anything.com/)
- 处理的材料：“Understand codebases through guided context” [✓](https://understand-anything.com/)
- 对象：“Files, functions, edges.” [✓](https://understand-anything.com/)
- 对象：“login() verify_token() session management” [✓](https://understand-anything.com/)
- 对象：“how your code maps to real business domains, processes, and flows” [✓](https://understand-anything.com/)
- 对象：“Domain mapping Business flows Process steps” [✓](https://understand-anything.com/)
- 关系：“Explore every file, function, and dependency” [✓](https://understand-anything.com/)
- 关系：“Typical code graph 23 nodes. 34 edges.” [✓](https://understand-anything.com/)
- 关系：“Auth flow. Session management. Now you understand.” [✓](https://understand-anything.com/)
- 视图：“Explorable graph with hierarchical drill-down, smart layout, and community clustering.” [✓](https://understand-anything.com/)
- 视图：“Interactive Dashboard” [✓](https://understand-anything.com/)
- 视图：“AI-generated walkthroughs that teach the codebase step by step.” [✓](https://understand-anything.com/)
- 交互：“Hierarchical drill-down” [✓](https://understand-anything.com/)
- 交互：“Fuzzy and semantic search to find anything.” [✓](https://understand-anything.com/)
- 交互：“or switch to business knowledge mode and watch your code transform” [✓](https://understand-anything.com/)
- 交互：“High-quality PNG, SVG, or filtered JSON for docs, presentations, or analysis.” [✓](https://understand-anything.com/)
- 回答的问题：“We teach you the codebase.” [✓](https://understand-anything.com/)
- 回答的问题：“See how your system connects.” [✓](https://understand-anything.com/)
- 回答的问题：“how your code maps to real business domains, processes, and flows” [✓](https://understand-anything.com/)
- 抽象与层级：“Filter by type, complexity, or layer.” [✓](https://understand-anything.com/)

</details>
- 没读到：encodings；（没读到：Features、Live Demo 等子页在首页上找不到可跟随的链接，只读了首页）

<a id="likec4"></a>

### LikeC4

- 领域：软件工程；议题：用同一份架构模型，向不同的人展示不同范围、不同层级的图
- 编码：层级与树 + 一般图与网络；重点：包含与层次、连通与邻域、跨视图的同一对象；把握：官方页面直接写了
- 编码所依据的原文：
  - 对象：“The model describes the architecture as a set of hierarchical elements and relationships among them.” [✓](https://likec4.dev/dsl/model/)
  - 抽象与层级：“LikeC4 does not enforce specific rules, such as a strict number of levels” [✓](https://likec4.dev/dsl/views/)
  - 抽象与层级：“The view will then inherit the scope of that element:” [✓](https://likec4.dev/dsl/views/)
  - 交互：“onNavigateTo” [✓](https://likec4.dev/tooling/react/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Describe your system architecture with code.” [✓](https://likec4.dev/)
- 对象：“An element is a basic building block.” [✓](https://likec4.dev/dsl/model/)
- 关系：“hierarchical elements and relationships among them.” [✓](https://likec4.dev/dsl/model/)
- 关系：“enableElementDetails enableRelationshipDetails” [✓](https://likec4.dev/tooling/react/)
- 属性与度量：“Element metadata is a set of key-value pairs defined in a nested block:” [✓](https://likec4.dev/dsl/model/)
- 属性与度量：“Element tags are defined in a nested block and must come first, before any other properties:” [✓](https://likec4.dev/dsl/model/)
- 属性与度量：“If title is not specified, name will be used by default” [✓](https://likec4.dev/dsl/model/)
- 视图：“Data flows and sequence diagrams” [✓](https://likec4.dev/dsl/views/)
- 视图：“System Landscape System Context Containers Components” [✓](https://likec4.dev/showcases/bigbank/)
- 视图：“Implement unique visual representations using SVG and drawing libraries” [✓](https://likec4.dev/tooling/react/)
- 视图：“Default view index is a special view, and is rendered by default if no view name is specified.” [✓](https://likec4.dev/dsl/views/)
- 交互：“Add custom buttons, toolbars, and interactive behaviors” [✓](https://likec4.dev/tooling/react/)
- 交互：“Create interactive dialogs for displaying detailed information” [✓](https://likec4.dev/tooling/react/)
- 交互：“showNavigationButtons” [✓](https://likec4.dev/tooling/react/)
- 回答的问题：“Visualize, validate and share — all from a single source of truth.” [✓](https://likec4.dev/)
- 回答的问题：“It gives an overview of the LikeC4 syntax and how it compares to Structurizr” [✓](https://likec4.dev/showcases/bigbank/)
- 抽象与层级：“the parent name is used as a prefix.” [✓](https://likec4.dev/dsl/model/)

</details>
- 没读到：encodings

<a id="bpmn-js"></a>

### bpmn-js

- 领域：业务流程；议题：在浏览器里查看、创建和编辑 BPMN 流程图
- 编码：一般图与网络；重点：先后与依赖方向、对象上的度量；把握：页面信息支持，归类靠推断
- 说明：官方页面把“图交互”（diagram-js）、“BPMN 元模型”（bpmn-moddle）和“组装”（bpmn-js）分成三层，说明图形层和语义层是分开设计的。
- 编码所依据的原文：
  - 视图：“Overlays - provides APIs for attaching additional information to diagram elements.” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
  - 抽象与层级：“Diagram Interaction / Modeling (diagram-js) BPMN Meta-Model (bpmn-moddle) Plugging Things together (bpmn-js)” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
  - 交互：“Integrate an in-browser process engine, token simulation” [✓](https://bpmn.io/toolkit/bpmn-js/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Use bpmn-js to view, create and edit BPMN 2.0 diagrams in your browser.” [✓](https://demo.bpmn.io/)
- 对象：“to draw shapes and connections” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 关系：“Plugging Things together (bpmn-js)” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 视图：“Embed the Viewer (pre-packaged)” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 视图：“Roll your own Modeler (via npm)” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 视图：“For advanced use cases such as modeling it contributes the context pad, palette” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 交互：“Click the diagram and continue modeling.” [✓](https://demo.bpmn.io/)
- 交互：“ContextPad - provides contextual actions around an element.” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 交互：“CommandStack - responsible for redo and undo during modeling.” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)
- 回答的问题：“Open or create a BPMN diagram.” [✓](https://demo.bpmn.io/)
- 回答的问题：“Create, embed and extend BPMN diagrams in your Browser.” [✓](https://bpmn.io/toolkit/bpmn-js/)
- 抽象与层级：“bpmn-js is built for extensibility.” [✓](https://bpmn.io/toolkit/bpmn-js/)
- 抽象与层级：“You may use the additionalModules option to extend the Viewer and Modeler on creation.” [✓](https://bpmn.io/toolkit/bpmn-js/walkthrough/)

</details>
- 没读到：attributes；encodings

<a id="agentensemble-viz"></a>

### AgentEnsemble Viz

- 领域：AI Agent 开发；议题：看清一次多 Agent 任务：计划里哪些任务并行、哪些串行、关键路径是哪条，实际每个任务何时运行、调了哪些工具
- 编码：有向无环图 + 序列与事件流；重点：先后与依赖方向、时间与演化、跨视图的同一对象；把握：官方页面直接写了
- 编码所依据的原文：
  - 回答的问题：“which tasks run in parallel, which are sequential, which agents are involved, and the critical path” [✓](https://docs.agentensemble.net/guides/visualization/)
  - 编码：“(gray = normal, red = critical path)” [✓](https://docs.agentensemble.net/guides/visualization/)
  - 编码：“L0, L1, … badges show the topological level” [✓](https://docs.agentensemble.net/guides/visualization/)
  - 交互：“Zoom slider to expand the time axis for fine-grained inspection” [✓](https://docs.agentensemble.net/guides/visualization/)
  - 抽象与层级：“with drill-down into LLM calls, tool invocations, and agent conversations” [？](https://docs.agentensemble.net/guides/visualization/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“DAG file (.dag.json)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 处理的材料：“Trace file (.trace.json)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 处理的材料：“This example shows how to export both a pre-execution DAG and a post-execution trace” [✓](https://docs.agentensemble.net/examples/visualization/)
- 处理的材料：“Write trace to a file” [✓](https://docs.agentensemble.net/examples/metrics/)
- 对象：“renders the task dependency DAG” [✓](https://docs.agentensemble.net/guides/visualization/)
- 对象：“which agents are involved” [✓](https://docs.agentensemble.net/guides/visualization/)
- 对象：“show tool invocations at the bottom of each bar” [✓](https://docs.agentensemble.net/guides/visualization/)
- 关系：“Edges are dependency arrows (gray = normal, red = critical path)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 关系：“show when each LLM iteration ran within a task” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“execution metrics (when a trace is loaded alongside the DAG)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“showing when each task ran” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“shows tool name, arguments, result, outcome, and timing” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“enables conversation history” [✓](https://docs.agentensemble.net/guides/visualization/)
- 视图：“The viewer provides two views:” [✓](https://docs.agentensemble.net/guides/visualization/)
- 视图：“Flow View — renders the task dependency graph before or after execution” [✓](https://docs.agentensemble.net/guides/visualization/)
- 视图：“Timeline View — renders a Gantt-chart-style execution timeline” [✓](https://docs.agentensemble.net/guides/visualization/)
- 编码：“Nodes are colored by agent role” [✓](https://docs.agentensemble.net/guides/visualization/)
- 编码：“Tool call markers (green/red/gray)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 交互：“Click a node to open the detail panel showing task description, agent info, and execution metrics” [✓](https://docs.agentensemble.net/guides/visualization/)
- 交互：“Click a task bar: shows task description, prompts, metrics, final output, and LLM iteration list” [✓](https://docs.agentensemble.net/guides/visualization/)
- 交互：“Click a tool marker: shows tool name, arguments, result, outcome, and timing” [✓](https://docs.agentensemble.net/guides/visualization/)
- 抽象与层级：“Zoom slider to expand the time axis for fine-grained inspection” [✓](https://docs.agentensemble.net/guides/visualization/)

</details>

<a id="agentprism"></a>

### AgentPrism

- 领域：AI Agent 观测；议题：调试 Agent 运行，看时间和成本浪费在哪
- 编码：层级与树 + 序列与事件流；重点：包含与层次、时间与演化、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 视图：“Tree View on the left, Timeline on the right” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
  - 编码：“Color-coded status indicators (green = success, red = error, yellow = warning)” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
  - 抽象与层级：“Collapsed summary for repetitive sequences” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
  - 抽象与层级：“We found that engineers wanted hierarchy above all” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
  - 回答的问题：“Timeline View quickly points to where time and money are being wasted.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“So, we built React components that transform raw OpenTelemetry trace data into interactive visualizations.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 处理的材料：“converting OpenTelemetry and Langfuse traces to UI-ready formats for AI agent trace visualization.” [✓](https://registry.npmjs.org/@evilmartians%2fagent-prism-data)
- 对象：“Input/output data for each step” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 对象：“Build hierarchical tree structure from spans” [✓](https://registry.npmjs.org/@evilmartians%2fagent-prism-data)
- 关系：“Shows parent-child relationships between agent steps” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 关系：“Tree View displays the hierarchical trace structure” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 属性与度量：“Real-time cost accumulation with dollar amounts” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 属性与度量：“getDurationMs, getTotalCost, getTotalTokens” [？](https://registry.npmjs.org/@evilmartians%2fagent-prism-data)
- 视图：“Tree View displays the hierarchical trace structure” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 视图：“Timeline View shows a Gantt-style execution flow” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 视图：“The Details Panel displays a compressed span of information” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 编码：“Red highlighting for problematic patterns” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 交互：“transform raw OpenTelemetry trace data into interactive visualizations” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 交互：“progressive disclosure keeps deep structures navigable” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 回答的问题：“We chose these 4 because they directly address the core debugging workflow.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 回答的问题：“cuts debugging time from hours to seconds” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 抽象与层级：“progressive disclosure keeps deep structures navigable and minimizes on-screen noise and navigation cost.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 为什么这样画：“Tree View was the most effective since progressive disclosure keeps deep structures navigable and minimizes on-screen noise and navigation cost.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 为什么这样画：“human brains excel at visual pattern recognition. This means that loops invisible in JSON become glaringly clear when made visual.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 为什么这样画：“We chose these 4 because they directly address the core debugging workflow.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 为什么这样画：“The Sequence Diagram is ideal for onboarding users and introducing the concept of agent traces.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 原来的问题：“The only problem? The answer is buried within a terrible wall of JSON logs, and it’s impossible to see the flow” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 原来的问题：“If you’re debugging them by parsing JSON logs at midnight, you’re suffering needlessly.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 原来的问题：“Great tools, but we realized they solve different parts of the same problem.” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)
- 原来的问题：“Instead of choosing between multiple complex tools, we’re bringing the essential features together” [✓](https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces)

</details>

<a id="otel-genai-semconv"></a>

### OpenTelemetry GenAI 语义约定

- 领域：AI Agent 观测；议题：规定 AI 和 Agent 的运行记录该有哪些字段（后面所有可视化的数据来源）
- 编码：序列与事件流；重点：对象上的度量；把握：证据很少
- 说明：这是“数据先于图”的一例：可视化假定的结构（谁是父、谁是子、带什么属性）要在这一层先定下来。官方页面已迁到别处，这里没读到 span 的定义。
- 编码所依据的原文：
  - 属性与度量：“The name of the operation being performed.” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
  - 对象：“Name of the tool utilized by the agent.” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
<details><summary>本案例读到的其他原文摘录</summary>

- 对象：“Free-form description of the GenAI agent” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- 对象：“The tool description.” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- 关系：“Name of the tool utilized by the agent.” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- 属性与度量：“Type of the tool utilized by the agent” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- 属性与度量：“Moved to the OpenTelemetry GenAI semantic conventions repository” [✓](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)

</details>
- 没读到：input_material；views；encodings；interactions；questions；abstraction；注：spans、事件、父子关系在本次读到的 opentelemetry.io 页面中未找到；页面原文 “Important GenAI semantic conventions have moved to the OpenTelemetry GenAI semantic conventions repository” 指向 github.com 上的外部仓库，本次未访问

<a id="openllmetry"></a>

### OpenLLMetry

- 领域：AI Agent 观测；议题：以不改代码的方式采集 LLM 应用的运行追踪
- 编码：序列与事件流；重点：包含与层次；把握：证据很少
- 编码所依据的原文：
  - 对象：“Workflows, Tasks, Agents and Tools” [✓](https://docs.traceloop.com/docs/openllmetry/introduction)
  - 回答的问题：“allows you to easily start monitoring and debugging the execution of your LLM app” [✓](https://docs.traceloop.com/docs/openllmetry/introduction)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“allows you to easily start monitoring and debugging the execution of your LLM app” [✓](https://docs.traceloop.com/docs/openllmetry/introduction)

</details>
- 没读到：relations；attributes；views；encodings；interactions；abstraction

<a id="jaeger"></a>

### Jaeger

- 领域：分布式系统运维；议题：找出一次请求流经了哪些服务，性能瓶颈和错误在哪
- 编码：层级与树 + 一般图与网络；重点：时间与演化、包含与层次、连通与邻域；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 回答的问题：“Find & fix performance bottlenecks” [✓](https://www.jaegertracing.io/)
  - 关系：“Analyze service dependencies” [✓](https://www.jaegertracing.io/)
  - 视图：“uiTimelineHideMinimap=1 removes the minimap, entirely, regardless of whether the trace header is expanded or not.” [✓](https://www.jaegertracing.io/docs/2.22/deployment/frontend-ui/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Jaeger: open source, distributed tracing platform” [✓](https://www.jaegertracing.io/)
- 处理的材料：“Jaeger maps the flow of requests and data as they traverse a distributed system.” [✓](https://www.jaegertracing.io/)
- 对象：“These requests may make calls to multiple services, which may introduce their own delays or errors.” [✓](https://www.jaegertracing.io/)
- 对象：“Jaeger maps the flow of requests and data as they traverse a distributed system.” [✓](https://www.jaegertracing.io/)
- 关系：“These requests may make calls to multiple services” [✓](https://www.jaegertracing.io/)
- 属性与度量：“which may introduce their own delays or errors” [✓](https://www.jaegertracing.io/)
- 视图：“Trace Page Configuration options” [✓](https://www.jaegertracing.io/docs/2.22/deployment/frontend-ui/)
- 视图：“Search Page Configuration options” [✓](https://www.jaegertracing.io/docs/2.22/deployment/frontend-ui/)
- 视图：“Trace Graph UI Controls” [✓](https://www.jaegertracing.io/docs/2.22/deployment/frontend-ui/)
- 交互：“button to go back to the results page” [✓](https://www.jaegertracing.io/docs/2.22/deployment/frontend-ui/)
- 回答的问题：“Track down root causes” [✓](https://www.jaegertracing.io/)
- 回答的问题：“Monitor and troubleshoot workflows in complex distributed systems” [✓](https://www.jaegertracing.io/)

</details>
- 没读到：encodings；abstraction

<a id="grafana-tempo"></a>

### Grafana Tempo

- 领域：分布式系统运维；议题：理解分布式系统的结构，找出瓶颈和互联问题
- 编码：层级与树 + 一般图与网络；重点：连通与邻域、关系上的类型与量；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“Analyzes traces to map relationships between services” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
  - 回答的问题：“help you to understand the structure of a distributed system” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/service_graphs/)
  - 属性与度量：“Calculates the total count and duration of spans based on dimensions like service name, operation, span kind, status code, and other span attributes.” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The metrics-generator looks at incoming spans, and calculates rate, error, and duration (RED) metrics from them” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
- 处理的材料：“Traces are composed of one or more spans.” [✓](https://grafana.com/docs/tempo/latest/introduction/)
- 对象：“A span is a unit of work within a trace that has a start time relative to the beginning of the trace, a duration” [✓](https://grafana.com/docs/tempo/latest/introduction/)
- 对象：“Analyzes traces to map relationships between services” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
- 对象：“A service graph is a visual representation of the interrelationships between various services.” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/service_graphs/)
- 关系：“It usually has a reference to a parent span, unless it’s the first, or root, span in a trace.” [✓](https://grafana.com/docs/tempo/latest/introduction/)
- 关系：“the connections and dependencies between its components” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/service_graphs/)
- 属性与度量：“It frequently includes key/value attributes that are relevant to the span itself, for example the HTTP method used in the request” [✓](https://grafana.com/docs/tempo/latest/introduction/)
- 属性与度量：“calculates rate, error, and duration (RED) metrics from them” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
- 视图：“Service graph view” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
- 视图：“A service graph is a visual representation of the interrelationships between various services.” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/service_graphs/)
- 交互：“Analyze service graph data” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)
- 回答的问题：“Traces are the ideal observability signal for discovering bottlenecks and interconnection issues.” [✓](https://grafana.com/docs/tempo/latest/introduction/)
- 抽象与层级：“Calculates the total count and duration of spans based on dimensions like service name, operation, span kind” [✓](https://grafana.com/docs/tempo/latest/metrics-from-traces/)

</details>
- 没读到：encodings

<a id="marquez"></a>

### Marquez

- 领域：数据工程；议题：数据模式改变时，审计并排查下游受影响的作业
- 编码：有向无环图；重点：先后与依赖方向、时间与演化；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 关系：“dependencies between jobs and the datasets they produce and consume” [✓](https://marquezproject.ai/docs/quickstart/)
  - 回答的问题：“especially useful for auditing or troubleshooting impacted jobs downstream of a schema change” [✓](https://marquezproject.ai/docs/quickstart/)
  - 属性与度量：“compare a previous schema version with the latest schema version” [✓](https://marquezproject.ai/docs/quickstart/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Marquez enables consuming, storing, and visualizing OpenLineage metadata from across an organization” [✓](https://marquezproject.ai/)
- 处理的材料：“for real-time collection of information from running jobs and applications” [✓](https://marquezproject.ai/)
- 对象：“normalized representation of the end-to-end metadata of your pipelines (composed of multiple jobs)” [✓](https://marquezproject.ai/docs/quickstart/)
- 对象：“View Dataset Metadata” [✓](https://marquezproject.ai/docs/quickstart/)
- 属性与度量：“A job version pointer is also present and mapped to a unique referenceable link to code, the latest run ID” [✓](https://marquezproject.ai/docs/quickstart/)
- 视图：“then explore the sample lineage metadata via the web UI” [✓](https://marquezproject.ai/docs/quickstart/)
- 视图：“Marquez enables consuming, storing, and visualizing OpenLineage metadata” [✓](https://marquezproject.ai/)
- 交互：“Search Job Metadata” [✓](https://marquezproject.ai/docs/quickstart/)
- 交互：“View Job Metadata” [✓](https://marquezproject.ai/docs/quickstart/)
- 交互：“View Dataset Metadata” [✓](https://marquezproject.ai/docs/quickstart/)
- 回答的问题：“serving use cases including data governance, data quality monitoring, and performance analytics” [✓](https://marquezproject.ai/)
- 回答的问题：“highly flexible data lineage queries across all datasets” [✓](https://marquezproject.ai/docs/quickstart/)
- 抽象与层级：“your pipelines (composed of multiple jobs)” [✓](https://marquezproject.ai/docs/quickstart/)

</details>
- 没读到：encodings

<a id="neodash"></a>

### NeoDash

- 领域：图数据库应用；议题：用图数据库里的查询结果搭交互看板
- 编码：一般图与网络；重点：对象上的度量；把握：证据很少
- 说明：官方页面没写数据对象和关系是什么，重点部分由用户的查询决定。这是“结构存在数据库里，视图由查询临时投影”的一例。
- 编码所依据的原文：
  - 视图：“tables, graphs, bar charts, line charts, maps and more” [✓](https://neo4j.com/labs/neodash/)
  - 处理的材料：“Create visualizations directly from Cypher” [✓](https://neo4j.com/labs/neodash/)
<details><summary>本案例读到的其他原文摘录</summary>

- 交互：“A low-code dashboard builder with a drag-and-drop interface” [✓](https://neo4j.com/labs/neodash/)
- 交互：“The ability to add customization and interactivity to dashboards” [✓](https://neo4j.com/labs/neodash/)
- 回答的问题：“It lets you build an interactive dashboard with tables, graphs, bar charts, line charts, maps and more.” [✓](https://neo4j.com/labs/neodash/)

</details>
- 没读到：entities；relations；attributes；encodings；abstraction

<a id="dify"></a>

### Dify

- 领域：AI Agent 开发；议题：搭建 AI 工作流，并逐节点测试、检查数据怎么流过去
- 编码：一般图与网络；重点：先后与依赖方向、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 属性与度量：“After testing, click “Last run” to see execution details including inputs, outputs, timing, and any error messages.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
  - 视图：“The Variable Inspector shows you all the data flowing through your workflow.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/variable-inspect)
  - 交互：“You can test any node individually without running the entire workflow.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
  - 抽象与层级：“reuse it as an agent node inside a workflow” [✓](https://dify.ai/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Create agents, agentic workflows, and chatbots that draw on your own data” [✓](https://docs.dify.ai/en/home)
- 处理的材料：“Create repeatable pipelines for files, websites” [✓](https://dify.ai/)
- 处理的材料：“Prepare searchable knowledge bases” [✓](https://dify.ai/)
- 对象：“reuse it as an agent node inside a workflow” [✓](https://dify.ai/)
- 对象：“Every node execution creates a record.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
- 对象：“Build Agents with Skills , Tools , and Knowledge” [✓](https://dify.ai/)
- 关系：“Use it as an app, embed it into a website, or reuse it as an agent node inside a workflow.” [✓](https://dify.ai/)
- 属性与度量：“It captures inputs and outputs from each node after they run” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/variable-inspect)
- 视图：“Workflow Studio Visual Builder for Agentic Workflows” [✓](https://dify.ai/)
- 视图：“Click “Last run” on any node to see its most recent execution details” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
- 交互：“Select the node, provide test input in its settings panel, and click Run to see the output.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
- 交互：“Just change the variable values in the inspector and run the node again.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
- 回答的问题：“Test individual nodes or run through your workflow step-by-step to catch issues before publishing.” [✓](https://docs.dify.ai/en/cloud/use-dify/debug/step-run)
- 回答的问题：“so teams can test, debug, deploy, and hand it off with confidence” [✓](https://dify.ai/)
- 回答的问题：“Build, test, and launch AI apps without managing infrastructure.” [✓](https://dify.ai/)

</details>
- 没读到：encodings

<a id="langflow"></a>

### Langflow

- 领域：AI Agent 开发；议题：用拖拽组件搭 AI 流程，并在 Playground 里实时测试
- 编码：一般图与网络；重点：先后与依赖方向；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 视图：“The visual editor simplifies prototyping of application” [✓](https://docs.langflow.org/)
  - 交互：“You can use the Playground to test flows without having to build your entire application stack.” [✓](https://docs.langflow.org/)
  - 抽象与层级：“Use components and flows as agent tools.” [✓](https://docs.langflow.org/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“converts audio files into structured data” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 处理的材料：“Your role is to analyze call transcripts and classify them based on” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 对象：“A parser component formats the transcript data appropriately before sending it to the agent for analysis.” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 对象：“agent designed for call analysis” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 对象：“Create a prompt template with dynamic variables.” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 对象：“Use components and flows as agent tools.” [✓](https://docs.langflow.org/)
- 关系：“before sending it to the agent for analysis” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 关系：“Connect Langflow to external MCP servers.” [✓](https://docs.langflow.org/)
- 属性与度量：“- Urgency: e.g., Low, Medium, High.” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 属性与度量：“- Sentiment: e.g., Positive, Neutral, Negative.” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 属性与度量：“- Resolution: e.g., Resolved, Escalated, Pending.” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 属性与度量：“structured JSON data containing both the original transcript and classification details including topic, resolution, sentiment, and urgency fields” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 视图：“This structured output is then displayed through a chat interface” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 视图：“Langflow's visual interface lets you build this pipeline quickly without extensive coding” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 交互：“You can interact with your flows and get real-time feedback about flow logic” [✓](https://docs.langflow.org/)
- 交互：“You can also use tweaks to temporarily override flow settings at runtime.” [✓](https://docs.langflow.org/)
- 交互：“Use the Langflow API to run flows from your application code.” [✓](https://docs.langflow.org/)
- 回答的问题：“Build an automated call transcription and classification system using Langflow” [✓](https://www.langflow.org/templates/use-langflow-to-process-and-classify-call-transcripts/)
- 抽象与层级：“In addition to the core components, Langflow supports custom components.” [✓](https://docs.langflow.org/)

</details>
- 没读到：encodings；focus 中的“与可观测性平台集成”在已读的三个页面中未找到原文（docs.langflow.org 页面内搜索 observab 无命中），未读集成类页面

<a id="n8n"></a>

### n8n

- 领域：业务自动化；议题：工作流在生产中失败后，把当时的执行数据带回编辑器里调试
- 编码：一般图与网络 + 序列与事件流；重点：跨视图的同一对象、时间与演化；把握：页面信息支持，归类靠推断
- 说明：“Debug in editor”把运行时的一条记录接回设计时的图——两种结构靠对象身份连起来。
- 编码所依据的原文：
  - 对象：“An execution is a single run of a workflow.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions)
  - 关系：“n8n copies the execution data into your current workflow” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“You can load data from a previous execution into your current workflow.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 对象：“Publish a version of the workflow to put it into production.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions)
- 对象：“Explore +10k workflow automation templates” [✓](https://n8n.io/workflows/)
- 关系：“To load data from a previous execution” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 属性与度量：“For failed executions: select Debug in editor.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 属性与度量：“For successful executions: select Copy to editor.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 属性与度量：“Manual: Run workflows manually by clicking Execute Workflow” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions)
- 属性与度量：“Production workflows run automatically.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions)
- 视图：“to view the Executions list. Select the execution you want to debug.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 视图：“View all executions: view and filter all executions across all your workflows.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions)
- 交互：“For failed executions: select Debug in editor.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 交互：“For successful executions: select Copy to editor.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 交互：“make changes to your workflow to fix it, then re-run it with the previous execution data.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 交互：“You can filter the executions list.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
- 回答的问题：“This is useful for debugging data from failed production executions” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 回答的问题：“you can see a failed execution, make changes to your workflow to fix it, then re-run it with the previous execution data.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
- 抽象与层级：“View all executions: view and filter all executions across all your workflows.” [✓](https://docs.n8n.io/build/understand-workflows/understand-executions)

</details>
- 没读到：encodings

<a id="node-red"></a>

### Node-RED

- 领域：物联网与事件流；议题：把节点连起来搭事件驱动的流，并看消息在流里是什么样
- 编码：一般图与网络；重点：连通与邻域、对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 视图：“The Debug sidebar displays messages passed to Debug nodes within the flow” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
  - 抽象与层级：“Groups Subflows Selection Arranging Nodes” [✓](https://nodered.org/docs/user-guide/editor/)
  - 对象：“build, wire together, and run your flows” [✓](https://nodered.org/docs/user-guide/editor/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“messages passed to Debug nodes within the flow” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
- 处理的材料：“certain log messages from the runtime” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
- 对象：“Find new nodes, share your flows and see what other people have done with Node-RED.” [✓](https://flows.nodered.org/)
- 对象：“messages passed to Debug nodes within the flow” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
- 关系：“build, wire together, and run your flows” [✓](https://nodered.org/docs/user-guide/editor/)
- 关系：“messages passed to Debug nodes within the flow” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
- 属性与度量：“certain log messages from the runtime” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
- 视图：“Sidebar Explorer Information Help Debug Config nodes Context data” [✓](https://nodered.org/docs/user-guide/editor/)
- 视图：“The workspace in the middle is where the work happens” [✓](https://nodered.org/docs/user-guide/editor/)
- 交互：“holds the deploy button and main menu” [✓](https://nodered.org/docs/user-guide/editor/)
- 交互：“build, wire together, and run your flows” [✓](https://nodered.org/docs/user-guide/editor/)
- 回答的问题：“how to use the Debug sidebar to understand the structure of messages” [✓](https://nodered.org/docs/user-guide/editor/sidebar/debug)
- 回答的问题：“Find new nodes, share your flows and see what other people have done with Node-RED.” [✓](https://flows.nodered.org/)

</details>
- 没读到：encodings

<a id="flowise"></a>

### Flowise

- 领域：AI Agent 开发；议题：可视化搭建带条件、循环、人工介入的多 Agent 流程
- 编码：一般图与网络；重点：先后与依赖方向、时间与演化；把握：页面信息支持，归类靠推断
- 说明：官网已宣布停止运营（见 projects/L3.yaml）。
- 编码所依据的原文：
  - 对象：“Executes a defined "sub-flow" — a sequence of nodes nested within it — for each item in an input array” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
  - 关系：“Shared state enables data exchange between agents, especially useful for passing data across branches or non-adjacent steps in a flow.” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
  - 属性与度量：“Each checkpoint is saved, allowing the workflow to resume from the same point even after an application restart.” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“It can accept input either directly from the chat interface or through a customizable form presented to the user.” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 处理的材料：“It takes an array, either provided directly or referenced via a variable” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 对象：“Condition Node Implements deterministic branching logic within the workflow based on defined rules.” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 对象：“the Flow State provides an explicit mechanism for managing and sharing data throughout the workflow” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 对象：“Shared state enables data exchange between agents” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 关系：“data can be passed between nodes by referencing the outputs of any previously executed node in the current flow” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 属性与度量：“Execution is paused while awaiting human input, without blocking the running thread.” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 属性与度量：“We're sunsetting Flowise. Learn more” [✓](https://flowiseai.com/)
- 视图：“Build AI Agents, Visually” [✓](https://flowiseai.com/)
- 交互：“Agents can also be configured to request permission before executing tools” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 交互：“Execution is paused while awaiting human input” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 回答的问题：“Learn how to build multi-agents system using Agentflow V2” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 抽象与层级：“a sequence of nodes nested within it” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)
- 抽象与层级：“clear separation between components, allowing workflows to become both more sophisticated and easier to design” [✓](https://docs.flowiseai.com/using-flowise/agentflowv2)

</details>
- 没读到：encodings

<a id="agentscope"></a>

### AgentScope 2.0

- 领域：AI Agent 开发；议题：观察一个由领导者协调多个工作者的 Agent 团队怎么运作
- 编码：层级与树 + 序列与事件流；重点：包含与层次、时间与演化、连通与邻域；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 对象：“A leader agent assembling a team and coordinating workers in the example web UI.” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
  - 视图：“the matching examples/web_ui frontend renders team membership and per-worker streams out of the box” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
  - 关系：“observe them exchange messages in the UI” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“inspect its full event stream directly in the terminal” [✓](https://docs.agentscope.io/en/versions/2.0.9/building-blocks/console)
- 对象：“A persistent group of agent members owned by one user.” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
- 关系：“renders team membership and per-worker streams out of the box” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
- 属性与度量：“watch workers come online” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
- 属性与度量：“A TeamRecord carries the team’s identity” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
- 视图：“inspect its full event stream directly in the terminal” [✓](https://docs.agentscope.io/en/versions/2.0.9/building-blocks/console)
- 视图：“plus a frontend UI and development SDK” [✓](https://docs.agentscope.io/en/versions/2.0.9)
- 交互：“you can chat with it and inspect its full event stream directly in the terminal” [✓](https://docs.agentscope.io/en/versions/2.0.9/building-blocks/console)
- 交互：“Create a team” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)
- 回答的问题：“If you need to quickly try out or debug an agent” [？](https://docs.agentscope.io/en/versions/2.0.9/building-blocks/console)
- 抽象与层级：“Full-stack coverage with development SDK, frontend UI, multi-tenant multi-session backend, and distributed deployment” [✓](https://docs.agentscope.io/en/versions/2.0.9)
- 抽象与层级：“A persistent group of agent members owned by one user.” [✓](https://docs.agentscope.io/en/versions/2.0.9/deploy/agent-team)

</details>
- 没读到：encodings

<a id="langgraph"></a>

### LangGraph / Studio

- 领域：AI Agent 开发；议题：调试 Agent 的状态：回到某个检查点重放，或分叉出另一条路径
- 编码：一般图与网络 + 序列与事件流；重点：先后与依赖方向、时间与演化；把握：页面信息支持，归类靠推断
- 说明：“分叉”让线性的运行历史长成树——对比两条路径靠的是共享前缀。
- 编码所依据的原文：
  - 关系：“Branch from a prior checkpoint with modified state to explore an alternative path” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
  - 视图：“Graph mode exposes the full feature-set and is useful when you would like as many details about the execution of your agent” [✓](https://docs.langchain.com/langsmith/studio)
  - 交互：“Debug agent state via time travel” [✓](https://docs.langchain.com/langsmith/studio)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“agentic systems that implement the Agent Server API protocol” [✓](https://docs.langchain.com/langsmith/studio)
- 处理的材料：“Use get_state_history to find the checkpoint you want to replay from” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
- 对象：“Visualize your graph architecture” [✓](https://docs.langchain.com/langsmith/studio)
- 对象：“LangGraph supports time travel through checkpoints” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
- 对象：“Manage threads” [✓](https://docs.langchain.com/langsmith/studio)
- 对象：“Define and update state” [✓](https://docs.langchain.com/oss/python/langgraph/use-graph-api)
- 关系：“Retry from a prior checkpoint” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
- 属性与度量：“History is in reverse chronological order” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
- 属性与度量：“including the nodes traversed” [✓](https://docs.langchain.com/langsmith/studio)
- 视图：“Visualize your graph architecture” [✓](https://docs.langchain.com/langsmith/studio)
- 交互：“Run and interact with your agent” [✓](https://docs.langchain.com/langsmith/studio)
- 交互：“Iterate on prompts” [✓](https://docs.langchain.com/langsmith/studio)
- 交互：“Replay past executions and fork to explore alternative paths in LangGraph” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
- 回答的问题：“enables visualization, interaction, and debugging of agentic systems” [✓](https://docs.langchain.com/langsmith/studio)
- 回答的问题：“Replay past executions and fork to explore alternative paths in LangGraph” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
- 抽象与层级：“Studio supports two modes:” [✓](https://docs.langchain.com/langsmith/studio)
- 抽象与层级：“Multiple interrupts Subgraphs” [✓](https://docs.langchain.com/oss/python/langgraph/use-time-travel)

</details>
- 没读到：encodings

<a id="agentensemble"></a>

### AgentEnsemble

- 领域：AI Agent 开发；议题：编排多 Agent 任务，并在关键点让人审核、修改或叫停
- 编码：有向无环图 + 序列与事件流；重点：先后与依赖方向、时间与演化；把握：证据很少
- 说明：可视化部分与 agentensemble-viz 相同，这里只记审核门这一点。
- 编码所依据的原文：
  - 视图：“The agentensemble-web module provides a Live Execution Dashboard that turns the browser into a real-time GUI for ensemble runs.” [✓](https://docs.agentensemble.net/guides/visualization/)
  - 交互：“can pause pipeline execution at three timing points to collect human approval, corrections, or clarification” [✓](https://docs.agentensemble.net/guides/review/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Generated by EnsembleDevTools.exportDag() . Contains the task dependency structure, agent metadata, topological levels, and critical path.” [✓](https://docs.agentensemble.net/guides/visualization/)
- 处理的材料：“Contains the full execution trace: all task traces, LLM interactions, tool calls, metrics, delegation chains, and agent conversation history” [✓](https://docs.agentensemble.net/guides/visualization/)
- 对象：“The Flow View renders the task dependency DAG: Nodes are colored by agent role” [✓](https://docs.agentensemble.net/guides/visualization/)
- 对象：“One horizontal swimlane per agent Task bars (colored) show when each task ran” [✓](https://docs.agentensemble.net/guides/visualization/)
- 对象：“LLM call sub-bars (indigo) show when each LLM iteration ran within a task” [✓](https://docs.agentensemble.net/guides/visualization/)
- 对象：“Tool call markers (green/red/gray) show tool invocations at the bottom of each bar” [✓](https://docs.agentensemble.net/guides/visualization/)
- 关系：“Edges are dependency arrows (gray = normal, red = critical path)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 关系：“which tasks run in parallel, which are sequential, which agents are involved, and the critical path” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“Prompts, tool args/results, timing, token counts” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“showing task description, agent info, and execution metrics (when a trace is loaded alongside the DAG)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“L0, L1, … badges show the topological level (tasks at the same level can run in parallel)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 属性与度量：“CP badge marks tasks on the critical path” [✓](https://docs.agentensemble.net/guides/visualization/)
- 视图：“The Flow View renders the task dependency DAG” [✓](https://docs.agentensemble.net/guides/visualization/)
- 视图：“The Timeline View renders a Gantt-chart-style execution timeline” [✓](https://docs.agentensemble.net/guides/visualization/)
- 视图：“It replaces the console prompt with a browser-based review panel” [？](https://docs.agentensemble.net/guides/visualization/)
- 编码：“Nodes are colored by agent role” [✓](https://docs.agentensemble.net/guides/visualization/)
- 编码：“Edges are dependency arrows (gray = normal, red = critical path)” [✓](https://docs.agentensemble.net/guides/visualization/)
- 编码：“L0, L1, … badges show the topological level” [✓](https://docs.agentensemble.net/guides/visualization/)
- 编码：“One horizontal swimlane per agent” [✓](https://docs.agentensemble.net/guides/visualization/)
- 交互：“Click any element to open the detail panel” [✓](https://docs.agentensemble.net/guides/visualization/)
- 交互：“Zoom slider to expand the time axis for fine-grained inspection” [✓](https://docs.agentensemble.net/guides/visualization/)
- 交互：“with drill-down into LLM calls, tool invocations” [✓](https://docs.agentensemble.net/guides/visualization/)
- 回答的问题：“which tasks run in parallel, which are sequential, which agents are involved, and the critical path” [✓](https://docs.agentensemble.net/guides/visualization/)
- 回答的问题：“to collect human approval, corrections, or clarification” [✓](https://docs.agentensemble.net/guides/review/)
- 抽象与层级：“Zoom slider to expand the time axis for fine-grained inspection” [✓](https://docs.agentensemble.net/guides/visualization/)
- 抽象与层级：“with drill-down into LLM calls, tool invocations” [✓](https://docs.agentensemble.net/guides/visualization/)
- 抽象与层级：“LLM call sub-bars (indigo) show when each LLM iteration ran within a task” [✓](https://docs.agentensemble.net/guides/visualization/)
- 抽象与层级：“L0, L1, … badges show the topological level (tasks at the same level can run in parallel)” [✓](https://docs.agentensemble.net/guides/visualization/)

</details>

<a id="autogen"></a>

### AutoGen / AutoGen Studio

- 领域：AI Agent 开发；议题：快速原型化 Agent 团队并观察它们的消息流
- 编码：一般图与网络 + 序列与事件流；重点：先后与依赖方向、时间与演化；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 关系：“Visual representation of message flow through a control transition graph” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
  - 视图：“A visual interface for creating agent teams through declarative specification (JSON) or drag-and-drop” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
  - 回答的问题：“It is not meant to be a production-ready app.” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“creating agent teams through declarative specification (JSON) or drag-and-drop” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 处理的材料：“Setup and test endpoints based on a team configuration” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 对象：“Supports configuration of all core components: teams, agents, tools, models, and termination conditions” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 对象：“Interactive sessions with teams using UserProxyAgent” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 对象：“Central hub for discovering and importing community-created components” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 关系：“Live message streaming between agents” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 属性与度量：“Fully compatible with AgentChat’s component definitions” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 属性与度量：“Full run control with the ability to pause or stop execution” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 视图：“Interactive environment for testing and running agent teams” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 视图：“Visual representation of message flow through a control transition graph” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 交互：“or drag-and-drop” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 交互：“Interactive sessions with teams using UserProxyAgent” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 交互：“Full run control with the ability to pause or stop execution” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 交互：“Export and run teams in python code” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 回答的问题：“rapidly prototype AI agents, enhance them with tools, compose them into teams and interact with them to accomplish tasks” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- 回答的问题：“help you rapidly prototype AI agents, enhance them with skills, compose them into workflows and interact with them to accomplish tasks” [✓](https://pypi.org/project/autogenstudio/)
- 回答的问题：“An web-based UI for prototyping with agents without writing code.” [✓](https://microsoft.github.io/autogen/stable/)
- 抽象与层级：“compose them into teams” [✓](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)

</details>
- 没读到：encodings

<a id="langfuse"></a>

### Langfuse

- 领域：AI 应用观测；议题：弄清应用内部发生了什么，并用评测持续改进
- 编码：层级与树 + 表与多维属性；重点：时间与演化、对象上的度量、跨视图的同一对象；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 处理的材料：“structured logs of every request that capture the exact prompt sent, the model's response, token usage, latency” [✓](https://langfuse.com/docs/observability/overview)
  - 属性与度量：“Analyze cost, latency, volume, and quality in custom dashboards” [✓](https://langfuse.com/docs/observability/overview)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“you score live traces in production, turn interesting examples into datasets, run experiments to compare changes” [✓](https://langfuse.com/docs/evaluation/overview)
- 对象：“Open Tracing and select your latest request to inspect its trace.” [✓](https://langfuse.com/docs/demo)
- 对象：“Online Trace traces · sessions · agents · prompts” [✓](https://langfuse.com/docs/evaluation/overview)
- 对象：“Build datasets datasets · features-as-tests” [✓](https://langfuse.com/docs/evaluation/overview)
- 对象：“Monitor application quality with scores” [✓](https://langfuse.com/docs/observability/overview)
- 关系：“how evaluators, scores, datasets, and experiments fit together” [✓](https://langfuse.com/docs/evaluation/overview)
- 关系：“turn interesting examples into datasets” [✓](https://langfuse.com/docs/evaluation/overview)
- 关系：“It also gives your evaluations real production traces to run on” [✓](https://langfuse.com/docs/observability/overview)
- 属性与度量：“Track model usage and cost” [✓](https://langfuse.com/docs/observability/overview)
- 视图：“Open Tracing and select your latest request to inspect its trace.” [✓](https://langfuse.com/docs/demo)
- 视图：“Online Monitor dashboards · LLM-as-judge · feedback” [✓](https://langfuse.com/docs/evaluation/overview)
- 视图：“Here's an example of a trace in the Langfuse UI” [✓](https://langfuse.com/docs/observability/overview)
- 交互：“Run a demo interaction below to generate real data.” [✓](https://langfuse.com/docs/demo)
- 交互：“Open the live shared project in Langfuse.” [✓](https://langfuse.com/docs/demo)
- 交互：“run experiments to compare changes” [✓](https://langfuse.com/docs/evaluation/overview)
- 交互：“judge the results with manual or automated evaluators” [✓](https://langfuse.com/docs/evaluation/overview)
- 回答的问题：“understand what's happening inside your application and why” [✓](https://langfuse.com/docs/observability/overview)
- 回答的问题：“so you can continuously measure and improve your system” [✓](https://langfuse.com/docs/observability/overview)
- 回答的问题：“to make sure your changes are ready for production” [✓](https://langfuse.com/docs/evaluation/overview)
- 抽象与层级：“It happens both online , on live production traces, and offline , before you ship a change.” [✓](https://langfuse.com/docs/evaluation/overview)

</details>
- 没读到：encodings

<a id="arize-phoenix"></a>

### Arize Phoenix

- 领域：AI 应用观测；议题：一步步看一次 AI 应用运行，调试行为并衡量输出质量
- 编码：层级与树 + 序列与事件流；重点：包含与层次、时间与演化、对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 抽象与层级：“Group related traces into conversations and user sessions” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
  - 回答的问题：“so you can debug behavior and understand where time is spent” [✓](https://arize.com/docs/phoenix)
  - 交互：“Span Replay — Debug by replaying LLM calls with different inputs” [✓](https://arize.com/docs/phoenix)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Phoenix accepts traces over OpenTelemetry (OTLP) and provides auto-instrumentation for popular frameworks” [✓](https://arize.com/docs/phoenix)
- 处理的材料：“A trace captures model calls, retrieval, tool use, and custom logic” [✓](https://arize.com/docs/phoenix)
- 处理的材料：“You can score traces & spans with LLM-based evaluators, code-based checks, or human labels” [✓](https://arize.com/docs/phoenix)
- 对象：“Add custom spans with decorators and wrappers” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 对象：“Organize traces into separate projects for different applications” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 对象：“Group related traces into conversations and user sessions” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 对象：“Prompt Management — Version, store, and deploy prompts” [✓](https://arize.com/docs/phoenix)
- 关系：“the sequence of operations, such as document retrieval, embedding generation, language model invocation, and response generation” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 关系：“Configure evaluators in the Phoenix UI and attach them to your datasets” [✓](https://arize.com/docs/phoenix/evaluation/llm-evals)
- 关系：“Phoenix scores experiment results automatically” [✓](https://arize.com/docs/phoenix/evaluation/llm-evals)
- 关系：“It is built on top of OpenTelemetry and is powered by OpenInference instrumentation” [✓](https://arize.com/docs/phoenix)
- 属性与度量：“Monitor latency, token usage, and error rates” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 属性与度量：“Add feedback, labels, and scores to your traces” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 属性与度量：“understand where time is spent” [✓](https://arize.com/docs/phoenix)
- 视图：“to provide a detailed timeline of the request’s execution” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 视图：“Prompt Playground — Experiment with prompts and models side-by-side” [✓](https://arize.com/docs/phoenix)
- 交互：“Score your traces with LLM-as-a-judge evaluators” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 交互：“Add feedback, labels, and scores to your traces” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 交互：“Experiment with prompts and models side-by-side” [✓](https://arize.com/docs/phoenix)
- 回答的问题：“understand and improve AI applications by giving you a workflow for debugging and iteration” [✓](https://arize.com/docs/phoenix)
- 回答的问题：“Evaluations help you measure the output quality of your application.” [✓](https://arize.com/docs/phoenix)
- 抽象与层级：“Organize traces into separate projects for different applications” [✓](https://arize.com/docs/phoenix/tracing/llm-traces)
- 抽象与层级：“Tracing lets you see what happened during a single run of your AI application, step by step.” [✓](https://arize.com/docs/phoenix)

</details>
- 没读到：encodings；phoenix-demo.arize.com 演示页（https://phoenix-demo.arize.com/）只读到标题 Phoenix，正文由 JS 渲染，没读到，未计入 pages_read

<a id="comet-opik"></a>

### Comet Opik

- 领域：AI 应用观测；议题：弄清 Agent 为什么失败、哪个 span 引起延迟
- 编码：层级与树 + 一般图与网络；重点：包含与层次、时间与演化、对象上的度量、跨视图的同一对象；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 回答的问题：“Which span caused the latency spike in this trace?” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
  - 视图：“Opik automatically generates visual representations of your agent workflows for Google ADK without requiring any additional configuration.” [✓](https://www.comet.com/docs/opik/tracing/advanced/log_agent_graphs)
  - 交互：“It can drill into individual spans, compare traces side by side, and search across your project for patterns.” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Ollie reads full span trees including inputs, outputs, latencies, token counts, and feedback scores.” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 处理的材料：“Evaluate traces from development, testing, or production” [✓](https://www.comet.com/site/products/opik/)
- 处理的材料：“A collection of test cases with inputs and optional expected outputs” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 对象：“Ollie reads the full span tree — every LLM call, tool invocation, and retrieval step” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 对象：“Traces, threads, datasets, experiments, and prompts are all queryable” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 对象：“Each evaluation run creates an Experiment — a record of every dataset item, your agent’s output, and the metric scores.” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 对象：“Agent Graphs are a great way to visualize the flow of an agent and simplifies it’s debugging.” [✓](https://www.comet.com/docs/opik/tracing/advanced/log_agent_graphs)
- 关系：“which you can access by clicking on Show Agent Graph in the trace sidebar” [✓](https://www.comet.com/docs/opik/tracing/advanced/log_agent_graphs)
- 关系：“Scoring functions that evaluate the output (e.g., Hallucination , AnswerRelevance , custom metrics)” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 关系：“visualize the flow of an agent” [✓](https://www.comet.com/docs/opik/tracing/advanced/log_agent_graphs)
- 属性与度量：“latencies, token counts, and feedback scores” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 属性与度量：“The pass rate is the ratio of passed items to total items” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 属性与度量：“An item passes if the number of passed runs meets the pass_threshold” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 属性与度量：“Score performance with 30+ metrics for answer relevance, context precision, task completion, hallucination, and more” [✓](https://www.comet.com/site/products/opik/)
- 视图：“Open Ollie from the trace view and describe what looks off.” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 视图：“Datasets & Metrics — quantitative scoring” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 交互：“by clicking on Show Agent Graph in the trace sidebar” [✓](https://www.comet.com/docs/opik/tracing/advanced/log_agent_graphs)
- 交互：“Collaborate with subject matter experts to annotate and fix underperforming traces.” [✓](https://www.comet.com/site/products/opik/)
- 交互：“Evaluate production traces in real time and get alerted if a user interaction fails your test criteria.” [✓](https://www.comet.com/site/products/opik/)
- 回答的问题：“Understand what your agent is doing, where it’s failing, and how to fix it.” [✓](https://www.comet.com/site/products/opik/)
- 回答的问题：“Why did the final answer ignore the retrieved context?” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 回答的问题：“Measuring quality across many traces with a common metric (hallucination, relevance, coherence)” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 抽象与层级：“It can drill into individual spans” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 抽象与层级：“Ollie reads the full span tree” [✓](https://www.comet.com/docs/opik/tracing/debug-agents)
- 抽象与层级：“Test Suites — assertion-based testing” [✓](https://www.comet.com/docs/opik/evaluation/concepts)
- 抽象与层级：“Datasets & Metrics — quantitative scoring” [✓](https://www.comet.com/docs/opik/evaluation/concepts)

</details>
- 没读到：encodings

<a id="agentops"></a>

### AgentOps

- 领域：AI 应用观测；议题：在会话的时间线上看 LLM 调用、工具调用和错误，并回放
- 编码：层级与树 + 序列与事件流；重点：时间与演化、包含与层次、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 视图：“Most powerful of all is the Session Waterfall.” [✓](https://docs.agentops.ai/v2/introduction)
  - 视图：“View a meta-analysis of all of your sessions in a single view.” [✓](https://docs.agentops.ai/v2/introduction)
  - 交互：“Rewind and replay agent runs with point in time precision.” [✓](https://www.agentops.ai/)
  - 关系：“Hierarchical structure of operations” [✓](https://docs.agentops.ai/v2/concepts/traces.md)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“After setting up AgentOps, each execution of your program is recorded as a session and the above data is automatically recorded for you.” [✓](https://docs.agentops.ai/v2/introduction)
- 处理的材料：“Visually track events such as LLM calls, tools, and multi-agent interactions.” [✓](https://www.agentops.ai/)
- 对象：“The root container for all activities in a single execution of your workflow” [✓](https://docs.agentops.ai/v2/concepts/spans.md)
- 对象：“Represents an autonomous entity with specialized capabilities” [✓](https://docs.agentops.ai/v2/concepts/spans.md)
- 对象：“An interaction with a language model” [✓](https://docs.agentops.ai/v2/concepts/spans.md)
- 对象：“All spans (operations, agents, tools, workflows) recorded during the trace” [✓](https://docs.agentops.ai/v2/concepts/traces.md)
- 关系：“most spans (other than the session itself) have a parent span that provides context” [✓](https://docs.agentops.ai/v2/concepts/spans.md)
- 属性与度量：“Total execution time (calculated automatically)” [✓](https://docs.agentops.ai/v2/concepts/traces.md)
- 属性与度量：“Success or error status” [✓](https://docs.agentops.ai/v2/concepts/spans.md)
- 属性与度量：“Track, save, and monitor every token your agent sees.” [✓](https://www.agentops.ai/)
- 属性与度量：“Manage and vizualize agent spend with up-to-date price monitoring.” [✓](https://www.agentops.ai/)
- 视图：“Here you will find a list of all of your previously recorded sessions and useful data about each such as total execution time.” [✓](https://docs.agentops.ai/v2/introduction)
- 编码：“On the left, a time visualization of all your LLM calls, Action events, Tool calls, and Errors.” [✓](https://docs.agentops.ai/v2/introduction)
- 交互：“Find any past sessions from your Session Drawer.” [✓](https://docs.agentops.ai/v2/introduction)
- 交互：“On the right, specific details about the event you’ve selected on the waterfall.” [✓](https://docs.agentops.ai/v2/introduction)
- 回答的问题：“AgentOps is the developer favorite platform for testing, debugging, and deploying AI agents and LLM apps.” [✓](https://docs.agentops.ai/v2/introduction)
- 回答的问题：“Track spending Across multiple agents.” [✓](https://www.agentops.ai/)
- 抽象与层级：“View a meta-analysis of all of your sessions in a single view.” [✓](https://docs.agentops.ai/v2/introduction)
- 抽象与层级：“A logical grouping of related operations” [✓](https://docs.agentops.ai/v2/concepts/spans.md)
- 抽象与层级：“Hierarchical structure of operations” [✓](https://docs.agentops.ai/v2/concepts/traces.md)

</details>
- 没读到：encodings 中的颜色、大小、线型（只有左右位置一句）

<a id="langwatch"></a>

### LangWatch

- 领域：AI 应用观测；议题：找出一次运行的瓶颈，并看全局的成本、延迟与话题分布
- 编码：层级与树 + 一般图与网络；重点：时间与演化、连通与邻域、群落与相似；把握：官方页面直接写了
- 说明：四种视图读的是同一次运行，各自强调不同部分：瀑布看时间，火焰看栈内占比，拓扑看连接，时序看消息顺序。
- 编码所依据的原文：
  - 视图：“Waterfall, flame graph, topology, and sequence diagram, whichever way you need to read a run.” [✓](https://langwatch.ai/)
  - 抽象与层级：“clustered by topic and subtopic automatically” [✓](https://langwatch.ai/)
  - 回答的问题：“See the full conversation flow, identify bottlenecks, and understand exactly how your AI applications behave in production.” [✓](https://langwatch.ai/docs/introduction.md)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Every LLM call, tool usage, and user interaction is automatically tracked with detailed traces, spans, and metadata.” [✓](https://langwatch.ai/docs/introduction.md)
- 处理的材料：“reads your traces, writes the tests, and opens the pull request” [✓](https://langwatch.ai/)
- 对象：“Trace every agent step and monitor cost and latency with full production visibility” [✓](https://langwatch.ai/)
- 对象：“Turn a production trace into a simulation and prove the fix.” [✓](https://langwatch.ai/)
- 对象：“Every conversation is clustered by topic and subtopic automatically, so you see what your users actually ask.” [✓](https://langwatch.ai/)
- 属性与度量：“monitor cost and latency with full production visibility” [✓](https://langwatch.ai/)
- 属性与度量：“Measure response quality and accuracy so you ship agents that hold up in production” [✓](https://langwatch.ai/)
- 属性与度量：“Full trace history and token spend for Claude Code, Codex, and every coding agent” [✓](https://langwatch.ai/)
- 属性与度量：“Build custom analytics graphs over any metric, cost, latency, scores, whatever you track.” [✓](https://langwatch.ai/)
- 视图：“Build custom analytics graphs over any metric” [✓](https://langwatch.ai/)
- 交互：“search in plain language, and filter smartly across millions of traces” [✓](https://langwatch.ai/)
- 交互：“Ask a question, get the matches back in minutes” [✓](https://langwatch.ai/)
- 交互：“Click into any trace to see exactly what went wrong” [✓](https://langwatch.ai/docs/observability/overview.md)
- 交互：“Turn a production trace into a simulation and prove the fix.” [✓](https://langwatch.ai/)
- 回答的问题：“Measure response quality and accuracy so you ship agents that hold up in production” [✓](https://langwatch.ai/)
- 抽象与层级：“whichever way you need to read a run” [✓](https://langwatch.ai/)
- 为什么这样画：“See it every way Waterfall, flame graph, topology, and sequence diagram, whichever way you need to read a run.” [✓](https://langwatch.ai/)
- 为什么这样画：“Every conversation is clustered by topic and subtopic automatically, so you see what your users actually ask.” [✓](https://langwatch.ai/)
- 为什么这样画：“Save the views your team lives in, search in plain language, and filter smartly across millions of traces.” [✓](https://langwatch.ai/)
- 原来的问题：“AI agents are still tested by hand, breaking in production.” [✓](https://langwatch.ai/)
- 原来的问题：“An agent can take a hundred paths to the same goal, testing them by hand catches only a few.” [✓](https://langwatch.ai/)

</details>
- 没读到：relations（只有 topology 视图名，未写边的含义）；encodings（未写颜色、位置、大小等含义）；app.langwatch.ai/demo 页面由 JS 渲染，没读到正文

<a id="nx"></a>

### Nx

- 领域：软件工程；议题：知道改动会影响哪些项目，决定任务的执行顺序
- 编码：有向无环图 + 层级与树；重点：先后与依赖方向、连通与邻域、包含与层次；把握：官方页面直接写了
- 说明：官方页面直接写：组合节点对“哪怕中等大小的图”也是必需的（“essential to navigate a graph of even a moderate size”）。
- 编码所依据的原文：
  - 抽象与层级：“Composite nodes are essential to navigate a graph of even a moderate size.” [✓](https://nx.dev/docs/features/explore-graph)
  - 交互：“Focus on a specific project and then use the proximity and group by folder controls in the sidebar to modify the graph around that project.” [✓](https://nx.dev/docs/features/explore-graph)
  - 回答的问题：“To share which other projects are directly affected by changes you are making” [✓](https://nx.dev/docs/features/explore-graph)
  - 关系：“Edges represent the dependencies between tasks.” [✓](https://nx.dev/docs/concepts/mental-model.md)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The project graph represents the source code in your repository and external dependencies such as Vite, React, and Angular.” [✓](https://nx.dev/docs/concepts/mental-model.md)
- 处理的材料：“Nx understands your workspace as a collection of projects.” [✓](https://nx.dev/docs/features/explore-graph)
- 对象：“Projects in Nx are the different parts of the monorepo which can have tasks run for them.” [✓](https://nx.dev/docs/features/explore-graph)
- 对象：“Each node is a task, which is a specific target invoked for a project, such as `myapp:build`.” [✓](https://nx.dev/docs/concepts/mental-model.md)
- 对象：“Composite nodes represent a set of projects in the same folder and can be expanded in place” [✓](https://nx.dev/docs/features/explore-graph)
- 关系：“Click on any dependency line to find which file(s) created the dependency.” [✓](https://nx.dev/docs/features/explore-graph)
- 关系：“Nx uses the project graph of your workspace to determine the order in which to run tasks” [✓](https://nx.dev/docs/features/explore-graph)
- 属性与度量：“Which executor was used to run the command” [✓](https://nx.dev/docs/features/explore-graph)
- 属性与度量：“This will give you all the information that is used to create the project graph visualization.” [✓](https://nx.dev/docs/features/explore-graph)
- 视图：“Project View: Project View Loading” [✓](https://nx.dev/docs/features/explore-graph)
- 视图：“This is a separate graph of tasks and their dependencies which is based on the project graph” [✓](https://nx.dev/docs/features/explore-graph)
- 视图：“This will open a browser window with an interactive view of the project graph of your workspace.” [✓](https://nx.dev/docs/features/explore-graph)
- 交互：“You can also "focus" a composite node to render a graph of just the projects inside that node.” [✓](https://nx.dev/docs/features/explore-graph)
- 交互：“Click on the nodes of this graph to see more information about the task” [✓](https://nx.dev/docs/features/explore-graph)
- 交互：“There is a floating action button in the bottom right of the project graph view which will save the graph as a .png file.” [✓](https://nx.dev/docs/features/explore-graph)
- 回答的问题：“When introducing new project(s) into the workspace” [✓](https://nx.dev/docs/features/explore-graph)
- 回答的问题：“Teach you to use this tool to explore projects, the project graph, and the task graphs for your workspace.” [✓](https://nx.dev/docs/features/explore-graph)
- 抽象与层级：“there are several ways to narrow the focus of the visualization down to the most useful part of the graph” [✓](https://nx.dev/docs/features/explore-graph)
- 抽象与层级：“can be expanded in place to show all the individual projects and their dependencies” [✓](https://nx.dev/docs/features/explore-graph)
- 为什么这样画：“Exploring this graph visually is vital to understanding how your code is structured and how Nx behaves.” [✓](https://nx.dev/docs/features/explore-graph)
- 为什么这样画：“Using this tool is vital to understanding both your workspace as well as how Nx behaves.” [✓](https://nx.dev/docs/features/explore-graph)
- 为什么这样画：“Composite nodes are essential to navigate a graph of even a moderate size.” [✓](https://nx.dev/docs/features/explore-graph)
- 为什么这样画：“Sharing this image with other developers is a great way to express how a project fits into the workspace.” [✓](https://nx.dev/docs/features/explore-graph)
- 原来的问题：“Viewing the entire graph can be unmanageable even for smaller repositories” [✓](https://nx.dev/docs/features/explore-graph)
- 原来的问题：“It always stays up to date without having to actively maintain a document as it is calculated by analyzing your source code.” [✓](https://nx.dev/docs/features/explore-graph)

</details>
- 没读到：encodings（颜色、大小、线型未写）

<a id="backstage"></a>

### Backstage

- 领域：软件工程；议题：看清软件目录里的对象各自由谁拥有、依赖谁、提供什么 API
- 编码：一般图与网络；重点：连通与邻域、关系上的类型与量；把握：官方页面直接写了
- 编码所依据的原文：
  - 交互：“KINDS - select what kinds of entities you want to view, default is all kinds” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
  - 交互：“RELATIONS - select which relationships you want to view, default is all relationships” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
  - 抽象与层级：“MAX DEPTH = infinite” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
  - 抽象与层级：“Simplified On = simple view Off = detailed view” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“we recommend that you name them catalog-info.yaml” [✓](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- 对象：“Each of the entities in the Catalog has various relationships to each other.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 对象：“the demo data includes an API that provides data to a website” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 对象：“Kind: Component” [✓](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- 对象：“Kind: System” [✓](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- 关系：“Each relationship is also designated, such as hasPart/partOf and apiProvidedBy/providesApi.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 关系：“guests is the owner of the API and the website” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 关系：“This section displays the selected entity and any other types of entities to which it is related.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 属性与度量：“Common to All Kinds: The Metadata” [✓](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- 属性与度量：“Common to All Kinds: Status” [✓](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- 视图：“This view allows you to filter what entities and relationships to display.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 视图：“Simplified On = simple view Off = detailed view” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 编码：“Direction - orientation in which you want to view the entity and its associated nodes” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 编码：“Curve = Monotone” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 交互：“The Catalog Graph automatically reflects any changes you make to the filter settings.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 交互：“Selecting any of the related entities allows you to drill down further through the system model.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 回答的问题：“Selecting any of the related entities allows you to drill down further through the system model.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 回答的问题：“guests is the owner of the API and the website” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 抽象与层级：“Off = You only see relations from the selected entity to its nodes.” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)
- 抽象与层级：“select what kinds of entities you want to view” [✓](https://backstage.io/docs/next/getting-started/viewing-entity-relationships/)

</details>
- 没读到：demo.backstage.io/catalog 页面由 JS 渲染，没读到正文

<a id="datahub"></a>

### DataHub

- 领域：数据工程；议题：排查数据问题的上游来源，改动前评估对下游的影响
- 编码：有向无环图；重点：先后与依赖方向、关系上的类型与量、时间与演化；把握：官方页面直接写了
- 编码所依据的原文：
  - 回答的问题：“Root cause analysis: debug data issues in minutes by tracing problems upstream” [✓](https://datahub.com/demos/data-lineage-with-datahub/)
  - 回答的问题：“Impact analysis to prevent breaking downstream dependencies before making changes” [✓](https://datahub.com/demos/data-lineage-with-datahub/)
  - 抽象与层级：“Column lineage can be visualized while viewing table-level lineage by expanding the columns of tables” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
  - 属性与度量：“The time picker can be used to filter out edges” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“SQL query parsing that automatically extracts transformation logic and column-level dependencies” [✓](https://datahub.com/demos/data-lineage-with-datahub/)
- 处理的材料：“Automated data lineage capture across databases, pipelines, transformations, AI systems, and BI tools” [✓](https://datahub.com/demos/data-lineage-with-datahub/)
- 对象：“entity is the primary node in the metadata graph” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 对象：“For example, an instance of a Dataset or a CorpUser is an Entity.” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 对象：“Ownership can be assigned to a dataset, a column, or other entities.” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 对象：“trace individual fields from source through transformations to final reports” [✓](https://datahub.com/demos/data-lineage-with-datahub/)
- 关系：“A relationship represents a named edge between 2 entities.” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 关系：“They are declared via foreign key attributes within Aspects along with a custom annotation (@Relationship).” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 关系：“to view the upstreams and downstreams of each task” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 属性与度量：“An aspect is a collection of attributes that describes a particular facet of an entity.” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 属性与度量：“Typically it is expressed as a Boolean value.” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 属性与度量：“Owner refers to the users or groups that have ownership rights over entities.” [✓](https://docs.datahub.com/docs/what-is-datahub/datahub-concepts)
- 视图：“Visual lineage explorer with filtering by time, owner, and platform” [✓](https://datahub.com/demos/data-lineage-with-datahub/)
- 视图：“in an Explorer visualization or the Impact Analysis tool” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 视图：“At its center will be the data pipeline node, represented as a box containing all of its composite tasks.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 编码：“represented as a box containing all of its composite tasks” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 编码：“The number on the expand lineage button represents how many data-dependence upstreams / downstreams the task has.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 交互：“After expanding, you can keep expanding lineage further like the standard lineage explorer.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 交互：“click and drag the data pipeline box itself” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 交互：“you can visualize lineage focused on a single column by clicking on the breadcrumb on a column” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 交互：“Data experts are free to add or remove upstream and downstream lineage edges” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 回答的问题：“Perform lineage impact analysis” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 抽象与层级：“Column-level lineage tracks changes and movements for each specific data column.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 抽象与层级：“This approach is often contrasted with table-level lineage, which specifies lineage at the table level.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 抽象与层级：“visualize lineage focused on a single column” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 为什么这样画：“Note that you can only expand one task's upstreams and one task's downstreams at a time, to keep the visualization simple.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 原来的问题：“If there is column-level lineage to hidden assets or the table-level view is getting too busy, you can visualize lineage focused on a single column by clicking on the breadcrumb on a column” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 局限与代价：“Selecting time windows in the patch will not show you historical lineages. It will only filter the view of the latest version of the lineage.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)
- 局限与代价：“Note that you can only expand one task's upstreams and one task's downstreams at a time, to keep the visualization simple.” [✓](https://docs.datahub.com/docs/features/feature-guides/lineage)

</details>
- 没读到：encodings（颜色、线型、大小未写，只写了方框和数字）；docs.datahub.com 首页由 JS 渲染，没读到正文

<a id="openmetadata"></a>

### OpenMetadata

- 领域：数据工程；议题：发现数据资产，并追踪数据怎么变换、在哪被使用
- 编码：有向无环图；重点：先后与依赖方向、关系上的类型与量、时间与演化；把握：官方页面直接写了
- 说明：“服务层、领域层、数据产品层”是在同一张血缘上换聚合口径——聚合方式本身是一个可选的维度。
- 编码所依据的原文：
  - 视图：“The Lineage page has two tabs at the top: Lineage (the graph you’ve seen so far) and Impact Analysis” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
  - 抽象与层级：“Column Layer Observability Layer Service Layer Domain Layer Data Product Layer” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
  - 属性与度量：“limit the graph to edges observed within a specific time range” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
  - 交互：“Click an edge to see its details: the Source, Target, Description, and SQL Query.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Lineage first comes from the metadata ingested from the databases.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 处理的材料：“Dashboard ingestion then adds the data models and charts, linking them back to the database tables they’re built on.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 对象：“search across tables, topics, dashboards, pipelines, ML models, containers, glossaries, and tags” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-discovery)
- 对象：“The table on the left is the parent, or Source node.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 对象：“The table on the right is the Target node” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 对象：“The arrow connecting them is the Edge” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 关系：“Each node expands to show its upstream and downstream edges.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 关系：“links the pipeline to the database tables it reads from and writes to” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 关系：“linking them back to the database tables they’re built on” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 属性与度量：“Each edge carries details such as the SQL query, pipeline information, and column-level lineage.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 属性与度量：“viewing the data evolution tracked using lineage and metadata versioning” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-discovery)
- 视图：“a table that lists the same upstream and downstream assets as rows instead of nodes on a graph” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 视图：“Explore lineage diagrams interactively to understand how data flows between sources, transformations, and dashboards.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 编码：“The table on the left is the parent, or Source node. The table on the right is the Target node” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 编码：“identifiable by the arrow pointing into it” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 交互：“Search for a data asset and expand the graph to see its lineage” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 交互：“use the calendar control (labeled All time by default)” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 交互：“Edit the table and column level lineage manually.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage)
- 回答的问题：“View column-level lineage to trace transformations and dependencies for data quality, debugging, and impact analysis.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/column)
- 回答的问题：“Users can visualize how data is transformed and where it is used” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage)
- 回答的问题：“Discover the right data assets quickly.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-discovery)
- 回答的问题：“Explore data discovery, lineage, and governance features hands-on.” [✓](https://docs.open-metadata.org/v2.0.x/quick-start/sandbox)
- 抽象与层级：“Each node expands to show its upstream and downstream edges.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 抽象与层级：“expand its list of columns and see column-level lineage” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 抽象与层级：“Lineage view supports multiple exploration layers that provide deeper insights into the structure, flow, and quality of data” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 为什么这样画：“a table that lists the same upstream and downstream assets as rows instead of nodes on a graph, which is easier to scan, search, and sort when an asset has a large number of dependencies.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 为什么这样画：“If a layer has more nodes than this, the rest are paginated instead of all being rendered at once.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 为什么这样画：“This is useful for seeing what an asset’s dependencies looked like as of a past date, or for narrowing a large graph down to recent activity.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 为什么这样画：“These layers help you visualize lineage not just at the dataset level, but also across services, domains, and business-critical data products.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 局限与代价：“If an edge falls outside the selected window, the graph excludes every asset reachable only through that edge, even if later edges fall inside the window.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)
- 局限与代价：“A window over a mix of legacy and timestamped edges returns all legacy edges plus whichever timestamped ones fall inside the window, not a clean point-in-time snapshot.” [✓](https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore)

</details>
- 没读到：没读到：https://sandbox.open-metadata.org/ 为 JS 渲染，只读到标题“OpenMetadata”，正文未读到。

<a id="skywalking"></a>

### Apache SkyWalking

- 领域：分布式系统运维；议题：从拓扑进入追踪、指标、日志，弄清运行系统的状况
- 编码：一般图与网络 + 层级与树、空间与几何；重点：连通与邻域、对象上的度量、包含与层次；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 视图：“The GENERAL layer enables the full set of sub-tabs: Service, Instance, Endpoint, API dependency, Topology, Traces, Logs” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
  - 编码：“an SLA health ring ( service_sla/100 , colored green / amber / red” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
  - 交互：“Follow dependencies, rotate the 3D scene, and select a node to inspect it.” [✓](https://skywalking.apache.org/)
  - 抽象与层级：“The primary drill-down for one selected service.” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“configure SkyWalking to analyze the topology and metrics from their access logs.” [✓](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/)
- 处理的材料：“Only support deployment with SkyWalking agents installed, currently Java agent and Python agent support trace profiling.” [✓](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/)
- 对象：“Services & APIs Kubernetes & Service Mesh Infrastructure & eBPF” [✓](https://skywalking.apache.org/)
- 对象：“endpoints as API — the endpoint-to-endpoint view is called API dependency” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
- 对象：“Start microservices WITHOUT SkyWalking agent enabled” [✓](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/)
- 对象：“Explore services and Kubernetes infrastructure together.” [✓](https://skywalking.apache.org/)
- 关系：“Service relationships” [✓](https://skywalking.apache.org/)
- 关系：“Follow dependencies, rotate the 3D scene, and select a node to inspect it.” [✓](https://skywalking.apache.org/)
- 关系：“Follow a request across your services” [✓](https://skywalking.apache.org/)
- 属性与度量：“Top 10 slowest instances — instances ranked by average response time” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
- 属性与度量：“every service node is decorated with RPM” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
- 属性与度量：“Connect service performance, model usage, and agent activity in one platform.” [✓](https://skywalking.apache.org/)
- 属性与度量：“Compare daily and hourly token usage across your agents.” [✓](https://skywalking.apache.org/)
- 视图：“Explore the 3D map” [✓](https://skywalking.apache.org/)
- 视图：“Infrastructure topology” [✓](https://skywalking.apache.org/)
- 视图：“Deploy a Grafana to show SkyWalking metrics and logs on the Grafana UI.” [✓](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/)
- 交互：“Interactive exploration” [✓](https://skywalking.apache.org/)
- 交互：“Filter collected conversations by runtime, time range, or title.” [✓](https://skywalking.apache.org/)
- 交互：“with tabs to re-rank by Traffic” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
- 回答的问题：“Understand your running systems.” [✓](https://skywalking.apache.org/)
- 回答的问题：“Bring topology, traces, metrics, logs, profiles, and alerts into every investigation.” [✓](https://skywalking.apache.org/)
- 回答的问题：“See how your services connect” [✓](https://skywalking.apache.org/)
- 抽象与层级：“the 3D Infrastructure Map for the cross-layer view” [✓](https://skywalking.apache.org/docs/skywalking-horizon-ui/next/dashboards/general/)
- 抽象与层级：“feed the AI_AGENT layer from its scenario feed” [✓](https://skywalking.apache.org/docs/skywalking-showcase/next/readme/)
- 抽象与层级：“Explore services and Kubernetes infrastructure together.” [✓](https://skywalking.apache.org/)

</details>
- 没读到：没读到：https://skywalking.apache.org/3d-map-app/ 为 JS 渲染，只读到标题“SkyWalking 3D Infrastructure Map — interactive demo”，正文未读到。；没读到：https://demo.skywalking.apache.org/ 为 JS 渲染，只读到标题“SkyWalking Horizon UI”，正文未读到。

<a id="kiali"></a>

### Kiali

- 领域：服务网格运维；议题：看服务网格里的流量，快速发现 mTLS、延迟、错误问题
- 编码：一般图与网络；重点：连通与邻域、关系上的类型与量、对象上的度量、时间与演化；把握：官方页面直接写了
- 说明：同一批流量，用不同的聚合粒度画四次（服务、应用、带版本的应用、工作负载）——粒度切换是产品的一等功能。
- 编码所依据的原文：
  - 抽象与层级：“The service graph provides a high-level view, which aggregates all traffic for defined services.” [✓](https://kiali.io/docs/features/topology/)
  - 抽象与层级：“The versioned app graph aggregates by app, but breaks out the different versions” [✓](https://kiali.io/docs/features/topology/)
  - 编码：“Colors in the graph represent the health of your service mesh.” [✓](https://kiali.io/docs/features/topology/)
  - 编码：“The node shape indicates the type of component such as services, workloads, or apps.” [✓](https://kiali.io/docs/features/topology/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The topology combines real-time request traffic with your Istio configuration information” [✓](https://kiali.io/docs/features/topology/)
- 处理的材料：“shows only the traffic reported by that node’s Istio proxy” [✓](https://kiali.io/docs/features/topology/)
- 对象：“The node shape indicates the type of component such as services, workloads, or apps.” [✓](https://kiali.io/docs/features/topology/)
- 对象：“From here users can perform namespace-level Actions, or quickly navigate to more detailed views.” [✓](https://kiali.io/docs/features/topology/)
- 对象：“an Operation node also provides a side-panel view” [✓](https://kiali.io/docs/features/topology/)
- 关系：“The workload graph provides the a detailed view of communication between workloads.” [✓](https://kiali.io/docs/features/topology/)
- 关系：“The color of an edge between components represents the health of the requests between those components.” [✓](https://kiali.io/docs/features/topology/)
- 属性与度量：“Charts showing traffic and response times.” [✓](https://kiali.io/docs/features/topology/)
- 属性与度量：“Response Code and Host breakdowns.” [✓](https://kiali.io/docs/features/topology/)
- 属性与度量：“The health of nodes and edges is refreshed automatically based on the user’s preference.” [✓](https://kiali.io/docs/features/topology/)
- 视图：“Kiali offers four different traffic-graph renderings” [✓](https://kiali.io/docs/features/topology/)
- 视图：“A double-click drills in to show the node’s Detail Graph” [✓](https://kiali.io/docs/features/topology/)
- 视图：“The collapsible side-panel summarizes the current graph selection, or the graph as a whole.” [✓](https://kiali.io/docs/features/topology/)
- 视图：“Graph replay allows you to replay traffic from a selected past time-period.” [✓](https://kiali.io/docs/features/topology/)
- 编码：“The health of Nodes and Edges is represented via a standard color system using shades of orange and red” [✓](https://kiali.io/docs/features/health/)
- 编码：“The color of an edge between components represents the health of the requests between those components.” [✓](https://kiali.io/docs/features/topology/)
- 交互：“A single-click will select the node, edge, or box of interest.” [✓](https://kiali.io/docs/features/topology/)
- 交互：“A double-click drills in to show the node’s Detail Graph” [✓](https://kiali.io/docs/features/topology/)
- 交互：“The graph can also be paused to examine a particular state, or replayed to re-examine a particular time period.” [✓](https://kiali.io/docs/features/topology/)
- 交互：“Combined with the find/hide feature, this allows you to quickly highlight or filter for important workloads, services, and applications.” [✓](https://kiali.io/docs/features/topology/)
- 回答的问题：“allowing you to quickly pinpoint issues” [✓](https://kiali.io/docs/features/topology/)
- 回答的问题：“It can identify mTLS issues, latency issues, error traffic and more.” [✓](https://kiali.io/docs/features/topology/)
- 回答的问题：“visualize traffic as a high-level service topology, a low-level workload topology, or as an application-level topology” [✓](https://kiali.io/docs/features/topology/)
- 抽象与层级：“A double-click drills in to show the node’s Detail Graph” [✓](https://kiali.io/docs/features/topology/)
- 抽象与层级：“or quickly navigate to more detailed views” [✓](https://kiali.io/docs/features/topology/)
- 为什么这样画：“Each combines several information types to help users quickly evaluate the health of their service architecture.” [✓](https://kiali.io/docs/features/topology/)
- 为什么这样画：“The topology combines real-time request traffic with your Istio configuration information to present immediate insight into the behavior of service mesh” [✓](https://kiali.io/docs/features/topology/)
- 为什么这样画：“Multiple Graph Types allow you to visualize traffic as a high-level service topology, a low-level workload topology, or as an application-level topology.” [✓](https://kiali.io/docs/features/topology/)
- 为什么这样画：“Combined with the find/hide feature, this allows you to quickly highlight or filter for important workloads, services, and applications.” [✓](https://kiali.io/docs/features/topology/)
- 局限与代价：“Because operation nodes represent aggregate traffic they are not compatible with Service graphs, which themselves are already logical aggregates.” [✓](https://kiali.io/docs/features/topology/)
- 局限与代价：“For similar reasons response time information is not available on edges leading into or out of operation nodes.” [✓](https://kiali.io/docs/features/topology/)
- 局限与代价：“The node detail graph visualizes traffic from the point-of-view of that node, meaning it shows only the traffic reported by that node’s Istio proxy.” [✓](https://kiali.io/docs/features/topology/)

</details>

<a id="grafana"></a>

### Grafana

- 领域：基础设施运维；议题：把查询结果画成面板，其中节点图用来看相互关联的元素
- 编码：表与多维属性 + 一般图与网络；重点：对象上的度量、连通与邻域；把握：证据很少
- 编码所依据的原文：
  - 视图：“Flame graph Gauge Geomap Heatmap Histogram Logs News Node graph Pie chart Stat State timeline Status history Table Text Traces Trend XY chart” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
  - 视图：“Node graphs are useful when you need to visualize elements that are related to each other.” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
  - 处理的材料：“composed of a query and a visualization, a graphical representation of query results” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Learn about working with traces and tracing data in Explore.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 处理的材料：“Learn about working with logs and log data in Explore.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 对象：“Panels are the basic building block in Grafana dashboards” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/)
- 对象：“displaying circles—or nodes —for each element you want to visualize” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 关系：“connected by lines—or edges” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 关系：“Node graphs display useful information about each node, as well as the relationships between them” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 关系：“Learn how to create and use Correlations.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 属性与度量：“Node graphs display useful information about each node” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 视图：“Learn about working with logs and log data in Explore.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 编码：“displaying circles—or nodes —for each element you want to visualize” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 编码：“By default, the visualization uses a layered layout that positions the nodes into a network of connected circles.” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 交互：“Learn how to manage queries in Explore.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 交互：“Learn how to use the Query inspector to troubleshoot issues with your queries.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 回答的问题：“Use Explore to query, collect, and analyze data for detailed real-time data analysis.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 回答的问题：“collect, correlate, and visualize data so you can make informed decisions in real time” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/)
- 回答的问题：“allowing you to visualize complex infrastructure maps” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)
- 抽象与层级：“Explore is your starting point for querying, analyzing, and aggregating data in Grafana.” [✓](https://grafana.com/docs/grafana/latest/visualizations/explore/)
- 抽象与层级：“composed of a query and a visualization, a graphical representation of query results” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/)
- 抽象与层级：“uses a layered layout that positions the nodes into a network of connected circles” [✓](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/)

</details>
- 没读到：没读到：https://play.grafana.org/ 为 JS 渲染，只读到“Grafana is starting up... Error loading Grafana”，正文未读到；官方页面列表中只给了这一个链接，因此改读文档页。

<a id="affine"></a>

### AFFiNE

- 领域：知识管理；议题：同一批内容既要线性地写，又要空间化地摆
- 编码：层级与树 + 空间与几何；重点：跨视图的同一对象；把握：官方页面直接写了
- 编码所依据的原文：
  - 关系：“the same blocks work in both modes, so written notes can become visual plans without copying content” [✓](https://affine.pro/pagedoc)
  - 抽象与层级：“From Freeform Canvas to Structured Pages” [✓](https://affine.pro/whiteboard)
  - 交互：“Every doc can switch to the edgeless whiteboard in one click” [✓](https://affine.pro/pagedoc)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“AFFiNE is a workspace with fully merged docs, whiteboards and databases.” [✓](https://affine.pro/)
- 处理的材料：“Multiple Document Formats Supported” [✓](https://affine.pro/whiteboard)
- 对象：“Build Rich, Interactive Documents Blocks Quote Resources PDF Preview Table Image & Videos” [✓](https://affine.pro/pagedoc)
- 对象：“customize its pages, databases, and Edgeless whiteboards” [✓](https://affine.pro/templates)
- 对象：“Collaborate on Multiple Docs in a Single Canvas” [✓](https://affine.pro/whiteboard)
- 关系：“Transform Docs into a Seamless Canvas in just one click.” [✓](https://affine.pro/whiteboard)
- 属性与度量：“Visualize deadlines, manage homework, and boost productivity” [✓](https://affine.pro/templates)
- 视图：“Sketch, write, and brainstorm freely with no boundaries.” [✓](https://affine.pro/whiteboard)
- 视图：“Browse templates for Cornell notes, digital planners, Kanban boards” [✓](https://affine.pro/templates)
- 视图：“Class Diagram Object Diagram Component Diagram Deployment Diagram Package Diagram” [✓](https://affine.pro/templates)
- 视图：“Visual & Mind Map Study Planner” [✓](https://affine.pro/templates)
- 交互：“Flexible convert from pages to canvas” [✓](https://affine.pro/whiteboard)
- 交互：“Preview any layout, duplicate it into your workspace, and customize its pages, databases, and Edgeless whiteboards without starting from scratch.” [✓](https://affine.pro/templates)
- 交互：“Transform Docs into a Seamless Canvas in just one click.” [✓](https://affine.pro/whiteboard)
- 回答的问题：“Write, Draw, Plan, All at Once. With AI.” [✓](https://affine.pro/)
- 回答的问题：“Sketch, write, and brainstorm freely with no boundaries.” [✓](https://affine.pro/whiteboard)
- 回答的问题：“Visualize deadlines, manage homework, and boost productivity” [✓](https://affine.pro/templates)
- 抽象与层级：“Collaborative Docs for Notes and Structured Writing” [✓](https://affine.pro/pagedoc)
- 抽象与层级：“Transform lengthy content into concise, impactful summaries” [✓](https://affine.pro/templates)
- 抽象与层级：“Collaborate on Multiple Docs in a Single Canvas” [✓](https://affine.pro/whiteboard)

</details>
- 没读到：encodings

<a id="drawio"></a>

### diagrams.net / draw.io

- 领域：通用绘图；议题：快速画出任意类型的图
- 编码：一般图与网络；重点：连通与邻域；把握：页面信息支持，归类靠推断
- 说明：这是“结构由作者给，工具不管”的一端：没有数据模型，因此也没有按结构做的聚合和过滤。
- 编码所依据的原文：
  - 视图：“Mindmaps and concept maps” [✓](https://www.drawio.com/docs/diagram-types/)
  - 视图：“Dependency graphs” [✓](https://www.drawio.com/docs/diagram-types/)
  - 抽象与层级：“Organise your diagram with layers and tags” [✓](https://www.drawio.com/docs/features/)
  - 交互：“Let auto-layouts format flowcharts and tree diagrams for you.” [✓](https://www.drawio.com/docs/features/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“An org chart, generated from CSV and formatting data” [✓](https://www.drawio.com/docs/diagram-types/)
- 对象：“Search for shapes, including in open-source icon libraries.” [✓](https://www.drawio.com/docs/features/)
- 对象：“Create your own custom shapes and custom shape libraries” [✓](https://www.drawio.com/docs/features/)
- 关系：“Style shapes and connectors with customisable palettes” [✓](https://www.drawio.com/docs/features/)
- 属性与度量：“Set shape properties” [✓](https://www.drawio.com/docs/features/)
- 属性与度量：“metadata and placeholders to add translations” [✓](https://www.drawio.com/docs/features/)
- 视图：“Use the infinite canvas, rulers, customisable grid and positioning guidelines to help you diagram faster.” [✓](https://www.drawio.com/docs/features/)
- 视图：“Tree diagrams and org charts” [✓](https://www.drawio.com/docs/diagram-types/)
- 交互：“Search for shapes, including in open-source icon libraries.” [✓](https://www.drawio.com/docs/features/)
- 交互：“Sketch and comment with freehand shapes” [✓](https://www.drawio.com/docs/features/)
- 回答的问题：“help you diagram faster” [✓](https://www.drawio.com/docs/features/)

</details>
- 没读到：encodings

<a id="kumu"></a>

### Kumu

- 领域：系统与关系分析；议题：把复杂的关系整理成地图，找出关键人物与关系
- 编码：一般图与网络；重点：连通与邻域、关系上的类型与量、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“Different views can also be layered on top of one another via the @import syntax” [✓](https://docs.kumu.io/guides/partial-views)
  - 交互：“Show everyone within three degrees of a given person using focus” [✓](https://kumu.io/tour)
  - 编码：“Size elements based on the number of incoming or outgoing connections” [✓](https://kumu.io/tour)
  - 编码：“Use a color scale to highlight relative strengths” [✓](https://kumu.io/tour)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Import a local spreadsheet or use our Google Sheets integration to build maps from live data” [✓](https://kumu.io/tour)
- 处理的材料：“Already have existing data? Our simple import format makes it easy to create a map from a spreadsheet.” [✓](https://kumu.io/tour)
- 处理的材料：“Kumu makes it easy to organize complex data into relationship maps” [✓](https://kumu.io/)
- 对象：“How do I add more than one element with the same label?” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 对象：“How do I edit virtual elements?” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 关系：“How do I add arrows to my connections?” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 关系：“How do I connect a connection to another connection? (split or branching connections)” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 属性与度量：“How do I change the length or strength of connections?” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 属性与度量：“Hide all connections except those where strength is "high" using filters” [✓](https://kumu.io/tour)
- 属性与度量：“How do I change the default for currency fields?” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 视图：“A view is a collection of decorations, filters, and other settings that change what is visible on your map and how it is styled.” [✓](https://docs.kumu.io/guides/views)
- 视图：“Understand and engage complex systems more effectively using systems maps and causal loop diagrams.” [✓](https://kumu.io/)
- 视图：“Concept maps that organize your understanding of how individual ideas relate to the bigger picture” [✓](https://kumu.io/tour)
- 视图：“Capture the structure of personal networks and reveal key players.” [✓](https://kumu.io/)
- 交互：“Cut through the clutter using filter, focus and showcase.” [✓](https://kumu.io/tour)
- 交互：“Highlight key people and fade the rest of map into the background using showcase” [✓](https://kumu.io/tour)
- 交互：“Switch between views using the navigation at the top of your map.” [✓](https://docs.kumu.io/guides/views)
- 回答的问题：“Reduce complex relationships into compelling visualizations, fast.” [✓](https://kumu.io/tour)
- 回答的问题：“Join the thousands of people using Kumu to find clarity within complex relationships.” [✓](https://kumu.io/tour)
- 回答的问题：“Make sense of your messy world.” [✓](https://kumu.io/)
- 抽象与层级：“Organize your project into multiple maps and views to capture different perspectives.” [✓](https://kumu.io/tour)
- 抽象与层级：“How do I collapse duplicate connections?” [✓](https://docs.kumu.io/overview/kumus-architecture)
- 抽象与层级：“Create before and after views of the same map” [✓](https://kumu.io/tour)
- 为什么这样画：“Reduce complex relationships into compelling visualizations, fast.” [✓](https://kumu.io/tour)
- 为什么这样画：“Cut through the clutter using filter, focus and showcase.” [✓](https://kumu.io/tour)
- 为什么这样画：“Organize your project into multiple maps and views to capture different perspectives.” [✓](https://kumu.io/tour)
- 为什么这样画：“More than a pretty picture, a visual database.” [✓](https://kumu.io/tour)
- 局限与代价：“The possibilities are endless, but don't go too crazy... nobody wants to look at an ugly map!” [✓](https://kumu.io/tour)

</details>
- 没读到：说明：演示页 https://kumu.io/tanyabeer/hewlett-foundation-madison-initiative 由 JS 渲染，只读到标题，未引用

<a id="infranodus"></a>

### InfraNodus

- 领域：文本分析与知识发现；议题：在一大段文字里找出主要话题群和它们之间的结构空白
- 编码：一般图与网络；重点：群落与相似、连通与邻域、对象上的度量；把握：官方页面直接写了
- 说明：重点不只是“连了什么”，还有“没连什么”：结构空白（structural gaps）是主要产出。
- 编码所依据的原文：
  - 对象：“the concepts (or entities) are the nodes, and their co-occurrences are the connections.” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
  - 编码：“Nodes are sized by betweenness centrality” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
  - 编码：“the most influential concepts (bigger nodes), the topical clusters (colors)” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
  - 回答的问题：“Reveal the most important topical clusters and gaps between them using a text network.” [✓](https://infranodus.com/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Analyze your notes, ideas, PDFs, CSVs, Google search results, surveys, tweets, spreadsheets.” [✓](https://infranodus.com/)
- 处理的材料：“paste any text (about 100 words is enough to see structure)” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 处理的材料：“Use #hashtags or [[wiki-links]] to create your nodes as your write” [✓](https://infranodus.com/graphs)
- 对象：“The words (or lemmas) are the nodes” [✓](https://infranodus.com/use-case/text-network-analysis)
- 关系：“their co-occurrences are the relations between them” [✓](https://infranodus.com/use-case/text-network-analysis)
- 关系：“adjacent words get the strongest link, words further apart a weaker one” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 属性与度量：“Use advanced network science metrics, such as betweenness centrality and modularity” [✓](https://infranodus.com/use-case/text-network-analysis)
- 属性与度量：“Calculate and export advanced statistical data on your text and every statement.” [✓](https://infranodus.com/use-case/text-network-analysis)
- 属性与度量：“Range the nodes by their influence using betweenness centrality.” [✓](https://infranodus.com/use-case/text-network-analysis)
- 视图：“Text Network Graph Visualizations” [✓](https://infranodus.com/graphs)
- 视图：“Mind maps and concept maps made using InfraNodus.” [✓](https://infranodus.com/graphs)
- 视图：“laid out with Force-Atlas so related ideas sit close together” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 视图：“1 Topics View 2 Concepts View” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 交互：“create the graph manually with a plain text editor” [✓](https://infranodus.com/use-case/text-network-analysis)
- 交互：“You can use the powerful filters to perform sentiment analysis” [✓](https://infranodus.com/)
- 交互：“Use the network representation to find the structural gaps in your discourse.” [✓](https://infranodus.com/use-case/text-network-analysis)
- 回答的问题：“Generate better insights and steer your LLM's reasoning.” [✓](https://infranodus.com/)
- 回答的问题：“Then apply the built-in AI to generate research questions to bridge those gaps.” [✓](https://infranodus.com/use-case/text-network-analysis)
- 抽象与层级：“A community detection algorithm groups the nodes into topical clusters” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 抽象与层级：“Apply force-layout and modularity algorithms to detect topic clusters and tag your text statements.” [✓](https://infranodus.com/use-case/text-network-analysis)
- 为什么这样画：“adjacent words get the strongest link, words further apart a weaker one. This mimics how short-term memory holds context.” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 为什么这样画：“Nodes are sized by betweenness centrality — how important a word is for connecting different parts of the discourse.” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 为什么这样画：“A community detection algorithm groups the nodes into topical clusters, shown as colors, laid out with Force-Atlas so related ideas sit close together.” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 为什么这样画：“Represented this way, you can then align the words / nodes that tend to co-occur together as clusters in a 2D plane” [✓](https://infranodus.com/use-case/text-network-analysis)
- 原来的问题：“The result is not a word cloud: it is a map of relations.” [✓](https://infranodus.com/tutorial/create-your-first-knowledge-graph)
- 原来的问题：“The topics identified using this approach are much more precise than LDA-based methods.” [✓](https://infranodus.com/use-case/text-network-analysis)

</details>

<a id="cncf-landscape"></a>

### CNCF Landscape

- 领域：技术生态；议题：在云原生生态里找到某类项目，并查看具体项目的信息
- 编码：集合与分类；重点：有什么、对象上的度量；把握：页面信息支持，归类靠推断
- 说明：景观图表达的是“哪类里有谁”，不表达项目之间的依赖——这是它的重点，也是它的盲区。
- 编码所依据的原文：
  - 抽象与层级：“A comprehensive categorical overview of projects and product offerings in the cloud native space” [✓](https://www.cncf.io/blog/2018/11/05/beginners-guide-cncf-landscape/)
  - 交互：“allows viewers to filter, obtain detailed information on a specific project or technology, and easily share via stateful URLs” [✓](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“all data is available in a GitHub” [✓](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)
- 对象：“Its myriad of open source projects are supported by the constant contributions of a vibrant and expansive community” [✓](https://www.cncf.io/blog/2018/11/05/beginners-guide-cncf-landscape/)
- 对象：“obtain detailed information on a specific project or technology” [✓](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)
- 回答的问题：“obtain detailed information on a specific project or technology” [✓](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)
- 抽象与层级：“in an attempt to categorize most of the projects and product offerings in the cloud native space” [✓](https://www.cncf.io/blog/2018/03/08/introducing-the-cloud-native-landscape-2-0-interactive-edition/)

</details>
- 没读到：relations；attributes；views；encodings；说明：landscape.cncf.io 由 JS 渲染，只读到标题；landscapeapp.cncf.io/ospo/guide 证书校验失败，未绕过，记为没读到；2.0 博客的 GitHub 数据句只读到前半句

<a id="thoughtworks-tech-radar"></a>

### Thoughtworks Technology Radar

- 领域：技术生态；议题：判断每项技术或做法现在是否推荐采用
- 编码：集合与分类；重点：对象上的度量、时间与演化；把握：官方页面直接写了
- 编码所依据的原文：
  - 编码：“The rings indicate our recommendation for using that technology or technique.” [✓](https://www.thoughtworks.com/radar/faq)
  - 编码：“The quadrants represent different kinds of blips.” [✓](https://www.thoughtworks.com/radar/faq)
  - 属性与度量：“Blips may be new to the latest Radar volume, or they can move rings as our recommendation has changed.” [✓](https://www.thoughtworks.com/radar)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“This knowledge-sharing tool is based on our global teams’ experience and highlights things you may want to explore on your projects.” [✓](https://www.thoughtworks.com/radar)
- 处理的材料：“Map out your ‘blips’ on a Google Sheet” [✓](https://www.thoughtworks.com/radar/byor)
- 对象：“A blip is a technology or technique that plays a role in software development.” [✓](https://www.thoughtworks.com/radar/faq)
- 对象：“These include elements of a software development process” [✓](https://www.thoughtworks.com/radar/faq)
- 对象：“Platforms, Tools, Languages & Frameworks” [✓](https://www.thoughtworks.com/radar/byor)
- 属性与度量：“Enter your content under each column (name, ring, quadrant, isNew, description).” [✓](https://www.thoughtworks.com/radar/byor)
- 属性与度量：“New Moved in/out No change” [✓](https://www.thoughtworks.com/radar)
- 视图：“Explore the interactive version by quadrant, or download the PDF to read the Radar in full.” [✓](https://www.thoughtworks.com/radar)
- 视图：“Use our radar visualization tool to create a shareable version.” [✓](https://www.thoughtworks.com/radar/byor)
- 编码：“Our Radar has four rings” [✓](https://www.thoughtworks.com/radar/faq)
- 编码：“usually indicating our increasing confidence in recommending them as they move through the rings” [✓](https://www.thoughtworks.com/radar/faq)
- 交互：“Explore the interactive version by quadrant” [✓](https://www.thoughtworks.com/radar)
- 交互：“input field and click "Build my radar".” [✓](https://www.thoughtworks.com/radar/byor)
- 回答的问题：“What counts as a blip?” [✓](https://www.thoughtworks.com/radar/faq)
- 回答的问题：“What are the quadrants?” [✓](https://www.thoughtworks.com/radar/faq)
- 回答的问题：“What are the rings?” [✓](https://www.thoughtworks.com/radar/faq)
- 回答的问题：“highlights things you may want to explore on your projects” [✓](https://www.thoughtworks.com/radar)
- 抽象与层级：“We organize blips using two categorizing elements: the quadrants and the rings.” [✓](https://www.thoughtworks.com/radar/faq)
- 抽象与层级：“a way to break up the Radar into topic areas” [✓](https://www.thoughtworks.com/radar/faq)
- 抽象与层级：“The Adopt ring represents blips that we think you should seriously consider” [✓](https://www.thoughtworks.com/radar/faq)

</details>
- 没读到：relations

<a id="zalando-tech-radar"></a>

### Zalando Tech Radar

- 领域：技术生态；议题：帮工程团队为新项目选技术，并跟踪技术决策的演变
- 编码：集合与分类；重点：对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 处理的材料：“The Zalando Tech Radar is a list of technologies, complemented by an assessment result, called ring assignment” [✓](https://opensource.zalando.com/tech-radar/)
  - 回答的问题：“The Tech Radar is a tool to inspire and support Engineering teams at Zalando to pick the best technologies for new projects” [✓](https://opensource.zalando.com/tech-radar/)
<details><summary>本案例读到的其他原文摘录</summary>

- 对象：“ADOPT — Technologies we have high confidence in to serve our purpose, also in large scale.” [✓](https://opensource.zalando.com/tech-radar/)
- 对象：“HOLD — Technologies not recommended to be used for new projects.” [✓](https://opensource.zalando.com/tech-radar/)
- 属性与度量：“complemented by an assessment result, called ring assignment” [✓](https://opensource.zalando.com/tech-radar/)
- 属性与度量：“We use four rings with the following semantics” [✓](https://opensource.zalando.com/tech-radar/)
- 回答的问题：“to reflect on technology decisions and continuously evolve our technology landscape” [✓](https://opensource.zalando.com/tech-radar/)

</details>
- 没读到：views；encodings；relations；interactions；abstraction

<a id="build-your-own-radar"></a>

### Build Your Own Radar

- 领域：技术生态；议题：从一张表生成自己的技术雷达
- 编码：表与多维属性 + 集合与分类；重点：对象上的度量；把握：官方页面直接写了
- 说明：表的列名承担了“角色”：ring 决定半径，quadrant 决定扇区——视图对数据的要求就是列要有这些角色。
- 编码所依据的原文：
  - 处理的材料：“You can use Google Sheets or CSV/JSON file links to create the radar.” [✓](https://www.thoughtworks.com/radar/byor)
  - 属性与度量：“Enter your content under each column (name, ring, quadrant, isNew, description).” [✓](https://www.thoughtworks.com/radar/byor)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Enter the URL of your Google Sheet, CSV or JSON file below” [✓](https://radar.thoughtworks.com/)
- 对象：“Map out your ‘blips’ on a Google Sheet” [✓](https://www.thoughtworks.com/radar/byor)
- 对象：“Quadrant names : Techniques, Platforms, Tools, Languages & Frameworks” [✓](https://www.thoughtworks.com/radar/byor)
- 对象：“Ring names : Adopt, Trial, Assess, Hold” [✓](https://www.thoughtworks.com/radar/byor)
- 视图：“you can use this service to generate an interactive version of your Technology Radar” [✓](https://radar.thoughtworks.com/)
- 视图：“Use our radar visualization tool to create a shareable version.” [✓](https://www.thoughtworks.com/radar/byor)
- 编码：“The official Thoughtworks Technology Radar has updated the name of the outermost ring from “Hold” to “Caution”.” [✓](https://radar.thoughtworks.com/)
- 交互：“Build my radar” [✓](https://www.thoughtworks.com/radar/byor)
- 回答的问题：“There are two steps to creating your own radar” [✓](https://www.thoughtworks.com/radar/byor)
- 回答的问题：“Once you've created your Radar you can use this service to generate an interactive version of your Technology Radar.” [✓](https://radar.thoughtworks.com/)

</details>
- 没读到：relations；abstraction

<a id="oss-insight"></a>

### OSS Insight

- 领域：开源生态；议题：了解 GitHub 上现在在发生什么，以及技术领域的排名与趋势
- 编码：表与多维属性 + 序列与事件流；重点：总体分布、时间与演化、有什么；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 处理的材料：“OSSInsight is a free analytics platform that tracks over 10 billion GitHub events in real time.” [✓](https://ossinsight.io/)
  - 抽象与层级：“grouped by technology domain” [✓](https://ossinsight.io/collections)
  - 回答的问题：“Insights about the monthly and historical rankings and trends in technical fields” [✓](https://ossinsight.io/)
<details><summary>本案例读到的其他原文摘录</summary>

- 对象：“It provides deep insights into open source repositories, developers, and organizations” [✓](https://ossinsight.io/)
- 对象：“Browse 102 + curated collections of GitHub repositories grouped by technology domain.” [✓](https://ossinsight.io/collections)
- 属性与度量：“including stars, commits, pull requests, issues, contributors, and community health metrics” [✓](https://ossinsight.io/)
- 属性与度量：“Star-based rankings are paused” [✓](https://ossinsight.io/)
- 属性与度量：“History before May 2025, repository totals synced directly from GitHub, and commit activity are unaffected.” [✓](https://ossinsight.io/)
- 视图：“Data Explorer Collections Trending Languages” [✓](https://ossinsight.io/)
- 视图：“Trending Repos” [✓](https://ossinsight.io/)
- 交互：“You can still browse repository analytics, Collections, and Trending pages.” [✓](https://ossinsight.io/explore)
- 交互：“Browse 102 + curated collections of GitHub repositories grouped by technology domain.” [✓](https://ossinsight.io/collections)
- 回答的问题：“What is happening on GitHub NOW” [✓](https://ossinsight.io/)
- 回答的问题：“How does OSSInsight analyze repositories?” [✓](https://ossinsight.io/)
- 回答的问题：“What data does OSSInsight use?” [✓](https://ossinsight.io/)
- 抽象与层级：“with curated repository lists” [✓](https://ossinsight.io/)

</details>
- 没读到：relations；encodings

<a id="oss-compass"></a>

### OSS Compass

- 领域：开源生态；议题：评估开源社区的健康状况
- 编码：表与多维属性；重点：对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 回答的问题：“Build a three-dimensional evaluation system to evaluate the health status of open source communities.” [✓](https://oss-compass.org/docs/service-guide/)
  - 属性与度量：“Community Vitality Collaboration Efficiency Open Governance” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“by analyzing global open source projects” [✓](https://oss-compass.org/)
- 处理的材料：“Understand developers' productivity, activity, and collaboration from their contribution behaviors.” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)
- 对象：“communities, technology fields, developers, programming languages, and licenses” [✓](https://oss-compass.org/)
- 对象：“to evaluate the health status of open source communities” [✓](https://oss-compass.org/docs/service-guide/)
- 对象：“provides precise developer capability assessment for open source project managers, enterprise technical teams, and researchers” [✓](https://oss-compass.org/docs/service-guide/)
- 关系：“global open source imports and exports” [✓](https://oss-compass.org/)
- 属性与度量：“including metrics models and metrics” [✓](https://oss-compass.org/)
- 属性与度量：“Developer Attraction Developer Growth Developer Retention” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)
- 属性与度量：“Understand developers' productivity, activity, and collaboration” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)
- 视图：“Repository Weekly Activity Board” [✓](https://oss-compass.org/)
- 视图：“Community Weekly Activity Board” [✓](https://oss-compass.org/)
- 交互：“Submit your project” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)
- 回答的问题：“Understand developers' productivity, activity, and collaboration from their contribution behaviors.” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)
- 回答的问题：“Gain insights into global open source imports and exports” [✓](https://oss-compass.org/)
- 抽象与层级：“leveraging a data-driven multi-dimensional modeling system” [✓](https://oss-compass.org/docs/service-guide/)
- 抽象与层级：“V3 Assessment System Community Ecosystem Health Assessment” [✓](https://oss-compass.org/docs/service-guide/ecosystem-evaluation/)

</details>
- 没读到：encodings；dimensions-define 与 os-situation 页面为 JS 渲染，正文未读到，未核对

<a id="pygraphistry"></a>

### PyGraphistry

- 领域：数据分析；议题：把任意表当作图来做可视分析（例如攻击者 IP 到受害者 IP）
- 编码：表与多维属性 + 一般图与网络；重点：连通与邻域、群落与相似、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 处理的材料：“Visually analyze any table as a graph” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
  - 对象：“Treat each row as a node, and link it to each cell value in it” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
  - 编码：“Node colors : Graphistry defaults to inferring the commmunity” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
  - 编码：“Node sizes : Graphistry defaults to the number of edges (“degree”)” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Graphistry works seamlessly with dataframes like Pandas and GPU RAPIDS cuDF” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 对象：“optional: node table, with matching node ID column” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 关系：“Simple graphs are: required: edge table, with src+dst ID columns” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 关系：“Link df ’s columns attackerIP -> victimIP” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 关系：“Link values from column entries” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 属性与度量：“optional additional property columns” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 属性与度量：“the number of edges (“degree”)” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 视图：“Ring - categorical Ring - continuous Ring - time Group in a box Modularity weighted Tree” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 回答的问题：“Visually analyze any table as a graph” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)
- 抽象与层级：“Group in a box Modularity weighted” [✓](https://pygraphistry.readthedocs.io/en/latest/demos/for_analysis.html)

</details>
- 没读到：interactions

<a id="embedding-projector"></a>

### Embedding Projector

- 领域：机器学习；议题：检查相近的点是否在语义上真的相关，并在高维空间里找有意义的方向
- 编码：空间与几何；重点：群落与相似、空间位置；把握：官方页面直接写了
- 编码所依据的原文：
  - 回答的问题：“Confirming that nearby points are semantically related represented an important step in establishing trust in an algorithm.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
  - 回答的问题：“Users can construct specialized linear projections based on text searches, supporting Task 3, finding meaningful directions in space.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
  - 关系：“brings up a list of nearest points and distances, which shows which words the algorithm has learned to be semantically related” [✓](https://research.google/blog/open-sourcing-the-embedding-projector-a-tool-for-visualizing-high-dimensional-data/)
  - 编码：“where users can choose data columns to color and label points” [✓](https://ar5iv.arxiv.org/html/1611.05469)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Embeddings are ubiquitous in machine learning, appearing in recommender systems, NLP, and many other applications.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 处理的材料：“TensorBoard reads tensors and metadata from the logs of your tensorflow projects” [✓](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)
- 处理的材料：“Each word (or sub-word in this case) will be associated with a 16-dimensional vector (or embedding)” [✓](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)
- 对象：“Clicking on any point (which represents the learned embedding for a given word)” [✓](https://research.google/blog/open-sourcing-the-embedding-projector-a-tool-for-visualizing-high-dimensional-data/)
- 关系：“highlights words that are adjacent to each other in the embedding (low-dimensional) space” [✓](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)
- 属性与度量：“each of which has a sentiment label (positive/negative)” [✓](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)
- 属性与度量：“Save Labels separately on a line-by-line manner.” [✓](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)
- 视图：“views of data in either a 2D or a 3D mode” [✓](https://research.google/blog/open-sourcing-the-embedding-projector-a-tool-for-visualizing-high-dimensional-data/)
- 视图：“(b) the projected view in the center” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 视图：“(c) the inspector panel on the right side, where users can search for particular points and see a list of nearest neighbors” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 编码：“to fade out more distant points” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 交互：“zooming, rotating, and panning using natural click-and-drag gestures” [✓](https://research.google/blog/open-sourcing-the-embedding-projector-a-tool-for-visualizing-high-dimensional-data/)
- 交互：“right-clicking and dragging defines a selection sphere” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 交互：“the user can isolate those points for further analysis on their own with the "Isolate Points" button” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 回答的问题：“Many users wanted to inspect the nearest neighbors of a given point.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 抽象与层级：“users then typically want to switch quickly between many views, zooming and filtering, and then closely inspecting details” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 为什么这样画：“it is customized for the kinds of tasks faced by machine learning developers and researchers” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 为什么这样画：“it is optimized for the use cases that arise in machine learning and includes special features to explore meaningful directions in a data set.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 为什么这样画：“Because t-SNE often preserves some local structure, in practice it supports both Task 1 and Task 2.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 为什么这样画：“To help interpretation of the 3D mode, the Projector uses multiple redundant depth cues” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 原来的问题：“Unfortunately, these static views are generally inadequate for exploring high-dimensional data” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 原来的问题：“Many tools exist to perform various types of dimensionality reduction, but they are largely non-interactive” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 原来的问题：“traditional systems often assume the underlying dimensions have a particular meaning” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 原来的问题：“We know of no current tools that help with this use case.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 局限与代价：“it could be useful to visually compare two embeddings. Doing so would require nontrivial additions to the current visualizations.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 局限与代价：“A second direction for future research is to make it easier for users to discover meaningful directions in the data.” [✓](https://ar5iv.arxiv.org/html/1611.05469)
- 局限与代价：“While the current interface makes it easy to explore various hypotheses, there may be ways for the computer to generate and test hypotheses automatically.” [✓](https://ar5iv.arxiv.org/html/1611.05469)

</details>
- 没读到：说明：projector.tensorflow.org 首页只读到 JS 代码和许可证文本，没有界面文字；界面描述来自 arXiv 论文与 Google 研究博客

<a id="argdown"></a>

### Argdown

- 领域：论证与讨论；议题：把一场辩论或论证重建成地图
- 编码：命题与论证；重点：连通与邻域、关系上的类型与量；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“This map hides a lot of the logical details for simplicty's sake (to dive into the details, click on "Source").” [✓](https://argdown.org/)
  - 抽象与层级：“where every premise and inferential step is visualized, it takes only a few configuration changes” [✓](https://argdown.org/)
  - 视图：“Your code is transformed into an argument map while you are typing.” [✓](https://argdown.org/)
  - 对象：“Creating statement and argument nodes” [✓](https://argdown.org/guide/a-first-example.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Writing pros & cons in Argdown is as simple as writing a Twitter message.” [✓](https://argdown.org/)
- 处理的材料：“Exports Argdown documents and argument maps to JSON, web component HTML, HTML, DOT, GRAPHML, SVG, PNG or PDF.” [✓](https://argdown.org/guide/installing-the-commandline-tool.html)
- 处理的材料：“The VS Code Argdown extension adds support for the Argdown argumentation syntax.” [✓](https://argdown.org/guide/installing-the-vscode-extension.html)
- 对象：“Creating group nodes” [✓](https://argdown.org/guide/a-first-example.html)
- 关系：“Creating edges” [✓](https://argdown.org/guide/a-first-example.html)
- 关系：“-> [Causal link]” [✓](https://argdown.org/)
- 属性与度量：“Changing the node style” [✓](https://argdown.org/guide/a-first-example.html)
- 属性与度量：“Changing the node size” [✓](https://argdown.org/guide/a-first-example.html)
- 视图：“Creating oldschool argument maps and inference trees” [✓](https://argdown.org/guide/a-first-example.html)
- 视图：“Changing the graph layout” [✓](https://argdown.org/guide/a-first-example.html)
- 交互：“Choose your own argument map style” [✓](https://argdown.org/)
- 交互：“Colorizing maps” [✓](https://argdown.org/guide/a-first-example.html)
- 交互：“Code linting: Prints syntax error with location information” [✓](https://argdown.org/guide/installing-the-commandline-tool.html)
- 交互：“you can publish your analysis as pdf, embed it as a web-component in a webpage” [✓](https://argdown.org/)
- 回答的问题：“Writing pros & cons in Argdown is as simple as writing a Twitter message.” [✓](https://argdown.org/)
- 回答的问题：“If you are new to argument mapping, read our tutorial about how this debate was reconstructed.” [✓](https://argdown.org/)
- 抽象与层级：“Choose your own argument map style” [✓](https://argdown.org/)
- 抽象与层级：“Creating group nodes” [✓](https://argdown.org/guide/a-first-example.html)
- 为什么这样画：“Writing pros & cons in Argdown is as simple as writing a Twitter message. You don't have to learn anything new, except a few simple rules that will feel very natural.” [✓](https://argdown.org/)
- 为什么这样画：“With these simple rules you will be able to define more complex relations between arguments or dive into the details of their logical premise-conclusion structures.” [✓](https://argdown.org/)
- 为什么这样画：“Argdown can even be used within Markdown! Your code is transformed into an argument map while you are typing.” [✓](https://argdown.org/)
- 为什么这样画：“With Argdown no user interface gets in your way. You can focus on writing without getting distracted.” [？](https://argdown.org/guide/a-first-example.html)
- 原来的问题：“Some of the above argument descriptions actually seem to contain different lines of thought, and it's recommendable to split those descriptions up” [✓](https://argdown.org/guide/a-first-example.html)
- 原来的问题：“Now, it's questionable whether all pros and cons are directly supporting or attacking the central claim.” [✓](https://argdown.org/guide/a-first-example.html)
- 局限与代价：“This map hides a lot of the logical details for simplicty's sake (to dive into the details, click on "Source").” [？](https://argdown.org/guide/a-first-example.html)

</details>
- 没读到：encodings

<a id="insightmaker"></a>

### Insight Maker

- 领域：系统建模；议题：搭建存量流量模型并改变参数，看系统的行为
- 编码：因果与反馈 + 流量网络；重点：环与反馈、对象上的度量、关系上的类型与量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 对象：“Types of Primitives Stocks Flows Variables Links Converters States Transitions Actions Agent Populations” [✓](https://www.insightmaker.com/help)
  - 属性与度量：“Run the model with various values for filling and draining to see the implications.” [✓](https://www.insightmaker.com/tag/simulation?page=3)
  - 关系：“Use Insight Maker to create rich pictures and causal loop diagrams.” [✓](https://www.insightmaker.com/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Equations and Formulas” [✓](https://www.insightmaker.com/help)
- 处理的材料：“Built-in Functions” [✓](https://www.insightmaker.com/help)
- 对象：“Simple bathtub model to show the difference between Stock and Flow.” [✓](https://www.insightmaker.com/tag/simulation?page=3)
- 关系：“Types of Primitives Stocks Flows Variables Links Converters States Transitions Actions Agent Populations” [✓](https://www.insightmaker.com/help)
- 属性与度量：“amount and interest rate and run the model to see the implications of changing these values.” [✓](https://www.insightmaker.com/tag/simulation?page=3)
- 视图：“Use Insight Maker to create rich pictures and causal loop diagrams.” [✓](https://www.insightmaker.com/)
- 交互：“Clone of Savings Account Model” [✓](https://www.insightmaker.com/tag/simulation?page=3)
- 交互：“Interactive Live Simulations” [✓](https://www.insightmaker.com/help)
- 回答的问题：“Use System Dynamics to gain insights into your system” [✓](https://www.insightmaker.com/)
- 抽象与层级：“Explore powerful simulation algorithms for System Dynamics and Agent Based Modeling.” [✓](https://www.insightmaker.com/)

</details>
- 没读到：encodings

<a id="tree-sitter"></a>

### Tree-sitter

- 领域：软件工程；议题：把源码解析成语法树，并随编辑增量更新
- 编码：层级与树；重点：包含与层次；把握：官方页面直接写了
- 编码所依据的原文：
  - 处理的材料：“It can build a concrete syntax tree for a source file and efficiently update the syntax tree as the source file is edited.” [✓](https://tree-sitter.github.io/tree-sitter/)
  - 抽象与层级：“a tree in which the less important details have been removed” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
  - 交互：“you can also click any node in the tree to select the corresponding part of the code” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
  - 抽象与层级：“by making a distinction between named and anonymous nodes” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The syntax tree should update as you type in the code.” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 对象：“trees that contain nodes for every individual token in the source code” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
- 对象：“Every tree has a root node” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
- 对象：“A syntax node’s type is a string that indicates which grammar rule the node represents.” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
- 关系：“Once you have a node, you can access the node’s children” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
- 关系：“you can also click any node in the tree to select the corresponding part of the code” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 关系：“the current node should be highlighted in the tree” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 属性与度量：“You can check whether any given node is named” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)
- 属性与度量：“Show anonymous nodes” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 视图：“Tree-sitter Syntax Tree Playground” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 视图：“You can enter one or more patterns into the Query panel.” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 视图：“Query Tree” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 编码：“Otherwise the problematic parts of the query will be underlined” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 编码：“its captures will be highlighted both in the Code and in the Query panels” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 交互：“The syntax tree should update as you type in the code.” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 交互：“detailed diagnostics will be available on hover” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 回答的问题：“Robust enough to provide useful results even in the presence of syntax errors” [✓](https://tree-sitter.github.io/tree-sitter/)
- 回答的问题：“Fast enough to parse on every keystroke in a text editor” [✓](https://tree-sitter.github.io/tree-sitter/)
- 回答的问题：“General enough to parse any programming language” [✓](https://tree-sitter.github.io/tree-sitter/)
- 回答的问题：“You can try out tree-sitter with a few pre-selected grammars on this page.” [✓](https://tree-sitter.github.io/tree-sitter/7-playground.html)
- 抽象与层级：“the syntax tree functions much like an abstract syntax tree” [✓](https://tree-sitter.github.io/tree-sitter/using-parsers/2-basic-parsing.html)

</details>

<a id="docling"></a>

### Docling

- 领域：文档处理；议题：把 PDF 等文档转成保留版面和阅读顺序的统一结构
- 编码：层级与树；重点：包含与层次、来源与证据；把握：官方页面直接写了
- 编码所依据的原文：
  - 关系：“which reference children and parents through JSON pointers” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
  - 属性与度量：“Layout information (i.e. bounding boxes) for all items, if available” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
  - 抽象与层级：“Disambiguation between main body and headers, footers (furniture)” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
  - 抽象与层级：“Document hierarchy with sections and groups” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Processes entire pages for comprehensive document conversion” [✓](https://huggingface.co/docling-project/SmolDocling-256M-preview)
- 处理的材料：“Trained for both scientific and non-scientific documents” [✓](https://huggingface.co/docling-project/SmolDocling-256M-preview)
- 对象：“we introduced a unified document representation format called DoclingDocument” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
- 对象：“Text, Tables, Pictures, and more” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
- 对象：“All items that have a text representation (paragraph, section heading, equation, ...)” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
- 关系：“The reading order of the document is encapsulated through the body tree and the order of children in each item in the tree” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
- 属性与度量：“Provenance information” [✓](https://docling-project.github.io/docling/concepts/docling_document/)
- 属性与度量：“Preserves document structure and document element bounding boxes” [✓](https://huggingface.co/docling-project/SmolDocling-256M-preview)
- 视图：“such as for markdown, dictionary etc.” [✓](https://docling-project.github.io/docling/concepts/architecture/)
- 回答的问题：“An ultra-compact vision-language model for end-to-end multi-modal document conversion” [✓](https://huggingface.co/docling-project/SmolDocling-256M-preview)
- 回答的问题：“Introduces DocTags an efficient and minimal representation for documents that is fully compatible with DoclingDocuments” [✓](https://huggingface.co/docling-project/SmolDocling-256M-preview)
- 抽象与层级：“The root node of a tree-structure for the main document body” [✓](https://docling-project.github.io/docling/concepts/docling_document/)

</details>
- 没读到：encodings；interactions；Space 演示页为 JS 渲染，界面文字未读到

<a id="docling-graph"></a>

### Docling Graph

- 领域：文档处理；议题：把文档变成带显式语义关系的知识图，用于需要精确实体连接的场合
- 编码：一般图与网络；重点：连通与邻域、关系上的类型与量、来源与证据；把握：官方页面直接写了
- 编码所依据的原文：
  - 关系：“builds a directed knowledge graph with explicit semantic relationships” [✓](https://docling-project.github.io/docling-graph/)
  - 关系：“Composition & Containment” [✓](https://docling-project.github.io/docling-graph/fundamentals/schema-definition/relationships/)
  - 属性与度量：“The __provenance__ node attribute” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/provenance/)
  - 回答的问题：“This transformation enables high-precision use cases in chemistry, finance, and legal domains, where AI must capture exact entity connections” [✓](https://docling-project.github.io/docling-graph/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Docling-Graph turns documents into validated Pydantic objects” [✓](https://docling-project.github.io/docling-graph/)
- 处理的材料：“Multi-Format Input: PDF, images, Office, HTML, Markdown, URLs, and more.” [✓](https://docling-project.github.io/docling-graph/)
- 对象：“Graph conversion transforms Pydantic models into NetworkX directed graphs, creating nodes for entities and edges for relationships.” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/graph-conversion/)
- 对象：“What Becomes a Node?” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/graph-conversion/)
- 关系：“Membership & Association” [✓](https://docling-project.github.io/docling-graph/fundamentals/schema-definition/relationships/)
- 关系：“Reference Edges (reference=True)” [✓](https://docling-project.github.io/docling-graph/fundamentals/schema-definition/relationships/)
- 属性与度量：“Node/edge counts, timestamps” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 属性与度量：“Node Distribution - Types and percentages” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 视图：“Interactive HTML Visualization” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 视图：“Markdown Reports” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 编码：“Color-coded node types” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 交互：“Zoom and pan” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 交互：“Node selection” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 交互：“Search functionality” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 交互：“Save as image” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)
- 抽象与层级：“Zoom and pan” [✓](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/)

</details>

<a id="graphrag"></a>

### Microsoft GraphRAG

- 领域：文本检索与知识建模；议题：回答关于整个语料库的整体性问题，以及关于具体实体的局部问题
- 编码：一般图与网络 + 层级与树；重点：群落与相似、包含与层次、对象上的度量；把握：官方页面直接写了
- 说明：社区层级是算法分出来的聚类，摘要是语义概括——两种抽象叠在一起；是否对应认知上的逻辑层级，官方页面没有说。
- 编码所依据的原文：
  - 抽象与层级：“Perform a hierarchical clustering of the graph using the Leiden technique” [✓](https://microsoft.github.io/graphrag/)
  - 抽象与层级：“Generate summaries of each community and its constituents from the bottom-up.” [✓](https://microsoft.github.io/graphrag/)
  - 交互：“Global Search for reasoning about holistic questions about the corpus by leveraging the community summaries.” [✓](https://microsoft.github.io/graphrag/)
  - 交互：“Local Search for reasoning about specific entities by fanning-out to their neighbors and associated concepts.” [✓](https://microsoft.github.io/graphrag/)
  - 编码：“with the size representing the degree of the entity, and the color representing its community” [✓](https://microsoft.github.io/graphrag/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“extracting a knowledge graph out of raw text” [✓](https://microsoft.github.io/graphrag/)
- 处理的材料：“creates a knowledge graph based on an input corpus” [✓](https://microsoft.github.io/graphrag/)
- 对象：“Each circle is an entity (e.g., a person, place, or organization)” [✓](https://microsoft.github.io/graphrag/)
- 对象：“Community Reports Table” [✓](https://microsoft.github.io/graphrag/index/default_dataflow/)
- 对象：“Claim Extraction (optional)” [✓](https://microsoft.github.io/graphrag/index/default_dataflow/)
- 关系：“Entity & Relationship Extraction” [✓](https://microsoft.github.io/graphrag/index/default_dataflow/)
- 关系：“Entity & Relationship Summarization” [✓](https://microsoft.github.io/graphrag/index/default_dataflow/)
- 关系：“Extract all entities, relationships, and key claims from the TextUnits.” [✓](https://microsoft.github.io/graphrag/)
- 属性与度量：“Run for Average Degree and Leiden Algorithm” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 属性与度量：“until we reach a community-size threshold” [✓](https://microsoft.github.io/graphrag/index/default_dataflow/)
- 视图：“Figure 1: An LLM-generated knowledge graph built using GPT-4 Turbo.” [✓](https://microsoft.github.io/graphrag/)
- 视图：“Open the Graph in Gephi” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 视图：“Layout the Graph” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 编码：“Resize Nodes by Degree Centrality” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 编码：“This will color the graph based on the partitions discovered by Leiden.” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 交互：“Add Text Labels (Optional)” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 回答的问题：“Global Search for reasoning about holistic questions about the corpus by leveraging the community summaries.” [✓](https://microsoft.github.io/graphrag/)
- 回答的问题：“Local Search for reasoning about specific entities by fanning-out to their neighbors and associated concepts.” [✓](https://microsoft.github.io/graphrag/)
- 回答的问题：“to holistically understand summarized semantic concepts over large data collections” [✓](https://microsoft.github.io/graphrag/)
- 回答的问题：“The following step-by-step guide walks through the process to visualize a knowledge graph” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 抽象与层级：“building a community hierarchy, generating summaries for these communities” [✓](https://microsoft.github.io/graphrag/)
- 抽象与层级：“This method will apply a recursive community-clustering to our graph until we reach a community-size threshold.” [✓](https://microsoft.github.io/graphrag/index/default_dataflow/)
- 为什么这样画：“graphml is a standard file format supported by many visualization tools. We recommend trying Gephi.” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 为什么这样画：“some of the settings recommended below are based on our own experience of what works well” [✓](https://microsoft.github.io/graphrag/visualization_guide/)
- 为什么这样画：“GraphRAG uses knowledge graphs to provide substantial improvements in question-and-answer performance when reasoning about complex information.” [✓](https://microsoft.github.io/graphrag/)
- 原来的问题：“Baseline RAG struggles to connect the dots.” [✓](https://microsoft.github.io/graphrag/)
- 原来的问题：“Baseline RAG performs poorly when being asked to holistically understand summarized semantic concepts over large data collections or even singular large documents.” [✓](https://microsoft.github.io/graphrag/)

</details>

<a id="lightrag"></a>

### LightRAG

- 领域：文本检索与知识建模；议题：用图结构配合向量做检索，并用网页看板查看知识
- 编码：一般图与网络；重点：连通与邻域；把握：证据很少
- 编码所依据的原文：
  - 抽象与层级：“It adopts a dual-layer architecture to manage both knowledge graphs (KGs) and vector embeddings” [✓](https://pypi.org/project/lightrag-hku/)
  - 视图：“an interface that allows you to insert, query, and visualize LightRAG knowledge through an intuitive web-based dashboard” [✓](https://pypi.org/project/lightrag-hku/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“LightRAG's document processing pipeline supports MinerU, Docling, and” [✓](https://pypi.org/project/lightrag-hku/)
- 对象：“rebuild the affected entities and relationships” [✓](https://pypi.org/project/lightrag-hku/)
- 关系：“rebuild the affected entities and relationships” [✓](https://pypi.org/project/lightrag-hku/)
- 交互：“insert, query, and visualize LightRAG knowledge” [✓](https://pypi.org/project/lightrag-hku/)
- 回答的问题：“an interface that allows you to insert, query, and visualize LightRAG knowledge through an intuitive web-based dashboard” [✓](https://pypi.org/project/lightrag-hku/)

</details>
- 没读到：attributes；encodings；官网或文档站（未找到，WebSearch 结果均为第三方页面；GitHub 仓库不访问）

<a id="graphiti"></a>

### Graphiti

- 领域：Agent 记忆；议题：让 Agent 长期记得事实，并知道哪些事实现在不再成立
- 编码：一般图与网络 + 序列与事件流；重点：时间与演化、来源与证据；把握：官方页面直接写了
- 说明：没有可视化的案例：说明在画图之前，时间有效期和来源要先进数据模型，否则图只能显示“现在”。
- 编码所依据的原文：
  - 关系：“Graph edges include temporal metadata to record relationship lifecycles.” [✓](https://help.getzep.com/graphiti/getting-started/overview)
  - 属性与度量：“Explicit bi-temporal tracking” [✓](https://help.getzep.com/graphiti/getting-started/overview)
  - 抽象与层级：“Episodic data, semantic entities, communities” [✓](https://help.getzep.com/graphiti/getting-started/overview)
  - 属性与度量：“maintaining data provenance” [✓](https://help.getzep.com/graphiti/getting-started/overview)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Adding a text or message Episode” [✓](https://help.getzep.com/graphiti/core-concepts/adding-episodes)
- 处理的材料：“Adding an Episode using structured data in JSON format” [✓](https://help.getzep.com/graphiti/core-concepts/adding-episodes)
- 对象：“An episode is itself a node” [✓](https://help.getzep.com/graphiti/core-concepts/adding-episodes)
- 对象：“A Context Graph is a temporal knowledge graph — a graph of entities, relationships, and facts” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 对象：“Custom Entity and Edge Types” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 关系：“entity and edge extraction” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 属性与度量：“Temporal edge invalidation” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 属性与度量：“Graph edges include temporal metadata to record relationship lifecycles.” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 交互：“Hybrid semantic, keyword, and graph-based search” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 交互：“CRUD Operations” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 交互：“Adding Fact Triples” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 回答的问题：“Graphiti helps you create and query Context Graphs that evolve over time.” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 回答的问题：“enabling long-term recall and state-based reasoning for both assistants and agents” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 回答的问题：“Use it to build and query a single Context Graph per subject locally” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 抽象与层级：“Entity clusters & community summaries” [✓](https://help.getzep.com/graphiti/getting-started/overview)
- 抽象与层级：“a single Context Graph per subject” [✓](https://help.getzep.com/graphiti/getting-started/overview)

</details>
- 没读到：views；encodings

<a id="tube-map"></a>

### 伦敦地铁图（Beck）

- 领域：交通；议题：乘客要知道在哪条线、哪站换乘、几站到达，不需要知道地面上的真实距离
- 编码：一般图与网络；重点：连通与邻域、有什么；把握：官方页面直接写了
- 编码所依据的原文：
  - 处理的材料：“He mapped Tube lines using geographically distorted straight lines, which didn’t represent the true shape of the network’s tunnels under the city.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
  - 关系：“the connections and interchanges between Tube lines and stations” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
  - 抽象与层级：“Over time, early map designs were simplified. Central London was distorted and made bigger.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
  - 回答的问题：“This made the map easier to use and reduced the network’s complexity.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“How could you accurately show the Tube network to scale, but also make it fit in someone’s pocket?” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 对象：“Instead, he created a diagram that made the connections and interchanges between Tube lines and stations clearer to see.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 属性与度量：“The lines were colour-coded – and some, like the Bakerloo and District, have the same colours today.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 属性与度量：“Beck's diagrammatic tube map was commissioned by the new London Passenger Transport Board in 1933.” [✓](https://www.londonmuseum.org.uk/collections/v/object-536576/railway-map/)
- 视图：“Instead, he created a diagram that made the connections and interchanges between Tube lines and stations clearer to see.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 视图：“This map of London's Underground railways was designed by Harry Beck.” [✓](https://www.londonmuseum.org.uk/collections/v/object-536576/railway-map/)
- 编码：“The lines were colour-coded – and some, like the Bakerloo and District, have the same colours today.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 回答的问题：“How could you accurately show the Tube network to scale, but also make it fit in someone’s pocket?” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 抽象与层级：“He also made the central London area much larger in scale, so station names were easier to read.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)
- 抽象与层级：“This made the map easier to use and reduced the network’s complexity.” [✓](https://www.londonmuseum.org.uk/collections/london-stories/harry-beck-revolutionised-tube-map/)

</details>
- 没读到：interactions；未读到：par.tfl.gov.uk 官方页面返回 525，没读到；维基百科未读，博物馆原始页面已够用

<a id="nextstrain"></a>

### Nextstrain / Auspice

- 领域：流行病与基因组；议题：同时看病原体的系统发生关系、地理传播和时间
- 编码：层级与树 + 空间与几何、序列与事件流；重点：跨视图的同一对象、时间与演化、空间位置；把握：官方页面直接写了
- 编码所依据的原文：
  - 编码：“Color is used consistently throughout the app in order to link different panels.” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
  - 视图：“Phylogenetic trees Phylogeographic map” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
  - 交互：“A number of controls are made available in a sidebar to control the time period viewed, the layout of the tree, etc.” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
  - 关系：“their phylogenetic relationships, putative transmissions on the map” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Auspice: An Open-source Interactive Tool for Visualising Phylogenomic Data” [✓](https://docs.nextstrain.org/projects/auspice/)
- 处理的材料：“An open-source project to harness the scientific and public health potential of pathogen genome data” [✓](https://nextstrain.org/)
- 对象：“display relationships between isolates such as their phylogenetic relationships, putative transmissions on the map, and variability across the genome.” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 属性与度量：“The generator of the data controls which traits are able to be visualized” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 属性与度量：“variability across the genome” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 视图：“Interacting with Nextstrain’s phylogeographic visualisations” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 编码：“changing between three different colorings: clades, age-ranges & mutations at a certain genome position.” [✓](https://docs.nextstrain.org/projects/auspice/)
- 交互：“transmissions can be turned off if the data is not informative.” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 交互：“changing between three different colorings” [✓](https://docs.nextstrain.org/projects/auspice/)
- 回答的问题：“providing a novel surveillance tool to the scientific and public health communities” [✓](https://nextstrain.org/)
- 回答的问题：“display relationships between isolates such as their phylogenetic relationships” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 抽象与层级：“Color is used consistently throughout the app in order to link different panels.” [✓](https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html)
- 抽象与层级：“Displaying multiple trees” [✓](https://docs.nextstrain.org/projects/auspice/)
- 为什么这样画：“We have developed Nextstrain to visualize outbreaks in as close to real time as possible.” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 为什么这样画：“Multiple views into different facets of the data are presented and remain in sync as one interacts with the data.” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 为什么这样画：“By animating the temporal dimension, a high level overview of how the entire outbreak unfolded is quickly gained.” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 为什么这样画：“Communicating scientific results while also allowing interrogation of the underlying data is an integral part of the scientific process.” [✓](https://docs.nextstrain.org/projects/auspice/)
- 原来的问题：“Current scientific publishing practices hinder both the rapid dissemination of epidemiologically relevant results and the ability to easily interact with the data used to draw inferences.” [✓](https://docs.nextstrain.org/projects/auspice/)
- 原来的问题：“Such analyses are often done in isolation, and may lack the spatial or temporal context in which to best interpret the results” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 原来的问题：“Furthermore, the results of analyses are rarely made available to the public or health bodies until after publication, which may be too late to aid understanding or effect change in policy.” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 局限与代价：“Sampling bias and lack of data can obscure transmission links, and in certain cases we have chosen not to display the inferred states.” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 局限与代价：“we try to address these concerns by preventing access to the raw genome sequences” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)
- 局限与代价：“we note the potential for recombination or low mutation rate to confound phylogenetic signal” [✓](https://www.bedford.io/pdfs/papers/hadfield-nextstrain.pdf)

</details>
- 没读到：abstraction 仅写到多视角联动与多棵树，折叠、钻取、聚合、层级、缩放未在所读页面中写明

<a id="onezoom"></a>

### OneZoom 生命之树

- 领域：生物分类；议题：在上百万物种的进化树里自由探索，不被规模压垮
- 编码：层级与树；重点：包含与层次、对象上的度量、总体分布；把握：官方页面直接写了
- 编码所依据的原文：
  - 交互：“Explore OneZoom like you would a geographic map, zoom in to reveal more detail by pinching on your touch screen or scrolling on your mouse.” [✓](https://www.onezoom.org/introduction)
  - 编码：“Under default settings, the leaf colours correspond to the risk of extinction for the species that leaf represents.” [✓](https://www.onezoom.org/full_guide)
  - 抽象与层级：“Allowing branches to have a thickness assists the concept of scale when zooming” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
  - 回答的问题：“Our vision for OneZoom is to do for the tree of life what online mapping tools have done for the globe” [✓](https://www.onezoom.org/introduction)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Leaves corresponding to species that are vulnerable, endangered, or critically endangered according to the IUCN Red List are shown in red.” [✓](https://www.onezoom.org/introduction)
- 处理的材料：“Each leaf represents a different species and the branches show how they are evolved from common ancestors over billions of years.” [✓](https://www.onezoom.org/introduction)
- 对象：“Each leaf represents a different species” [✓](https://www.onezoom.org/introduction)
- 对象：“one branch splits simultaneously into more than two descendants” [✓](https://www.onezoom.org/introduction)
- 关系：“the branches show how they are evolved from common ancestors over billions of years” [✓](https://www.onezoom.org/introduction)
- 关系：“this is called a polytomy” [✓](https://www.onezoom.org/introduction)
- 属性与度量：“There is no theoretical limit to the amount of metadata that can be put on a leaf or branch of the tree” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 属性与度量：“according to our index of species popularity” [✓](https://www.onezoom.org/introduction)
- 视图：“Try the 'polytomy' view Try the 'fern' view Try the 'natural' view” [✓](https://www.onezoom.org/introduction)
- 视图：“interactive fractal-inspired graph” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 编码：“Another colour scheme on offer shows how popular each species is according to our index of species popularity” [✓](https://www.onezoom.org/introduction)
- 编码：“we colour the randomly resolved branches in a slightly lighter shade” [✓](https://www.onezoom.org/introduction)
- 编码：“evolutionarily distinct species and clades appear larger” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 交互：“You can use the search box to type what you're looking for.” [✓](https://www.onezoom.org/full_guide)
- 交互：“You can change the colour scheme from the settings menu.” [✓](https://www.onezoom.org/full_guide)
- 交互：“fly through the tree to search hits with an animation feature” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 回答的问题：“You can use the search box to type what you're looking for.” [✓](https://www.onezoom.org/full_guide)
- 抽象与层级：“zoom in to reveal more detail” [✓](https://www.onezoom.org/introduction)
- 抽象与层级：“these data can be displayed at any size and zoomed in on” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 抽象与层级：“OneZoom: A Fractal Explorer for the Tree of Life” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 为什么这样画：“The key concept of our solution is that all the data is on one page so that all the user has to do is zoom to reveal it—hence the name OneZoom” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 为什么这样画：“In order to place the phylogenetic data on a scalable two-dimensional map, OneZoom uses concepts inspired by fractal geometry.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 为什么这样画：“We give the branches of the tree a width so that they appear as filled shapes rather than narrow lines and thus can contain rich metadata within them” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 为什么这样画：“Zooming to reveal further details as implemented in OneZoom feels intuitive because it is akin to the way we explore the real world by moving closer to objects of interest” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 原来的问题：“we all too often constrain ourselves to the “paper paradigm”—the practice of displaying data in ways that are optimized for printing on paper.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 原来的问题：“This approach is costly and does not give tree visualization capabilities to the masses, which is what is really needed.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 原来的问题：“they can display large trees, but users do not find them intuitive” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 原来的问题：“Unfortunately, there has so far been no practical and intuitive way to explore even the much smaller trees with thousands of tips that are now being routinely produced.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 局限与代价：“but all these have the common property that evolutionarily distinct species and clades appear larger.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 局限与代价：“The natural view emphasizes tree balance over rates of diversification.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 局限与代价：“Our software plots the phylogeny in a shape that can reflect the topology and balance, whilst the timescales are expressed in ways that are independent of shape including color, text, and animation.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)
- 局限与代价：“In OneZoom, we can be wasteful of space because there is an infinite quantity of space available.” [✓](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001406)

</details>

<a id="circos"></a>

### Circos

- 领域：比较基因组；议题：比较基因组，显示基因组位置对之间的关系
- 编码：空间与几何 + 一般图与网络；重点：空间位置、连通与邻域；把握：页面信息支持，归类靠推断
- 说明：本案例的摘录里有 MISSING 标记：PMC 页面对我们的核对脚本返回的不是全文，摘录来自子智能体的阅读，未经脚本核对。
- 编码所依据的原文：
  - 关系：“to facilitate the display of relationships between pairs of positions by the use of ribbons” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
  - 视图：“Circos is capable of displaying data as scatter, line, and histogram plots, heat maps, tiles, connectors, and text.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
  - 抽象与层级：“focus on regions of interest, axis breaks can be used to map chromosomes onto any number of ideograms” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
  - 抽象与层级：“To overcome this, scatter, histogram, and text tracks can be used as density plots” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Such data are routinely produced by sequence alignments, hybridization arrays, genome mapping, and genotyping studies.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 处理的材料：“Bitmap or vector images can be created from GFF-style data inputs and hierarchical configuration files” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 对象：“Circos uses a circular ideogram layout” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 对象：“Each data track can contain a rule block that filters and formats data elements based on position, value, or previous formatting.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 关系：“any other kind of positional relationships between genomic intervals” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 属性与度量：“based on position, value, or previous formatting” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 属性与度量：“data points can have their value and format characteristics altered by flexible rules” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 视图：“Circos can draw ideograms in any order and orientation.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 编码：“ribbons, which encode the position, size, and orientation of related genomic elements” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 编码：“glyph size is proportional to the number of small-scale events in each 5-Mb region” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 回答的问题：“To address the challenge in displaying large volumes of genomic rearrangement data” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 抽象与层级：“The resolution of a whole-genome view precludes the display of individual small-scale events at their native scale” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 为什么这样画：“we have developed Circos, which applies the circular ideogram layout to display relationships between genomic intervals.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 为什么这样画：“we require instructive and clear visualizations that (1) adapt to the density and dynamic range of the data, (2) maintain complexity and detail in the data” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 为什么这样画：“Circos uses a circular ideogram layout to facilitate the display of relationships between pairs of positions by the use of ribbons” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 原来的问题：“Previous efforts to visualize positional relationships applied linearly arranged ideograms, connected by lines, to represent rearrangements” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 原来的问题：“In such figures, multitudes of lines transgress unrelated ideograms and make patterns very difficult to discern.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 原来的问题：“Although color maps address the problem of overburdened visualizations by mapping a position pair onto a position and a color, they reduce the texture and richness of the data.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 局限与代价：“The resolution of a whole-genome view precludes the display of individual small-scale events at their native scale.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 局限与代价：“which cannot be effectively shown at this resolution” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)
- 局限与代价：“but details of these features cannot be discerned at this scale.” [✓](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/)

</details>
- 没读到：interactions（论文写的是配置文件与批量生成，未写交互操作）；circos.ca 官网：probe 返回 TLS 证书校验失败，没读到（未绕过校验）；仅读到 1 个官方页面（PMC 论文）

<a id="reactome"></a>

### Reactome 通路浏览器

- 领域：分子生物学通路；议题：浏览人类生物通路：从全部通路总览，进入某条通路的反应图
- 编码：层级与树 + 一般图与网络；重点：包含与层次、先后与依赖方向；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“This overview displays all pathways and allows rapid zooming to details.” [✓](https://reactome.org/userguide/pathway-browser)
  - 抽象与层级：“Shows the hierarchical organisation of Reactome pathways” [✓](https://reactome.org/userguide/pathway-browser)
  - 关系：“Pathway nodes are connected to their subpathways by edges (lines).” [✓](https://reactome.org/userguide/pathway-browser)
  - 关系：“so that the preceding reaction is above and the subsequent reaction below” [✓](https://reactome.org/userguide/pathway-browser)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Reactome is a free, open-source, curated and peer-reviewed pathway database.” [✓](https://reactome.org/)
- 处理的材料：“Where does the data come from?” [✓](https://www.ebi.ac.uk/training/online/courses/reactome-exploring-biological-pathways/understanding-the-pathway-browser/)
- 对象：“i.e. pathway, reaction, complex, set, protein or small molecule” [✓](https://reactome.org/userguide/pathway-browser)
- 对象：“pathway events or steps, known as reactions” [✓](https://reactome.org/userguide/pathway-browser)
- 视图：“When a Pathway Diagram contains subpathways” [✓](https://reactome.org/userguide/pathway-browser)
- 视图：“Shows the hierarchical organisation of Reactome pathways” [✓](https://reactome.org/userguide/pathway-browser)
- 视图：“This overview displays all pathways and allows rapid zooming to details.” [✓](https://reactome.org/userguide/pathway-browser)
- 编码：“the area containing each subpathway is overlaid with a coloured box, labelled with the subpathway name” [✓](https://reactome.org/userguide/pathway-browser)
- 交互：“As you zoom in, labels appear for the subpathway nodes.” [✓](https://reactome.org/userguide/pathway-browser)
- 交互：“Click on the plus and minus buttons to zoom in and out.” [✓](https://reactome.org/userguide/pathway-browser)
- 交互：“The overlay of user-supplied expression data onto a pathway” [✓](https://reactome.org/userguide/pathway-browser)
- 交互：“In-Diagram Search – click the button to open the search panel.” [✓](https://reactome.org/userguide/pathway-browser)
- 回答的问题：“Our goal is to provide intuitive bioinformatics tools for the visualization, interpretation and analysis of pathway knowledge” [✓](https://reactome.org/)
- 回答的问题：“Why do we need a pathway database?” [✓](https://www.ebi.ac.uk/training/online/courses/reactome-exploring-biological-pathways/understanding-the-pathway-browser/)
- 抽象与层级：“When a Pathway Diagram contains subpathways, the area containing each subpathway is overlaid with a coloured box” [✓](https://reactome.org/userguide/pathway-browser)

</details>
- 没读到：attributes（所读页面只写到对象类型，未写属性或度量值）

<a id="sbgn"></a>

### SBGN 系统生物学图形标记

- 领域：分子生物学通路；议题：用统一的图形语言表示生物网络，并按想传达的信息选择详细程度
- 编码：一般图与网络；重点：先后与依赖方向、关系上的类型与量、跨视图的同一对象；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“They can be seen as three alternative projections of the underlying, more complex biological information.” [✓](https://sbgn.github.io/specifications)
  - 视图：“The SBGN Process Description (PD) language shows the temporal courses of biochemical interactions in a network.” [✓](https://sbgn.github.io/specifications)
  - 视图：“allows you to see all the relationships in which a given entity participates, regardless of the temporal aspects” [✓](https://sbgn.github.io/specifications)
  - 回答的问题：“Know the message your network should convey. This will help you choose what to omit, what to represent, and how to represent it.” [？](https://sbgn.github.io/learning)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“They can be seen as three alternative projections of the underlying, more complex biological information.” [✓](https://sbgn.github.io/specifications)
- 对象：“Represents a very large biochemical substance, usually a protein, a nucleic acid or a complex sugar.” [✓](https://sbgn.github.io/symbols)
- 对象：“Represents a small biochemical substance, usually an atom, a mono-atomic ion, a salt, a solid metal, etc.” [✓](https://sbgn.github.io/symbols)
- 对象：“Represents a biochemical entity composed of other biochemical entities, whether macromolecules, simple chemicals or other complexes.” [✓](https://sbgn.github.io/symbols)
- 对象：“a process is represented by the process node, an unlabelled square.” [✓](https://sbgn.github.io/symbols)
- 关系：“via arcs representing consumption, production or modulation.” [✓](https://sbgn.github.io/symbols)
- 关系：“In SBGN Process Description language, the stimulation of a process is represented by the stimulation arc” [✓](https://sbgn.github.io/symbols)
- 关系：“Glucose and ATP are linked to the process by consumption arcs” [✓](https://sbgn.github.io/learning)
- 关系：“Relationships can be seen as rules describing the influences of entities nodes on other relationships.” [✓](https://sbgn.github.io/specifications)
- 属性与度量：“"P@Y701" means "phosphorylated at tyrosine 701"” [✓](https://sbgn.github.io/learning)
- 属性与度量：“represent a multimer macromolecule X that is phosphorylated (state variable P@S100) and is a dimer (unit of information N:2).” [✓](https://sbgn.github.io/symbols)
- 属性与度量：“give additional information about the physical environment of the compartment (pH, temperature, voltage, etc.)” [✓](https://sbgn.github.io/symbols)
- 属性与度量：“the state of a macromolecule (that is the values of all its state variables) is part of its identity.” [✓](https://sbgn.github.io/symbols)
- 视图：“There are three orthogonal and complementary visual languages defined in SBGN” [✓](https://sbgn.github.io/specifications)
- 视图：“The SBGN Activity Flow (AF) language depicts the flow of information between biochemical entities in a network.” [✓](https://sbgn.github.io/specifications)
- 编码：“The generation of products is represented by the production arc, an arc ending by a filled arrowhead.” [✓](https://sbgn.github.io/symbols)
- 编码：“The target extremity of a stimulation carries an empty arrowhead” [✓](https://sbgn.github.io/symbols)
- 编码：“The target extremity of a catalysis carries an empty circle.” [✓](https://sbgn.github.io/symbols)
- 编码：“The compartment has its own symbol: it is an enclosed structure with thick borders that can have any geometry.” [✓](https://sbgn.github.io/symbols)
- 交互：“Redrawing a small example diagram will help with a quick start” [✓](https://sbgn.github.io/learning)
- 交互：“the available templates can be used to design a diagram by adding one brick after another” [✓](https://sbgn.github.io/learning)
- 回答的问题：“is particularly convenient for representing the effects of perturbations, whether genetic or environmental in nature” [✓](https://sbgn.github.io/specifications)
- 回答的问题：“It can be used to show all the molecular interactions taking place in a network of biochemical entities” [✓](https://sbgn.github.io/specifications)
- 抽象与层级：“Select the right level of granularity for your map. Be as specific as you can without diluting your message” [？](https://sbgn.github.io/learning)
- 抽象与层级：“Represents a biochemical entity composed of other biochemical entities” [✓](https://sbgn.github.io/symbols)
- 抽象与层级：“Design your map in a reasonable level of detail.” [✓](https://sbgn.github.io/learning)
- 为什么这样画：“They can be seen as three alternative projections of the underlying, more complex biological information.” [✓](https://sbgn.github.io/specifications)
- 为什么这样画：“Reading a PD diagram is much simpler if it is seen as a collection of interconnected processes.” [✓](https://sbgn.github.io/learning)
- 为什么这样画：“This will help you choose what to omit, what to represent, and how to represent it.” [✓](https://sbgn.github.io/learning)
- 为什么这样画：“Be as specific as you can without diluting your message: important parts of your network should stand out to the readers.” [✓](https://sbgn.github.io/learning)
- 局限与代价：“It omits information about the state transitions of entities and is particularly convenient for representing the effects of perturbations, whether genetic or environmental in nature.” [✓](https://sbgn.github.io/specifications)
- 局限与代价：“Next, to avoid any confusion, we concentrate only on the Process Description (PD) language.” [✓](https://sbgn.github.io/learning)

</details>

<a id="llnl-energy-flow"></a>

### LLNL 美国能源流向图

- 领域：能源；议题：看清能源从哪里来、被哪些部门使用、有多少被浪费
- 编码：流量网络；重点：关系上的类型与量、总体分布；把握：官方页面直接写了
- 编码所依据的原文：
  - 编码：“Every line's width is proportional to the quantity of energy used by a particular sector” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
  - 编码：“Lines are color-coded according to the form of energy.” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
  - 抽象与层级：“the four major end-use categories (residential, commercial, industrial, transportation)” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
  - 回答的问题：“details the sources of energy production, how Americans are using energy and how much waste exists” [✓](https://flowcharts.llnl.gov/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The development team combined data from the Energy Information Administration with its own software to generate updated charts” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 处理的材料：“that contain quantitative data about resource, commodity, and byproduct flows in a graphical form.” [✓](https://flowcharts.llnl.gov/)
- 处理的材料：“Energy resources included solar, nuclear, hydroelectric, wind, geothermal, natural gas, coal, biomass, and petroleum.” [✓](https://flowcharts.llnl.gov/commodities/energy)
- 对象：“The lines flow from resources (left) to disposition (right)” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 对象：“the four major end-use categories (residential, commercial, industrial, transportation)” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 对象：“This rejected energy ultimately takes the form of waste heat transferred to the environment.” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 关系：“where they diverge in proportion to how much energy from each resource powers the four major end-use categories” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 关系：“The water flow charts also track the fate of water” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 关系：“map the carbon emissions from their physical sources” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 关系：“visualize the complex interrelationships involved in managing our nation’s resources” [✓](https://flowcharts.llnl.gov/)
- 属性与度量：“a unit that quantifies all forms of energy from heat to electricity, equivalently” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 属性与度量：“generate updated charts of the United States' and individual states' energy use annually” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 属性与度量：“In the 1990s, at five-year intervals, flow charts of water use in the United States and individual states became available.” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 视图：“Flow charts, also referred to as Sankey Diagrams, are single-page references” [✓](https://flowcharts.llnl.gov/)
- 视图：“turned to the Sankey diagram for its versatility in displaying quantitative information visually” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 视图：“Lawrence Livermore has been producing one-page charts that summarize these flows for decades.” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 编码：“The lines flow from resources (left) to disposition (right)” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 交互：“Search the flow chart database by year, country, and state.” [✓](https://flowcharts.llnl.gov/commodities/energy)
- 交互：“Reset parameters for a new search.” [✓](https://flowcharts.llnl.gov/commodities/energy)
- 交互：“Click image to enlarge or download a PDF version” [✓](https://flowcharts.llnl.gov/)
- 回答的问题：“help scientists, analysts, and other decision makers to visualize the complex interrelationships” [✓](https://flowcharts.llnl.gov/)
- 回答的问题：“in understanding energy usage and its affect on the economic security of the United States” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 抽象与层级：“energy, carbon, and water flows at the international, state, municipal, and organizational (e.g., Air Force) level” [✓](https://flowcharts.llnl.gov/)
- 抽象与层级：“A single energy flow chart depicting resources and their use represents vast quantities of data.” [✓](https://flowcharts.llnl.gov/commodities/energy)
- 为什么这样画：“To develop the first chart of U.S. energy use, Livermore's experts turned to the Sankey diagram for its versatility in displaying quantitative information visually.” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 为什么这样画：“Flow charts are an ideal tool for analyzing not only energy, but also carbon (shown here), water, and other relevant "networks."” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 为什么这样画：“The changing economics of energy created the need to understand how much energy the United States uses from coal, petroleum, nuclear, and renewable sources” [✓](https://star.llnl.gov/energy-homeland-security/energy-security/energy-flow-charts)
- 为什么这样画：“These flow charts help scientists, analysts, and other decision makers to visualize the complex interrelationships involved in managing our nation’s resources.” [✓](https://flowcharts.llnl.gov/)

</details>

<a id="icij-offshore-leaks"></a>

### ICIJ Offshore Leaks 数据库

- 领域：调查报道与金融；议题：查出离岸公司背后是谁，以及两个人之间有什么间接联系
- 编码：一般图与网络；重点：连通与邻域、关系上的类型与量、来源与证据；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 对象：“Officer - A person or company who plays a role in an offshore entity, such as beneficiary, director, or shareholder.” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
  - 回答的问题：“discover the shortest paths between two entity officers through a set of Entity or Address nodes” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
  - 交互：“If you select the filter “Officers,” you’ll be able to see all the people connected to France.” [✓](https://offshoreleaks.icij.org/pages/howtouse)
  - 处理的材料：“They come from leaked records and not a standardized corporate registry, so there may be duplicates, including in the same leak.” [✓](https://offshoreleaks.icij.org/pages/about)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The data comes directly from the leaked files ICIJ has received in connection with various investigations” [✓](https://offshoreleaks.icij.org/pages/about)
- 处理的材料：“it doesn’t disclose bank accounts, email exchanges and financial transactions contained in the documents.” [✓](https://offshoreleaks.icij.org/pages/about)
- 对象：“Entity - The offshore legal entity.” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 对象：“Intermediary - A go-between for someone seeking an offshore corporation and an offshore service provider” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 对象：“Address - The registered address as it appears in the original databases obtained by ICIJ.” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 关系：“They're connected to form a "graph" that reveals a complex web of relationships.” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 关系：“explore the connections between this company and related addresses, shareholders, beneficiaries and more” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 关系：“Intermediary connected to an Entity node through the intermediary_of relationship” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 属性与度量：“The records cover more than 80 years up to 2020” [✓](https://offshoreleaks.icij.org/pages/about)
- 属性与度量：“The Panama Papers data, added to the Offshore Leaks Database in May 2016” [✓](https://offshoreleaks.icij.org/pages/about)
- 属性与度量：“connected to Ecuador and registered in the British Virgin Islands” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 属性与度量：“Beneficial ownership data on more than 25,000 entities from the Pandora Papers investigation” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 视图：“you’ll also see an interactive visualization that allows you to explore the connections” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 视图：“There’s also a text list of these connections” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 视图：“you can switch between the graph visualization and tabular results” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 视图：“The search results are displayed in sections” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 交互：“Clicking on the beneficiary node shows the address connected to Allawi” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 交互：“you could have filtered by jurisdiction, for example by clicking on “British Virgin Islands” in the right menu.” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 交互：“searching by names or keywords, looking for country-specific connections or browsing offshore entities by jurisdiction” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 回答的问题：“Find out who’s behind more than 810,000 offshore companies, foundations and trusts.” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 回答的问题：“The database strips away the secrecy that cloaks companies and trusts incorporated in tax havens and exposes the people behind them.” [✓](https://offshoreleaks.icij.org/pages/about)
- 回答的问题：“Find all the names connected to a country” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 抽象与层级：“The search results are displayed in sections: you can see the offshore entities” [✓](https://offshoreleaks.icij.org/pages/howtouse)
- 抽象与层级：“We can also check how many entities of each type are in our database.” [✓](https://guides.neo4j.com/sandbox/icij-offshoreleaks/panama-papers-examples.html)
- 抽象与层级：“You can browse all the companies registered in one of the jurisdictions included in our data” [✓](https://offshoreleaks.icij.org/pages/howtouse)

</details>
- 没读到：encodings

<a id="wikidata-query-views"></a>

### Wikidata Query Service 结果视图

- 领域：开放知识图谱；议题：把一次 SPARQL 查询的结果换成不同的图来看
- 编码：表与多维属性；重点：对象上的度量、时间与演化、空间位置；把握：官方页面直接写了
- 说明：这是研究“数据结构的哪一部分对应视图的哪个通道”最直接的一例：每种视图的页面都列出了它要的列角色。
- 编码所依据的原文：
  - 视图：“Shows the result data as a table.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
  - 视图：“Shows the result data as map with OpenStreetMap data.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
  - 编码：“First will be X-axis, second Y-axis” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
  - 编码：“Shows a bubble chart where the size and the color of the bubble can configured.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
  - 抽象与层级：“1st label in a row will be 1st level in tree map.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Will map every variable from the SPARQL select clause to a formatted table column.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 处理的材料：“Shows the result data as a table.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 对象：“Every column in the result row is mapped to a dimension” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 对象：“Item Node ID” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 对象：“Labels will be appended to current node.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 关系：“row will be nested.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 属性与度量：“Number Bubble Size” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 属性与度量：“End Point in Time” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 视图：“Shows the result data as a grid with images.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 视图：“Shows an interactive graph that allow hierarchically ordering and exploring items.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 编码：“?rgb Color Bubble Color (optional)” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 交互：“Every grid item has a big picture and opens the gallery when clicking on it.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 交互：“It also allows filtering them by selecting an axis fraction.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 交互：“Shows a zoomable tree map.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 交互：“Shows a explorable timeline.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)
- 抽象与层级：“Shows an interactive graph that allow hierarchically ordering and exploring items.” [✓](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help/Result_Views)

</details>
- 没读到：questions

<a id="vowl"></a>

### VOWL / WebVOWL 本体可视化

- 领域：本体与语义网；议题：让不懂本体语言的人也能看懂本体
- 编码：一般图与网络；重点：连通与邻域、关系上的类型与量；把握：证据很少
- 说明：官方站点读不到，只依据期刊页面摘要。
- 编码所依据的原文：
  - 处理的材料：“The Visual Notation for OWL Ontologies (VOWL) is a well-specified visual language for the user-oriented representation of ontologies.” [✓](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0)
  - 对象：“It defines graphical depictions for most elements of the Web Ontology Language (OWL)” [✓](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0)
  - 视图：“that are combined to a force-directed graph layout visualizing the ontology.” [✓](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0)
<details><summary>本案例读到的其他原文摘录</summary>

- 为什么这样画：“In contrast to related work, VOWL aims for an intuitive and comprehensive representation that is also understandable to users less familiar with ontologies.” [✓](https://semantic-web-journal.net/content/visualizing-ontologies-vowl-0)
- 为什么这样画：“VOWL uses a graph visualization, as this is considered an intuitive way to represent the structure of ontologies” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 为什么这样画：“We decided on this approach, as we consider it important to give users a visual impression of the size and topology of the ontology before they start to explore it any further.” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 为什么这样画：“We chose this systematic and modular approach in order to improve the semantics of the visual language and to facilitate its implementation.” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 原来的问题：“A major drawback of these attempts is that they require knowledge about UML.” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 原来的问题：“since UML has been designed for the representation of software rather than knowledge” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 原来的问题：“they do not propose intuitive ontology visualizations that are immediately understandable to casual users.” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 原来的问题：“several of the works implement a stepwise approach of ontology exploration, where only a root class is shown at the beginning and the user has to navigate through the visualization” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 局限与代价：“the nesting direction is not yet displayed in VOWL: A union including an intersection and an intersection including a union look the same and can hence not be immediately distinguished” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 局限与代价：“graph visualizations are only viable up to a certain size, at which the overview is lost and the graph is no longer easily usable.” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 局限与代价：“prevents users from creating a “mental map” of the visualization that remains constant for several sessions” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)
- 局限与代价：“However, it has its limitations and challenges, especially when it comes to the visualization of very large ontologies” [✓](https://www.semantic-web-journal.net/system/files/swj1114.pdf)

</details>
- 没读到：relations；attributes；encodings；interactions；questions；abstraction；官方站点 vowl.visualdataweb.org 域名无法解析（DNS 失败），没读到；WebVOWL 的交互与编码未核对

<a id="kialo"></a>

### Kialo 论证树

- 领域：论证与讨论；议题：把一个论题的赞成与反对理由层层展开，参与者能找到自己该回应的位置
- 编码：命题与论证 + 层级与树；重点：包含与层次、关系上的类型与量；把握：证据很少
- 编码所依据的原文：
  - 视图：“Click the + symbol at the top of the Pros or Cons column.” [✓](https://support.kialo.com/en/hc/creating-a-claim/)
  - 关系：“Linking Claims Between Discussions” [✓](https://support.kialo.com/en/)
  - 抽象与层级：“Marking a Branch Seen” [✓](https://support.kialo.com/en/hc/navigating-the-claim-menu/)
  - 抽象与层级：“Multi- vs Single-Thesis Discussions” [✓](https://support.kialo.com/en/hc/navigating-the-claim-menu/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Enter your claim in the text box.” [✓](https://support.kialo.com/en/hc/creating-a-claim/)
- 对象：“To create a claim in a discussion:” [✓](https://support.kialo.com/en/hc/creating-a-claim/)
- 关系：“Adding a Link” [✓](https://support.kialo.com/en/)
- 交互：“Navigating the Claim Menu” [✓](https://support.kialo.com/en/hc/navigating-the-claim-menu/)
- 交互：“Moving/Linking a Claim” [✓](https://support.kialo.com/en/hc/moving-linking-a-claim/)

</details>
- 没读到：attributes；encodings；questions

<a id="codecity"></a>

### CodeCity

- 领域：软件演化与度量；议题：把软件系统的整体结构一眼看清，找出设计问题的位置
- 编码：层级与树 + 表与多维属性；重点：包含与层次、对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 处理的材料：“Our metaphor depicts software systems as cities in which the buildings represent the classes of the software system, while the city’s districts represent the packages in which the classes are defined.” [✓](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf)
  - 编码：“the number of methods metric for the class is mapped on the building height, the number of attributes on the base size (both width and length).” [✓](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf)
  - 编码：“The nesting level of a package is mapped on the color saturation of the district” [✓](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf)
<details><summary>本案例读到的其他原文摘录</summary>

- 交互：“The elements can be queried using both a generic query language and predefined queries.” [✓](https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2008e.pdf)
- 为什么这样画：“The key point in conceiving a realistic software city is to map the information about the source code in meaningful ways in order to take the approach beyond beautiful pictures.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 为什么这样画：“We claim that to contrast the feeling of disorientation and frustration a good metaphor is needed, because it allows the viewer to embed the visual elements in a familiar context.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 为什么这样画：“A city, with its downtown area and its suburbs is a familiar notion with a clear concept of orientation.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 为什么这样画：“Being able to navigate and interact with a visual representation is a critical feature, since static pictures are limited with respect to expressiveness.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 原来的问题：“this idea is not new, but we claim that it has so far been used at the wrong levels of granularity.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 原来的问题：“This is because they exploit the additional 3rd dimension as yet another visual means to communicate information, quickly leading to information overload, over-plotting, and navigation problems” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 原来的问题：“Using an all too simple visual metaphor (such as a large cube or sphere for the whole system or each package) does not do justice to the complexity of a software system” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 原来的问题：“A more serious problem is the extensive range of building sizes presented simultaneously to the viewer, which according to the gestalt principles [9] is more than one can grasp.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 局限与代价：“We currently do not display the class internals” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 局限与代价：“The drawback is that they cannot be used to compare among cities, because a low value of a metric in one system may be high in another system.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 局限与代价：“Threshold-based mapping overcomes this disadvantage, but requires well-defined thresholds for each metric.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)
- 局限与代价：“However, in cities representing very large systems the interactivity and navigability can be substantially slowed down.” [✓](https://www.si.usi.ch/assets/publications/conf/vissoft/vissoft2007/WettelL07.pdf)

</details>

<a id="hive-plot"></a>

### Hive Plot

- 领域：网络分析（生物与社会网络）；议题：在大型网络里看出趋势和异常，并能比较相关的网络
- 编码：一般图与网络；重点：连通与邻域、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 编码：“Node-to-axis assignment and node-on-axis position are determined solely by network structure” [✓](https://mk.bcgsc.ca/linnet/)
  - 回答的问题：“exposing both trends and outlier patterns in network structure” [✓](https://mk.bcgsc.ca/linnet/)
  - 视图：“Multiple hive plots are presented together in a hive panel” [✓](https://mk.bcgsc.ca/linnet/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“gene regulation, protein-protein interaction, internet traffic, user space in a social network” [✓](https://mk.bcgsc.ca/linnet/)
- 对象：“In a hive plot, nodes are constrained to linear axes and edges are drawn as curves.” [✓](https://mk.bcgsc.ca/linnet/)
- 关系：“Edges are drawn as curved links.” [✓](https://mk.bcgsc.ca/linnet/)
- 属性与度量：“Edges are drawn as Bezier curves, which can be annotated with color, thickness or label to communicate additional information.” [✓](https://mk.bcgsc.ca/linnet/)
- 编码：“Mapping to axis (A, in figure below), position (B) and color (C) can be a function of sink/source status” [✓](https://mk.bcgsc.ca/linnet/)
- 回答的问题：“The purpose of the hive plot is to establish a new baseline for visualization of large networks” [✓](https://mk.bcgsc.ca/linnet/)
- 抽象与层级：“Nodes are mapped to and positioned on radially distributed linear axes” [✓](https://mk.bcgsc.ca/linnet/)
- 抽象与层级：“Multiple hive plots are presented together in a hive panel” [✓](https://mk.bcgsc.ca/linnet/)
- 为什么这样画：“The purpose of the hive plot is to establish a new baseline for visualization of large networks — a method that is both general and tunable and useful as a starting point in visually exploring network structure.” [✓](https://mk.bcgsc.ca/linnet/)
- 为什么这样画：“To rationally visualize networks, we introduce the hive plot. The hive plot is based on meaningful network properties, which can be selected to address a specific question.” [✓](https://mk.bcgsc.ca/linnet/)
- 为什么这样画：“Hive plots make it possible to assess network structure because they are founded on network properties, not on aesthetic layout.” [✓](https://mk.bcgsc.ca/linnet/)
- 为什么这样画：“To understand networks visually, we need to see their structure directly, not by proxy of a layout algorithm based on aesthetics.” [✓](https://mk.bcgsc.ca/linnet/)
- 原来的问题：“Conventional network visualization is unsuitable for visual analytics of large networks.” [✓](https://mk.bcgsc.ca/linnet/)
- 原来的问题：“In a hairball, data is subordinate to layout” [✓](https://mk.bcgsc.ca/linnet/)
- 原来的问题：“The central drawback of hairball-based visualization is that they cannot be tuned to address a user's specific questions.” [✓](https://mk.bcgsc.ca/linnet/)
- 原来的问题：“Nodes on the axes were not ordered. Network edges between the top and bottom layer cross the middle layer axis and complicate the view.” [✓](https://mk.bcgsc.ca/linnet/)
- 局限与代价：“Interpretation of the linear visualization is easy (once you get the hang of it).” [✓](https://mk.bcgsc.ca/linnet/)
- 局限与代价：“The axis and node mapping is arbitrary, and this may sound very abstract at this point.” [✓](https://mk.bcgsc.ca/linnet/)
- 局限与代价：“The method requires that your data be mappable onto a set of pairwise relationships.” [✓](https://mk.bcgsc.ca/linnet/)

</details>
- 没读到：interactions

<a id="gapminder"></a>

### Gapminder 气泡图

- 领域：国际发展统计；议题：看各国在收入、寿命、人口等指标上的关系，以及这种关系怎样随时间变化
- 编码：表与多维属性 + 序列与事件流；重点：对象上的度量、时间与演化、总体分布；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 对象：“Decide what you want to show as bubbles (e.g. countries)” [✓](https://www.gapminder.org/upload-data/motion-chart/)
  - 属性与度量：“The second column is for time (e.g. Years)” [✓](https://www.gapminder.org/upload-data/motion-chart/)
  - 编码：“The area of each bubble corresponds to the number of citizens in the country” [✓](https://www.gapminder.org/data/documentation/gd000/)
  - 编码：“The colors of the bubbles show the four regions” [✓](https://www.gapminder.org/data/documentation/gd000/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Gapminder Tools is free and comes with built-in data.” [✓](https://www.gapminder.org/about/about-gapminder/faq/)
- 处理的材料：“Following columns are for your data (e.g. life expectancy, GDP, population). The value in these columns can be numbers or texts.” [✓](https://www.gapminder.org/upload-data/motion-chart/)
- 属性与度量：“The value in these columns can be numbers or texts.” [✓](https://www.gapminder.org/upload-data/motion-chart/)
- 属性与度量：“Gapminder’s calculations of GDP per capita , in constant PPP dollars with 2021 prices.” [✓](https://www.gapminder.org/data/documentation/gd000/)
- 视图：“Gapminder Tools : our new Bubble Chart and more!” [✓](https://www.gapminder.org/news/gapminder-tools-are-coming/)
- 视图：“The offline version also allows you to create your own animated bubble charts, line charts and so on.” [✓](https://www.gapminder.org/about/about-gapminder/faq/)
- 视图：“For the animated chart, data before 1950 comes from many historic sources” [✓](https://www.gapminder.org/data/documentation/gd000/)
- 编码：“Y-axis: Life expectancy is based on estimates from Global Burden of Disease Study 2023 (GBD 2023) Results” [✓](https://www.gapminder.org/data/documentation/gd000/)
- 编码：“X-axis : Gapminder’s calculations of GDP per capita” [✓](https://www.gapminder.org/data/documentation/gd000/)
- 交互：“It works on mobile devices and supports touch screens” [✓](https://www.gapminder.org/news/gapminder-tools-are-coming/)
- 抽象与层级：“The colors of the bubbles show the four regions” [✓](https://www.gapminder.org/data/documentation/gd000/)
- 为什么这样画：“There has been a market failure in distributing global data.” [✓](https://www.gapminder.org/about/about-gapminder/faq/)
- 为什么这样画：“Gapminder wants to make data more accessible and easier to use for instant visual analysis.” [✓](https://www.gapminder.org/about/about-gapminder/faq/)
- 为什么这样画：“We believe decision makers, politicians as well as education at almost all levels lack adequate tools.” [✓](https://www.gapminder.org/about/about-gapminder/faq/)
- 原来的问题：“Flash is a technology used less and less nowadays, we have no control over it, and we are expecting the old Bubble Chart to become less and less reliable with time.” [✓](https://www.gapminder.org/news/gapminder-tools-are-coming/)
- 局限与代价：“Gapminder Tools is not fully polished yet and may behave strangely or slowly at times.” [✓](https://www.gapminder.org/news/gapminder-tools-are-coming/)
- 局限与代价：“The data in the new version should be exactly the same as in Gapminder World, but there might be differences in how it’s displayed.” [✓](https://www.gapminder.org/news/gapminder-tools-are-coming/)

</details>
- 没读到：relations；questions

<a id="gephi"></a>

### Gephi

- 领域：通用网络分析；议题：探索网络、检验假设、发现复杂关系数据里的模式
- 编码：一般图与网络；重点：连通与邻域、群落与相似、对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 回答的问题：“Gephi helps data analysts explore networks, test hypotheses, and discover meaningful patterns in complex relational data.” [✓](https://gephi.org/desktop/)
  - 编码：“Use ranking or partition data to make meaningful the network representation.” [✓](https://gephi.org/desktop/)
  - 交互：“Use interactive user interface to filter the network in real-time.” [✓](https://gephi.org/desktop/)
  - 关系：“Under the folder “Topology”, you will find all the filters related to the relational structure of the network.” [✓](https://gephi.org/quickstart/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Gephi can read the majority of graph file formats but also supports CSV and databases import.” [✓](https://gephi.org/desktop/)
- 处理的材料：“Gephi can import a variety of standard graph file formats. These include GEXF , GDF, GML, GraphML, Pajek NET, GraphViz DOT, CSV” [✓](https://gephi.org/faq/)
- 处理的材料：“Now that the GEXF has been imported, a network appears in the centre of the “Overview” tab.” [✓](https://gephi.org/quickstart/)
- 对象：“Handle networks with up to 1M nodes and 5M edges” [✓](https://gephi.org/desktop/)
- 对象：“the “Nodes” and “Edges” buttons” [✓](https://gephi.org/quickstart/)
- 关系：“Filter the network to select nodes and/or edges based on the network structure or data.” [✓](https://gephi.org/desktop/)
- 属性与度量：“Under the folder “Attributes”, for example, you will find all the filters operating on the variables saved in the columns of your Data Laboratory.” [✓](https://gephi.org/quickstart/)
- 属性与度量：“Betweenness Centrality, Closeness, Diameter, Clustering Coefficient, PageRank” [✓](https://gephi.org/desktop/)
- 属性与度量：“Use ranking or partition data to make meaningful the network representation.” [✓](https://gephi.org/desktop/)
- 视图：“The “Graph” window at the center of the “Overview” tab is the heart of Gephi.” [✓](https://gephi.org/quickstart/)
- 视图：“The Data Laboratory allows you to view, and if necessary edit, your data in tabular format.” [✓](https://gephi.org/quickstart/)
- 视图：“The vectorial based preview rendering lets you put the final touch and care about aesthetics before explorting in SVG , PNG or PDF.” [✓](https://gephi.org/desktop/)
- 编码：“Customize colors, size or labels to bring sense to the network representation.” [✓](https://gephi.org/desktop/)
- 交互：“Drag and drop nodes” [✓](https://gephi.org/desktop/)
- 交互：“Highlight neighbors” [✓](https://gephi.org/desktop/)
- 交互：“The Layout module enables real-time adjustment of layout settings” [✓](https://gephi.org/desktop/)
- 回答的问题：“to explore, manipulate, and understand complex networks” [✓](https://gephi.org/desktop/)
- 回答的问题：“Gephi Quickstart: Visualize and Analyze Your First Network” [✓](https://gephi.org/quickstart/)
- 抽象与层级：“Community detection (Modularity)” [✓](https://gephi.org/desktop/)

</details>

<a id="treemap-diskspace"></a>

### Treemap（磁盘空间）

- 领域：文件系统与资源占用；议题：看谁占用了最多的磁盘空间，哪里有大块或重复的目录
- 编码：层级与树；重点：包含与层次、总体分布、对象上的度量；把握：官方页面直接写了
- 编码所依据的原文：
  - 处理的材料：“I became obsessed with the idea of producing a compact visualization of directory tree structures.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
  - 编码：“Showing file size by area coding seemed appealing” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
  - 编码：“a more comprehensible design used a border to show the nesting” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
  - 抽象与层级：“Aggregate the Lower Levels of the Tree” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“I've visualized the same files here (the source for linux 4.9.-rc5) in different ways” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)
- 对象：“It is very effective in showing attributes of leaf nodes using size and color coding.” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 对象：“The capacity to see tens of thousands of nodes in a fixed space” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 关系：“Treemap is a space-constrained visualization of hierarchical structures.” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 关系：“Treemap enables users to compare nodes and sub-trees even at varying depth in the tree” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 关系：“the term 'treemap' described the notion of turning a tree into a planar space-filling map.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 属性与度量：“Color, size and label attribute” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 属性与度量：“Color Setting and Binning for Numerical Attributes” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 属性与度量：“encoding a linear variable such as file size as an area” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 视图：“Ordered and Quantum Treemaps: Making Effective Use of 2D Space to Display Hierarchies” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 视图：“Choose layout algorithm” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 视图：“An advantage to all tree maps is that we can more easily use vertical space.” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)
- 编码：“It is very effective in showing attributes of leaf nodes using size and color coding.” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 交互：“Zooming in and out, showing details of a node, showing the path” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 交互：“Filter with Dynamic Query Sliders” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 交互：“cursoring over the boxes produced the exact file size on the bottom of the display” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 交互：“Aggregate the Lower Levels of the Tree” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 回答的问题：“determining which users consumed the largest shares of disk space were difficult tasks” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 回答的问题：“The capacity to see tens of thousands of nodes in a fixed space and find large areas or duplicate directories is very powerful.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 回答的问题：“Treemap enables users to compare nodes and sub-trees even at varying depth in the tree, and help them spot patterns and exceptions.” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 回答的问题：“showing how they can visualize where disk space is consumed” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)
- 抽象与层级：“Treemap enables users to compare nodes and sub-trees even at varying depth in the tree” [✓](https://www.cs.umd.edu/projects/hcil/treemap/index.shtml)
- 抽象与层级：“a more comprehensible design used a border to show the nesting” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 抽象与层级：“Focusing on areas of interest” [✓](https://www.cs.umd.edu/projects/hcil/treemap/doc4.1/toc.html)
- 为什么这样画：“During 1990, in response to the common problem of a filled hard disk, I became obsessed with the idea of producing a compact visualization of directory tree structures.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 为什么这样画：“splitting the screen into rectangles in alternating horizontal and vertical directions as you traverse down the levels” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 为什么这样画：“The capacity to see tens of thousands of nodes in a fixed space and find large areas or duplicate directories is very powerful.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 为什么这样画：“My initial design simply nested the rectangles, but a more comprehensible design used a border to show the nesting.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 原来的问题：“Tree structured node-link diagrams grew too large to be useful, so I explored ways to show a tree in a space-constrained layout.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 原来的问题：“I rejected strategies that left blank spaces or those that dealt with only fixed levels or fixed branching factors.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 原来的问题：“Showing file size by area coding seemed appealing, but various rectangular, triangular, and circular strategies all had problems.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 局限与代价：“It does take some learning for novices to grasp the tree structure layout in treemaps, but the benefits are great.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 局限与代价：“We knew that encoding a linear variable such as file size as an area was breaking a graphic design guideline” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 局限与代价：“We also knew that visually comparing long narrow rectangles to squarish ones was problematic” [✓](https://www.cs.umd.edu/hcil/treemap-history/)
- 局限与代价：“We struggled to deal with the problem of many small files in some directories, but wound up showing only a blackened area that invited closer examination by zooming.” [✓](https://www.cs.umd.edu/hcil/treemap-history/)

</details>

<a id="git-history"></a>

### Git 提交历史

- 领域：版本控制；议题：回看发生过什么，分支怎样分叉与合并
- 编码：有向无环图；重点：先后与依赖方向、时间与演化；把握：官方页面直接写了
- 编码所依据的原文：
  - 关系：“pointers to the commit or commits that directly came before this commit (its parent or parents)” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
  - 视图：“--graph Display an ASCII graph of the branch and merge history beside the log output.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
  - 视图：“By default, with no arguments, git log lists the commits made in that repository in reverse chronological order” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
  - 抽象与层级：“a series of summarizing options with git log” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Git doesn’t store data as a series of changesets or differences, but instead as a series of snapshots” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 处理的材料：“if you have cloned a repository with an existing commit history” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 对象：“Git then creates a commit object that has the metadata and a pointer to the root project tree” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 对象：“one tree that lists the contents of the directory and specifies which file names are stored as which blobs” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 对象：“A branch in Git is simply a lightweight movable pointer to one of these commits.” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 关系：“the next commit stores a pointer to the commit that came immediately before it” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 关系：“Git creates a new snapshot that results from this three-way merge and automatically creates a new commit that points to it.” [✓](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- 属性与度量：“This object also contains the author’s name and email address, the message that you typed” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 属性与度量：“--relative-date Display the date in a relative format (for example, “2 weeks ago”) instead of using the full date format.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 属性与度量：“--stat Show statistics for files modified in each commit.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 视图：“The oneline value for this option prints each commit on a single line” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 视图：“Figure 10. Commits and their parents” [✓](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- 编码：“that is, the most recent commits show up first” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 交互：“To create a new branch and switch to it at the same time, you can run the git checkout command with the -b switch” [✓](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- 交互：“Show only the last n commits.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 交互：“Limit the commits to those made after the specified date.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 交互：“Show commits in an alternate format.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 回答的问题：“you’ll probably want to look back to see what has happened” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 回答的问题：“this command gets the list of commits made in the last two weeks” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 抽象与层级：“--shortstat Display only the changed/insertions/deletions line from the --stat command.” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- 抽象与层级：“The oneline value for this option prints each commit on a single line” [✓](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)

</details>

<a id="flame-graph"></a>

### 火焰图

- 领域：性能剖析；议题：找出最频繁的代码路径
- 编码：层级与树；重点：包含与层次、总体分布；把握：官方页面直接写了
- 说明：同一个官方页面还讲到“火焰图表”（flame chart）：把时间放在 x 轴——这是同一批栈数据换了重点部分后的另一种视图。
- 编码所依据的原文：
  - 编码：“The x-axis shows the stack profile population, sorted alphabetically (it is not the passage of time)” [✓](https://www.brendangregg.com/flamegraphs.html)
  - 编码：“The wider a frame is is, the more often it was present in the stacks.” [✓](https://www.brendangregg.com/flamegraphs.html)
  - 抽象与层级：“Flame graphs reorder the x-axis samples alphabetically, which maximizes frame merging” [✓](https://www.brendangregg.com/flamegraphs.html)
  - 回答的问题：“so that the most frequent code-paths can be identified quickly and accurately” [✓](https://www.brendangregg.com/flamegraphs.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“a visualization of hierarchical data that I created to visualize stack traces of profiled software” [✓](https://www.brendangregg.com/flamegraphs.html)
- 处理的材料：“./flamegraph.pl --colors=java out.profile-folded > profile.svg” [✓](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)
- 处理的材料：“The flame graph visualization works for any stack trace plus value combination” [✓](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)
- 对象：“Each rectangle represents a stack frame.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 关系：“The top edge shows what is on-CPU, and beneath it is its ancestry.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 关系：“The flame graph visualization is really an adjacency diagram with an inverted icicle layout” [✓](https://www.brendangregg.com/flamegraphs.html)
- 属性与度量：“The width of the box shows the total time it was on-CPU or part of an ancestry that was on-CPU (based on sample count).” [✓](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)
- 属性与度量：“The sample count can exceed elapsed time if multiple threads were running and sampled concurrently.” [✓](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)
- 属性与度量：“This samples at 99 Hertz (-F 99)” [✓](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)
- 视图：“Flame graphs are both a static and dynamic visualization.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 视图：“Icicle charts are flame graphs upside down.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 视图：“flame charts put the passage of time on the x-axis instead of the alphabet” [✓](https://www.brendangregg.com/flamegraphs.html)
- 视图：“Sunburst layout using radial coordinates for the x-axis, a flame graph can be turned into a hierarchical pie chart.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 编码：“the y-axis shows stack depth, counting from zero at the bottom” [✓](https://www.brendangregg.com/flamegraphs.html)
- 编码：“The colors aren't significant, and are usually picked at random to be warm colors” [✓](https://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)
- 交互：“Mouse hover shows additional frame details in a status bar.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 交互：“Mouse click zooms the visualization horizontally, revealing function names previously elided.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 交互：“Search matches and highlights a given term and shows the "cumulative percentage" of stacks including the search term.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 交互：“A dynamic visualization allows interactive features to aid navigation and comprehension” [✓](https://www.brendangregg.com/flamegraphs.html)
- 回答的问题：“showing how they can visualize where disk space is consumed” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)
- 抽象与层级：“only the most frequent frames have enough width for labels” [✓](https://www.brendangregg.com/flamegraphs.html)
- 为什么这样画：“a visualization of hierarchical data that I created to visualize stack traces of profiled software so that the most frequent code-paths can be identified quickly and accurately.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 为什么这样画：“Flame graphs reorder the x-axis samples alphabetically, which maximizes frame merging, and better shows the big picture of the profile.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 为什么这样画：“As a static visualization, a flame graph can be saved as an image, included in print (books)” [✓](https://www.brendangregg.com/flamegraphs.html)
- 为什么这样画：“I switched to timed sampling (profiling) to solve the overhead problem, but since the function flow is no longer known (sampling has gaps) I ditched time on the x-axis” [✓](https://www.brendangregg.com/flamegraphs.html)
- 原来的问题：“The regular profilers/tracers had produced walls of text, so I was exploring visualizations.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 原来的问题：“the overhead of function tracing was too high, perturbing the target, and the final visualization was too dense to read when spanning multiple seconds.” [✓](https://www.brendangregg.com/flamegraphs.html)
- 原来的问题：“Not those big picture details (drivers 50%, etc).” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)
- 原来的问题：“The problem is that to understand this correctly requires the comparison of angles, instead of lengths or areas, which has been evaluated as a more difficult perceptive task.” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)
- 局限与代价：“The x-axis shows the stack profile population, sorted alphabetically (it is not the passage of time)” [✓](https://www.brendangregg.com/flamegraphs.html)
- 局限与代价：“But for very deep stacks the flame graph layout (with a GUI that starts at the top) often means the initial view may be mostly empty” [✓](https://www.brendangregg.com/flamegraphs.html)
- 局限与代价：“Many small rectangles are too thin to label, and, they also matter less overall.” [✓](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)

</details>

<a id="dsm"></a>

### 设计结构矩阵 DSM

- 领域：工程系统与产品架构；议题：看清一个系统里元素之间的依赖，决定怎样分组与排序（团队、模块、先后）
- 编码：一般图与网络；重点：先后与依赖方向、环与反馈、群落与相似；把握：官方页面直接写了
- 编码所依据的原文：
  - 编码：“Looking down any column of the matrix shows all of the inputs to the element in that column” [✓](https://dsmweb.org/reading-a-dsm/)
  - 交互：“Sequencing is the reordering of the DSM rows and columns such that the new DSM arrangement does not contain any feedback marks” [✓](https://dsmweb.org/sequencing-a-dsm/)
  - 交互：“finding subsets of DSM elements (i.e. clusters or modules) that are mutually exclusive or minimally interacting subsets” [✓](https://dsmweb.org/clustering-a-dsm/)
  - 抽象与层级：“A DSM always only contains elements from one domain.” [✓](https://dsmweb.org/different-dsm-types/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Basically, the type of the elements and dependencies needs to be defined as precisely as possible to obtain the information structure for the DSM.” [✓](https://dsmweb.org/different-dsm-types/)
- 处理的材料：“From a structural point of view, a system can be disentangled down to a network-like model of entities and their relations.” [✓](https://dsmweb.org/different-dsm-types/)
- 对象：“The cells along the diagonal of the matrix represent the system elements.” [✓](https://dsmweb.org/reading-a-dsm/)
- 对象：“the term “element” is used to refer to an entity that is entered into a row or a column” [✓](https://dsmweb.org/different-dsm-types/)
- 对象：“Each kind of entities represents a specific view to the system, called “domain”.” [✓](https://dsmweb.org/different-dsm-types/)
- 关系：““relation” refers to any kind of connection or association between two entities, may they be directed or not” [✓](https://dsmweb.org/different-dsm-types/)
- 关系：“a dependency often implies a direction as element A will depend on element B” [✓](https://dsmweb.org/different-dsm-types/)
- 关系：“The sources and destinations of these input and output interactions are identified by marks in the off-diagonal cells.” [✓](https://dsmweb.org/reading-a-dsm/)
- 关系：“The relationship type therefore defines the kind of dependency between two elements.” [✓](https://dsmweb.org/different-dsm-types/)
- 属性与度量：“such as the number of interactions and/or the importance, impact, or strength of each” [✓](https://dsmweb.org/reading-a-dsm/)
- 属性与度量：“to describe, for example, the type, owner, or status of each element.” [✓](https://dsmweb.org/reading-a-dsm/)
- 属性与度量：“Additional attributes of the interactions, such as their names, requirements, etc.” [✓](https://dsmweb.org/reading-a-dsm/)
- 视图：“The matrix provides a highly compact, easily scalable, and intuitively readable representation of a system architecture.” [✓](https://dsmweb.org/reading-a-dsm/)
- 视图：“node-directed link diagram equivalents of portions of the DSM” [✓](https://dsmweb.org/reading-a-dsm/)
- 编码：“Examining any row in the matrix reveals all of the outputs from the element in that row” [✓](https://dsmweb.org/reading-a-dsm/)
- 编码：“a mark in an off-diagonal cell (e.g., cell 3,5) represents an interaction that is both an input and an output” [✓](https://dsmweb.org/reading-a-dsm/)
- 编码：“Banding is the addition of alternating light and dark bands to a DSM to show independent (i.e. parallel or concurrent) activities” [✓](https://dsmweb.org/banding-a-dsm/)
- 回答的问题：“If we were to form several development teams within this project, what will be the number of teams required and the membership of each team?” [✓](https://dsmweb.org/clustering-a-dsm/)
- 回答的问题：“it is possible to learn about what elements of the system might possibly have to be reworked” [✓](https://dsmweb.org/sequencing-a-dsm/)
- 抽象与层级：“The term “domain” can therefore be defined as one specific view (among several) on one complex system at a time.” [✓](https://dsmweb.org/different-dsm-types/)
- 抽象与层级：“The collection of bands or levels within a DSM constitute the critical path of the system or project.” [✓](https://dsmweb.org/banding-a-dsm/)
- 抽象与层级：“clusters absorb most, if not all, of the interactions (i.e. DSM marks) internally” [✓](https://dsmweb.org/clustering-a-dsm/)
- 为什么这样画：“The matrix provides a highly compact, easily scalable, and intuitively readable representation of a system architecture.” [✓](https://dsmweb.org/reading-a-dsm/)
- 为什么这样画：“There is no pre-defined DSM that is helpful for any problem that is to be structured. Rather, DSM needs to be adapted to the kinds of elements and relations that prevail in the system in focus.” [✓](https://dsmweb.org/different-dsm-types/)
- 为什么这样画：“The purpose of a domain, which is comparable to a “class” of objects in object-oriented programming paradigms, is to create “homogeneous networks”” [✓](https://dsmweb.org/different-dsm-types/)
- 为什么这样画：“It is important that a DSM contains only one relationship type, as only then the analyses will make sense.” [✓](https://dsmweb.org/different-dsm-types/)
- 原来的问题：“However, if many such kinds are mixed, the network is incoherent.” [✓](https://dsmweb.org/different-dsm-types/)
- 原来的问题：“For complex engineering systems, it is highly unlikely that simple row and column manipulation will result in an upper triangular form.” [✓](https://dsmweb.org/sequencing-a-dsm/)
- 原来的问题：“comprehensive feedback loops of larger structures cannot be analyzed by this approach” [✓](https://dsmweb.org/sequencing-a-dsm/)
- 原来的问题：“Furthermore, this approach does not always permit the length and quantity of the existing feedback loops to be acquired.” [✓](https://dsmweb.org/sequencing-a-dsm/)
- 局限与代价：“DSM models using simple binary representations display the existence of a dependency between two tasks without providing additional information on the nature of the interaction.” [✓](https://dsmweb.org/different-dsm-types/)
- 局限与代价：“A DSM always only contains elements from one domain.” [✓](https://dsmweb.org/different-dsm-types/)
- 局限与代价：“Additional attributes of the interactions, such as their names, requirements, etc. are usually kept in separate repositories but may be linked to the DSM cells by numerical identification numbers or indices.” [✓](https://dsmweb.org/reading-a-dsm/)

</details>

<a id="genealogical-graphs"></a>

### 家谱图的交互可视化

- 领域：谱系与家族史；议题：在家谱里按自己的关系去探索，不迷路
- 编码：有向无环图；重点：连通与邻域、包含与层次；把握：证据很少
- 说明：证据来自课程幻灯片对论文的转述，没读到论文原文。
- 编码所依据的原文：
  - 处理的材料：“single person has tree of ancestors, tree of descendants” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
  - 抽象与层级：“Dual trees abstraction” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
  - 抽象与层级：“topological navigation via collapse/expand on selection” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Interactive visualization of genealogical graphs” [✓](https://espace2.etsmtl.ca/id/eprint/22387)
- 对象：“no crossings, nodes ordered by generation” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 关系：“Another example • vertical connection • horizontal connection” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 属性与度量：“no spatial ordering for generations” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 视图：“rooted trees: standard layouts” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 视图：“free trees” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 视图：“Indented, flipped, combined” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 编码：“no crossings, nodes ordered by generation” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 交互：“topological navigation via collapse/expand on selection” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 交互：“preview dots: expand if collapsed” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 交互：“popup marking menu” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 交互：“Interaction as fundamental to design” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 回答的问题：“explore canonical subsets and combinations, easy to interpret, scales well” [✓](https://www.cs.ubc.ca/~tmm/courses/grad/slides/week8.pdf)
- 为什么这样画：“This motivates some novel graphical representations, including one based on a dual-tree, a subgraph formed by the union of two trees.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 为什么这样画：“convinced us to focus on visualizing only a subset of the graph at a time, and therefore to identify which subset might be best.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 为什么这样画：“Because a dual-tree diagram consists of only 2 trees, it can be drawn in a straight-forward manner, and may prove to be easy to understand and interpret.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 为什么这样画：“it scales relatively well, since the crowding of nodes within it is no worse than the crowding that occurs in individual trees.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 原来的问题：“In an hourglass diagram of A(x) ∪ D(x), the choice of x is a tradeoff between the number of ancestors and number of descendants revealed” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 原来的问题：“conventional charts of large, extended families inevitably contain at least some long edges or nodes displaced far away from their close relatives, to make room for other nodes” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 原来的问题：“Although such diagrams are much simpler looking than traditional ones, they ultimately suffer from the same exponential crowding (see § 3.4).” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 原来的问题：“Although the novel representations in Figures 7 and 9 are interesting, they do not order nodes by generation. Their unfamiliarity might also make them difficult to interpret for many users.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 局限与代价：“Dual-trees can show many generations vertically, but have a horizontal extent limited to ancestors or descendants of 2 root nodes.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 局限与代价：“Although these roots can be changed interactively to traverse a data set, only a fraction of a large data set may be visible at any given time.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 局限与代价：“Such rotations generally require that certain other nodes be collapsed, to maintain the dual-tree scheme.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)
- 局限与代价：“The user mentioned the lack of a symbol explicitly linking spouses, which is shown in conventional diagrams.” [✓](https://www.dgp.toronto.edu/~mjmcguff/research/genealogyVis/genealogyVis.pdf)

</details>
- 没读到：encodings（只有位置相关一条，颜色、线型、大小未写）；attributes（只有 generation 一条）

<a id="universal-dependencies"></a>

### Universal Dependencies 依存树

- 领域：语言学；议题：用同一套标注描述多种语言的句子结构，方便比较和训练解析器
- 编码：层级与树；重点：关系上的类型与量、包含与层次；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 关系：“HEAD: Head of the current word, which is either a value of ID or zero (0).” [✓](https://universaldependencies.org/format.html)
  - 关系：“DEPREL: Universal dependency relation to the HEAD ( root iff HEAD = 0)” [✓](https://universaldependencies.org/format.html)
  - 关系：“DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.” [✓](https://universaldependencies.org/format.html)
  - 抽象与层级：“propose a universal inventory of categories and guidelines” [✓](https://universaldependencies.org/introduction.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“treebanks, collections of sentences annotated for word morphology and sentence syntax, for many languages” [✓](https://universaldependencies.org/introduction.html)
- 处理的材料：“We use a revised version of the CoNLL-X format called CoNLL-U. Annotations are encoded in plain text files” [✓](https://universaldependencies.org/format.html)
- 对象：“organizes sentence analysis around identifying clauses, nominals, and modifiers of these” [✓](https://universaldependencies.org/introduction.html)
- 对象：“Word lines containing the annotation of a word/token/node in 10 fields separated by single tab characters” [✓](https://universaldependencies.org/format.html)
- 关系：“UD adopts a dependency representation of syntax, marking dependents of head words” [✓](https://universaldependencies.org/introduction.html)
- 属性与度量：“UPOS: Universal part-of-speech tag” [✓](https://universaldependencies.org/format.html)
- 属性与度量：“FEATS: List of morphological features from the universal feature inventory” [✓](https://universaldependencies.org/format.html)
- 属性与度量：“MISC: Any other annotation.” [✓](https://universaldependencies.org/format.html)
- 视图：“There is also a simple JavaScript-based CoNLL-U file viewer” [✓](https://universaldependencies.org/format.html)
- 编码：“The main grammatical relations shown in blue (involving a passive verb, a nominal subject and an oblique agent)” [✓](https://universaldependencies.org/introduction.html)
- 回答的问题：“with the goal of facilitating multilingual parser development, language analysis, psycholinguistics, and language typology” [✓](https://universaldependencies.org/introduction.html)
- 回答的问题：“UD must be suitable for computer parsing with high accuracy.” [✓](https://universaldependencies.org/introduction.html)
- 抽象与层级：“using language-specific extensions when necessary” [✓](https://universaldependencies.org/introduction.html)
- 抽象与层级：“or a defined language-specific subtype of one” [✓](https://universaldependencies.org/format.html)

</details>
- 没读到：interactions（页面未写交互操作，只写了查看器）

<a id="cmaptools"></a>

### CmapTools 概念图

- 领域：教育与知识建模；议题：围绕一个焦点问题组织并表示知识，发现概念之间的跨联
- 编码：命题与论证 + 层级与树；重点：包含与层次、连通与邻域、关系上的类型与量；把握：官方页面直接写了
- 说明：这个案例里最关键的一条：层级“依赖于使用知识的情境”，所以要有焦点问题。
- 编码所依据的原文：
  - 回答的问题：“construct concept maps with reference to some particular question we seek to answer, which we have called a focus question” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
  - 关系：“the inclusion of cross-links. These are relationships or links between concepts in different segments or domains of the concept map.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
  - 编码：“the concepts are represented in a hierarchical fashion with the most inclusive, most general concepts at the top of the map” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
  - 关系：“Words on the line, referred to as linking words or linking phrases, specify the relationship between the two concepts.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“construct, navigate, share and criticize knowledge models represented as concept maps” [✓](https://cmap.ihmc.us/)
- 处理的材料：“We define concept as a perceived regularity in events or objects, or records of events or objects, designated by a label.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 对象：“They include concepts, usually enclosed in circles or boxes of some type” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 对象：“Propositions contain two or more concepts connected using linking words or phrases to form a meaningful statement.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 对象：“specific examples of events or objects that help to clarify the meaning of a given concept” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 关系：“relationships between concepts indicated by a connecting line linking two concepts” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 属性与度量：“the most inclusive, most general concepts at the top of the map” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 视图：“Concept maps are graphical tools for organizing and representing knowledge in an organized fashion.” [✓](https://cmap.ihmc.us/)
- 视图：“Concept Map about Concept Maps” [✓](https://cmap.ihmc.us/docs/learn.php)
- 编码：“Concept maps tend to be read progressing from the top downward.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 编码：“Normally these are not included in ovals or boxes, since they are specific events or objects and do not represent concepts.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 交互：“click on the icons underneath the concepts to display a list of links to relevant resources” [✓](https://cmap.ihmc.us/docs/learn.php)
- 交互：“It empowers users to construct, navigate, share and criticize knowledge models represented as concept maps.” [✓](https://cmap.ihmc.us/)
- 回答的问题：“Why the Focus Question?” [✓](https://cmap.ihmc.us/docs/learn.php)
- 回答的问题：“Learn what concept maps are, how to construct them, and use them.” [✓](https://cmap.ihmc.us/)
- 抽象与层级：“the concepts are represented in a hierarchical fashion with the most inclusive, most general concepts at the top of the map” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 抽象与层级：“relationships or links between concepts in different segments or domains of the concept map” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 为什么这样画：“Concept maps are graphical tools for organizing and representing knowledge.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 为什么这样画：“Therefore, it is best to construct concept maps with reference to some particular question we seek to answer, which we have called a focus question.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 为什么这样画：“There are two features of concept maps that are important in the facilitation of creative thinking: the hierarchical structure that is represented in a good map and the ability to search for and characterize new cross-links.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 为什么这样画：“In the creation of new knowledge, cross-links often represent creative leaps on the part of the knowledge producer.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 原来的问题：“Typical objective tests seldom require more than rote learning” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 原来的问题：“Rote learning contributes very little at best to our knowledge structures, and therefore cannot underlie creative thinking or novel problem solving.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 原来的问题：“one should avoid “sentences in the boxes”, that is, full sentences used as concepts, since this usually indicates that a whole subsection of the map could be constructed from the statement in the box.” [？](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 原来的问题：““String maps” illustrate either poor understanding of the material or an inadequate restructuring of the map.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 局限与代价：“although it may somewhat limit the creativity of the student in selecting the concepts to include” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)
- 局限与代价：“As with any tool, it can also be misused, and we have illustrated some examples of this.” [✓](https://cmap.ihmc.us/Publications/ResearchPapers/TheoryUnderlyingConceptMaps.pdf)

</details>
- 没读到：attributes（除概括程度外未写具体属性或度量）

<a id="wikipedia-summary-style"></a>

### Wikipedia 摘要式写作

- 领域：百科写作；议题：一个大主题的文章太长，如何拆分又不让读者迷路
- 编码：层级与树；重点：包含与层次、跨视图的同一对象；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“Wikipedia articles cover topics at several levels of detail” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
  - 关系：“The original article should contain a section with a summary of the subtopic's article as well as a link to it, or an excerpt of it.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
  - 关系：“It also contains a link back to the parent article” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
  - 交互：“Templates are available to link to subtopics and to tag synchronization problems between a summary section and the article it summarizes.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Sections of long articles should be spun off into their own articles, leaving summaries in their place.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 处理的材料：“Wikipedia articles cannot be of indefinite length as very long articles would cause problems and should be split” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 对象：“Each subtopic or child article is a complete encyclopedic article in its own right” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 对象：“The original article should contain a section with a summary of the subtopic's article as well as a link to it, or an excerpt of it.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 对象：“contains its own lead section that is quite similar to the summary in its parent article” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 关系：“Summary sections link to the detailed article with a { { Main } } template.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 属性与度量：“The length of a given Wikipedia article tends to grow as people add information to it.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 属性与度量：“Articles should be neither too large nor too small.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Article_size)
- 属性与度量：“Opinions vary as to what counts as an ideal length” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 交互：“it only takes a click for readers to switch between articles” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 回答的问题：“Sections of long articles should be spun off into their own articles, leaving summaries in their place.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 回答的问题：“It is advisable to develop new material in a subtopic article before summarizing it in the parent article.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 抽象与层级：“each major subtopic is detailed in its own section of the article” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 抽象与层级：“A fuller treatment of any major subtopic should go in a separate article of its own.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 抽象与层级：“leaving summaries in their place” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 为什么这样画：“Summary style keeps the reader from being overwhelmed by too much information up front, by summarizing main points and going into more details on particular points (subtopics) in separate articles.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 为什么这样画：“Summary style is based on the premise that information about a topic need not all be contained in a single article since different readers have different needs:” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 为什么这样画：“This type of organization is made possible because Wikipedia is an online encyclopedia: unlike traditional paper encyclopedias, it only takes a click for readers to switch between articles” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 为什么这样画：“Ordering sections in this way is important because many readers will not finish reading the article.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 原来的问题：“Articles over a certain size might not cover their topic in a way that is easy to find or read.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 原来的问题：“This is more helpful to the reader than a very long article that just keeps growing, eventually reaching book length.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 原来的问题：“Wikipedia articles cannot be of indefinite length as very long articles would cause problems and should be split.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 局限与代价：“If the child article changes considerably without updating the parent article, the summary of the child article in the parent article will need to be rewritten to do it justice.” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 局限与代价：“In applying summary style to articles, care must be taken to avoid a point of view fork” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 局限与代价：“However, certain types of content can be difficult to write neutrally in independent articles, such as "Criticism of..." articles” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)
- 局限与代价：“If only a few sentences could be written and supported by sources about the subject, that subject does not qualify for a separate article” [✓](https://en.wikipedia.org/wiki/Wikipedia:Summary_style)

</details>
- 没读到：views（页面未写视图形式）；encodings（页面未写视觉编码）

<a id="explorable-explanations"></a>

### Explorable Explanations

- 领域：交互式写作；议题：让读者不只读结论，还能改动前提看后果
- 编码：因果与反馈；重点：关系上的类型与量、对象上的度量；把握：页面信息支持，归类靠推断
- 编码所依据的原文：
  - 关系：“The reader can play with the premise and assumptions of various claims, and see the consequences update immediately.” [✓](https://worrydream.com/ExplorableExplanations/)
  - 抽象与层级：“It can be read at multiple levels, depending on the reader's level of interest.” [✓](https://worrydream.com/ExplorableExplanations/)
  - 抽象与层级：“Contextual information allows the reader to learn related material just-in-time” [✓](https://worrydream.com/ExplorableExplanations/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“The reactive document integrates spreadsheet-like models into authored text.” [✓](https://worrydream.com/ExplorableExplanations/)
- 处理的材料：“A reactive document requires the author to disclose the models behind their argument, to open them up for scrutiny.” [✓](https://worrydream.com/ExplorableExplanations/)
- 处理的材料：“Below is a simplified digital adaptation of the analog state variable filter.” [✓](https://worrydream.com/ExplorableExplanations/)
- 对象：“Mouse over a claim to see an analysis.” [✓](https://worrydream.com/TenBrighterIdeas/)
- 对象：“The reader can play with the premise and assumptions of various claims” [✓](https://worrydream.com/ExplorableExplanations/)
- 对象：“It is merely a dataset and model; it cannot be read.” [✓](https://worrydream.com/ExplorableExplanations/)
- 关系：“Notice how the consequences of your adjustments are reflected in the following paragraph.” [✓](https://worrydream.com/ExplorableExplanations/)
- 属性与度量：“F c (cutoff frequency) and Q (resonance) are controlled by independent coefficients” [✓](https://worrydream.com/ExplorableExplanations/)
- 属性与度量：“Computer device # (millions) off power laptop W desktop W CRT display W LCD display W” [✓](https://worrydream.com/TenBrighterIdeas/)
- 属性与度量：“Millions of households with: someone home all day no one home all day 1 member 2 members 3 members 4 members 5+ members” [✓](https://worrydream.com/TenBrighterIdeas/)
- 视图：“Ten Brighter Ideas was my early prototype of a reactive document.” [✓](https://worrydream.com/ExplorableExplanations/)
- 视图：“v_powerPlants draws a grid of little power plants.” [✓](https://worrydream.com/TenBrighterIdeas/)
- 视图：“sector TWh % residential (before) residential (after) commercial manufacturing other total” [✓](https://worrydream.com/TenBrighterIdeas/)
- 交互：“Edit the source code of this analysis.” [✓](https://worrydream.com/TenBrighterIdeas/)
- 交互：“Some parts of the analysis above are underlined -- try adjusting them” [✓](https://worrydream.com/ExplorableExplanations/)
- 交互：“Your readers can interactively explore possibilities, play with parameters, and see the document update immediately.” [✓](https://worrydream.com/Tangle/)
- 交互：“Instead, the reader simply nudges the examples that the author has already presented.” [✓](https://worrydream.com/ExplorableExplanations/)
- 回答的问题：“The reader can explore alternative scenarios, understand the tradeoffs involved, and come to a more confident conclusion” [✓](https://worrydream.com/ExplorableExplanations/)
- 回答的问题：“Is this a good proposition? It's hard to evaluate without context.” [✓](https://worrydream.com/ExplorableExplanations/)
- 回答的问题：“Why $18? What if the tax were more or less?” [✓](https://worrydream.com/ExplorableExplanations/)
- 抽象与层级：“An explorable example makes the abstract concrete, and allows the reader to develop an intuition for how a system works.” [✓](https://worrydream.com/ExplorableExplanations/)
- 为什么这样画：“The goal is to change people's relationship with text. People currently think of text as information to be consumed. I want text to be used as an environment to think in.” [✓](https://worrydream.com/ExplorableExplanations/)
- 为什么这样画：“An explorable example makes the abstract concrete, and allows the reader to develop an intuition for how a system works.” [✓](https://worrydream.com/ExplorableExplanations/)
- 为什么这样画：“Instead, the impulse response of the actual filter is simulated, and its FFT is shown. I think this is more honest, and would work even if we allowed the reader to change the filter topology.” [✓](https://worrydream.com/ExplorableExplanations/)
- 为什么这样画：“The primary point of this example -- the reason I call it an "explorable explanation" -- is the subtlety with which the explorable is integrated with the explanation.” [✓](https://worrydream.com/ExplorableExplanations/)
- 原来的问题：“A typical reading tool, such as a book or website, displays the author's argument, and nothing else. The reader's line of thought remains internal and invisible, vague and speculative.” [✓](https://worrydream.com/ExplorableExplanations/)
- 原来的问题：“But a spreadsheet is not an explanation. It is merely a dataset and model; it cannot be read.” [✓](https://worrydream.com/ExplorableExplanations/)
- 原来的问题：“Most interactive widgets dump the user in a sandbox and say "figure it out for yourself". Those are not explanations.” [✓](https://worrydream.com/ExplorableExplanations/)
- 原来的问题：“But we care about the filter's dynamic behavior -- how the response changes as we vary the parameters F c and Q -- and two static examples give us little insight.” [✓](https://worrydream.com/ExplorableExplanations/)
- 局限与代价：“It's tempting to be impressed by the novelty of an interactive widget such as this, but the interactivity itself is not really the point.” [✓](https://worrydream.com/ExplorableExplanations/)
- 局限与代价：“Dishonest authors will always exist. They might use models based on faulty reasoning or data, but transparency means that the faulty model is available to be examined and refuted.” [✓](https://worrydream.com/ExplorableExplanations/)
- 局限与代价：“However, almost all of these articles are pedagogical, and that's not really what I was going for here.” [✓](https://worrydream.com/ExplorableExplanations/)

</details>
- 没读到：encodings

<a id="ladder-of-abstraction"></a>

### Up and Down the Ladder of Abstraction

- 领域：交互式写作与抽象；议题：通过在不同抽象层之间上下移动，理解一个系统的行为
- 编码：序列与事件流 + 因果与反馈；重点：时间与演化、对象上的度量、总体分布；把握：官方页面直接写了
- 编码所依据的原文：
  - 抽象与层级：“when creating abstractions, stepping down is as important as stepping up.” [✓](https://worrydream.com/LadderOfAbstraction/)
  - 抽象与层级：“The purpose of abstraction is to bring out high-level patterns.” [✓](https://worrydream.com/LadderOfAbstraction/)
  - 编码：“The color represents the time to completion, from red (fast) to black (mid-range) to white (slow).” [✓](https://worrydream.com/LadderOfAbstraction/)
  - 交互：“Mouse over Touch the chart to step down two levels, and see the trajectory for that particular turning rate and bend angle.” [✓](https://worrydream.com/LadderOfAbstraction/)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Algorithms run on data.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 处理的材料：“For many systems, that input data comes from some sort of environment.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 处理的材料：“designing the control system for a simple car simulation” [✓](https://worrydream.com/LadderOfAbstraction/)
- 对象：“an independent variable (such as time), a structure (such as an algorithm), and a dataset (such as an environment).” [✓](https://worrydream.com/LadderOfAbstraction/)
- 对象：“instead of showing the car, we show the car's entire trajectory” [✓](https://worrydream.com/LadderOfAbstraction/)
- 对象：“Here, we have called out the bend angle as an explicit parameter of the data.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 关系：“a system's state depends on its previous states in time.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 关系：“small differences in position are magnified into large differences in impact angle” [✓](https://worrydream.com/LadderOfAbstraction/)
- 关系：“We've controlled the data (the bend angle) and controlled the algorithm (the turning rate)” [✓](https://worrydream.com/LadderOfAbstraction/)
- 属性与度量：“Here, we have chosen a metric — a number that summarizes the behavior of the system in some interesting way.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 属性与度量：“the time to completion (number of steps the car takes to reach the end of the road)” [✓](https://worrydream.com/LadderOfAbstraction/)
- 属性与度量：“The independent variable is usually time.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 视图：“A realtime view is useful for getting a direct, visceral sense of a system's behavior” [✓](https://worrydream.com/LadderOfAbstraction/)
- 视图：“we simply overlay the trajectories for a range of turning rates” [✓](https://worrydream.com/LadderOfAbstraction/)
- 视图：“Another approach is an array of small multiples.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 视图：“This plots the time to completion (number of steps the car takes to reach the end of the road) versus the turning rate.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 交互：“Mouse over Drag the slider at the right to control time explicitly.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 交互：“Mouse over Touch the y-axis to step down just one level, and see trajectories for that particular turning rate.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 交互：“Mouse over Drag the lower slider to bend the road.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 回答的问题：“investigate areas of interest, and pose and verify hypotheses as quickly we think of them.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 回答的问题：“What patterns can we notice?” [✓](https://worrydream.com/LadderOfAbstraction/)
- 抽象与层级：“presents the ladder of abstraction, a technique for thinking explicitly about these levels” [✓](https://worrydream.com/LadderOfAbstraction/)
- 抽象与层级：“For most people, the level of abstraction makes math unpleasant or unusable as a practical tool” [✓](https://worrydream.com/SimulationAsAPracticalTool/)
- 为什么这样画：“This interactive essay presents the ladder of abstraction, a technique for thinking explicitly about these levels, so a designer can move among them consciously and confidently.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 为什么这样画：“The purpose of abstraction is to bring out high-level patterns.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 为什么这样画：“Instead, let's embrace the spirit of abstraction, and omit some details in the interest of exposing patterns.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 为什么这样画：“With visual patterns, we win hands-down. With logical inferences, we're slow and clumsy.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 原来的问题：“However, because each trajectory is separate and isolated, it's difficult to make visual comparisons between them.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 原来的问题：“We're attempting to overlay trajectories from different environments in the same space. This representation, though visually attractive, is difficult to make sense of.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 原来的问题：“However, it's difficult to deliberately explore a random space that doesn't offer well-defined dimensions to move in.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 原来的问题：“However, it is often impractical or impossible to derive a symbolic expression that represents the behavior of most systems.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 局限与代价：“But this benefit comes at a cost. We can no longer see the car! We can no longer viscerally experience the car's motion, and apply our common sense toward analyzing the system.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 局限与代价：“These representations reveal interesting high-level patterns. But they are too abstract to explain those patterns.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 局限与代价：“It's worth noting that both abstract representations above are actually approximations.” [✓](https://worrydream.com/LadderOfAbstraction/)
- 局限与代价：“We're pretty far up in the clouds now — this representation bears no resemblance to the motion of a car, and omits most lower-level details.” [✓](https://worrydream.com/LadderOfAbstraction/)

</details>

<a id="zettelkasten"></a>

### Luhmann 的卡片盒

- 领域：知识管理与写作；议题：让积累的笔记自己产生不显而易见的联想（“卡片盒为什么能发展出自己的创造力”）
- 编码：一般图与网络 + 层级与树；重点：连通与邻域、跨视图的同一对象；把握：页面信息支持，归类靠推断
- 说明：来源是 Bielefeld 的 Luhmann 档案网站上一篇分析卡片盒的文章（德语，二手分析），不是 Luhmann 本人的文字；档案网站的教程页读不到。
- 编码所依据的原文：
  - 关系：“Die Verweise können sich auf thematisch und räumlich nahestehende Zettel beziehen” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
  - 对象：“Auf einem solchen Zettel können bis zu 25 Verweise aufgeführt werden” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
  - 抽象与层级：“«Multiple-Storage-Prinzip» (Mehrfachablageprinzip)” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
  - 回答的问题：“Wie aber ist es möglich, dass der Zettelkasten eine eigene Kreativität entwickelt, also systematisch zu nicht naheliegenden Gedanken führt?” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
  - 视图：“eine Ordnungsstruktur im Sinne einer Systematik oder einer Buchgliederung” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Bereits bei der Lektüre von Texten orientierte sich Luhmann an den schon vorliegenden Einträgen” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 处理的材料：“einer Verzettelung der beim Lesen erstellten Notizen vor” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 对象：“die entsprechenden Begriffe aufgelistet sind” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 关系：“Verzettelungsverweis(e) auf einen (oder mehrere) Nebengedanken” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 关系：“das Verweisungssystem innerhalb der Sammlungen zentral” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 属性与度量：“Die Sammlung weist die Ordnungsziffern 1 bis 108” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 属性与度量：“durch spätere Eintragungen revidiert, nicht aber eliminiert wurden” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 视图：“die hier noch eher listenartig” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 交互：“Suchanfrage über das Schlagwortregister” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 交互：“des weitaus aufwendigeren physischen Nachschlagens und Herausnehmens der entsprechenden Zettel” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 抽象与层级：“Thema oder einen Begriff über verschiedene Zugänge” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)
- 抽象与层级：“3. Verweisungsstruktur” [✓](https://www.uni-bielefeld.de/fakultaeten/soziologie/forschung/luhmann-archiv/pdf/jschmidt_zettelkasten-als-uberraschungsgenerator.pdf)

</details>
- 没读到：encodings；说明：niklas-luhmann-archiv.de 的 tutorial 页与首页为 JS 渲染，静态 HTML 中无正文，没读到；以上摘录来自 Bielefeld Luhmann-Archiv 上 Johannes F. K. Schmidt 的文章，是二手分析，不是 Luhmann 原文

<a id="markmap"></a>

### Markmap

- 领域：知识管理与写作；议题：把一篇 Markdown 文档的层级直接看成一张可折叠的思维导图
- 编码：层级与树；重点：包含与层次；把握：官方页面直接写了
- 编码所依据的原文：
  - 处理的材料：“It parses Markdown content and extracts its intrinsic hierarchical structure” [✓](https://markmap.js.org/docs/markmap)
  - 交互：“Fold the current node and all its descendents.” [✓](https://markmap.js.org/docs/magic-comments)
  - 抽象与层级：“The maximum level of nodes to expand on initial render.” [✓](https://markmap.js.org/docs/json-options)
  - 编码：“all child branches will use the color of their ancestor node at the freeze level” [✓](https://markmap.js.org/docs/json-options)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“Basically we use markmap-lib to preprocess Markdown into structured data” [✓](https://markmap.js.org/docs/markmap)
- 对象：“Magic comments can be used to set the initial status of a node.” [✓](https://markmap.js.org/docs/magic-comments)
- 对象：“Freeze color at the specified level of branches” [✓](https://markmap.js.org/docs/json-options)
- 对象：“The max width of each node content.” [✓](https://markmap.js.org/docs/json-options)
- 关系：“all child branches will use the color of their ancestor node at the freeze level” [✓](https://markmap.js.org/docs/json-options)
- 关系：“Fold the current node and all its descendents.” [✓](https://markmap.js.org/docs/magic-comments)
- 属性与度量：“The stroke width of lines between nodes.” [✓](https://markmap.js.org/docs/json-options)
- 属性与度量：“The animation duration when folding/unfolding a node.” [✓](https://markmap.js.org/docs/json-options)
- 属性与度量：“The max width of each node content.” [✓](https://markmap.js.org/docs/json-options)
- 视图：“renders an interactive mindmap, aka markmap” [✓](https://markmap.js.org/docs/markmap)
- 视图：“then render the data into interactive SVG with markmap-view” [✓](https://markmap.js.org/docs/markmap)
- 编码：“A list of colors to use as the branch and circle colors for each node.” [✓](https://markmap.js.org/docs/json-options)
- 交互：“Whether to allow zooming the markmap.” [✓](https://markmap.js.org/docs/json-options)
- 交互：“Whether to allow panning the markmap.” [✓](https://markmap.js.org/docs/json-options)
- 交互：“The animation duration when folding/unfolding a node.” [✓](https://markmap.js.org/docs/json-options)
- 回答的问题：“Visualize your Markdown with mindmaps” [✓](https://markmap.js.org/)
- 抽象与层级：“extracts its intrinsic hierarchical structure” [✓](https://markmap.js.org/docs/markmap)
- 抽象与层级：“Freeze color at the specified level of branches” [✓](https://markmap.js.org/docs/json-options)

</details>

<a id="toulmin"></a>

### 图尔敏论证模型

- 领域：论证与写作；议题：分析并检验一个论证站不站得住，找出最弱的一环
- 编码：命题与论证；重点：关系上的类型与量、来源与证据；把握：官方页面直接写了
- 编码所依据的原文：
  - 对象：“WARRANT – logical and persuasive connection between a claim and the evidence.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
  - 属性与度量：“Toulmin says that the weakest part of any argument is its weakest warrant.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
  - 关系：“The warrant is the assumption on which the claim and the evidence depend.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
  - 回答的问题：“Second, test and critique your own argument.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
<details><summary>本案例读到的其他原文摘录</summary>

- 处理的材料：“analyzing the kind of argument you read and hear every day, in newspapers and on television” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 处理的材料：“involves analyzing your own argument from all sides to make it stronger” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 对象：“THE CLAIM – the statement or assertion the writer hopes to prove.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 对象：“GROUND/EVIDENCE – foundation that proves the claim.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 对象：“BACKING – the evidence supporting the warrant.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 关系：“the data (also called grounds or evidence ), which support the claim” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 关系：“connected by” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 关系：“reinforced by” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 属性与度量：“A qualifier is a statement about how strong the claim is.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 属性与度量：“Some qualifiers: in some cases, under these conditions, possibly, routinely, etc.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 属性与度量：“A strong warrant is one that is very difficult to disagree with.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 视图：“DIAGRAM OF THE TOULMIN ARGUMENT MODEL” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 交互：“First, analyze your sources by identifying the basic elements of the arguments being made.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 交互：“Second, test and critique your own argument.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 交互：“Compare one claim with another.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 交互：“Compare data between the two arguments.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 回答的问题：“Toulmin created a useful model for analyzing the validity of an argument.” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 抽象与层级：“Toulmin identifies the three essential parts of any argument as the claim” [✓](https://www.blinn.edu/writing-centers/wide/toulmin-argument.html)
- 抽象与层级：“Acknowledging the opposition to your argument is a good way to show that you fully understand all sides of your claim.” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)
- 抽象与层级：“involves analyzing your own argument from all sides to make it stronger” [✓](https://www.utsa.edu/twc/documents/Toulmin_Model_of_Argumentation.pdf)

</details>
- 没读到：encodings
<!-- /gen -->
