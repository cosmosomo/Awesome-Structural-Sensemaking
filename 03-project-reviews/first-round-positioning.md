# 第一轮代表项目定位

依据项目文档形成的初步能力定位，不是对所有项目安装使用后的实测评分。

“需要进一步验证”不是指某项能力必然缺失，而是指当前资料不足以对它作出充分判断。

<!-- gen:eval:positioning-1 -->
| 项目 | 最值得借鉴 | 主要适用范围 | 需要进一步验证 | 依据 |
| --- | --- | --- | --- | --- |
| [AntV G6](https://g6.antv.antgroup.com/) | 嵌套图、分组与交互 | 复杂关系及子图 | 大图展开时的布局稳定性 | 调研报告（未复核） |
| [LikeC4](https://likec4.dev/) | 统一模型、多视角 | 软件架构认知 | 跨视图对象定位、复杂模型导航 | 调研报告（未复核） |
| [Nx](https://github.com/nrwl/nx) | 项目图与任务图分离 | 工程依赖与执行 | 更复杂跨层关系的表达能力 | 调研报告（未复核） |
| [Backstage](https://github.com/backstage/backstage) | 关系图融入实体管理 | 开发者门户 | 多层展开、密集关系处理 | 调研报告（未复核） |
| [Understand Anything](https://understand-anything.com/) | 源码提炼与交互理解 | 代码库、知识文档 | 自动提炼结果的语义保真性 | 调研报告（未复核） |
| [AgentEnsemble](https://agentensemble.github.io/agentensemble/) | DAG 与 Trace 时间图切换 | 多 Agent 任务 | 跨层身份同步、复杂协作规模 | 调研报告（未复核） |
| [AgentPrism](https://github.com/evilmartians/agent-prism) | 独立 Trace 组件设计 | Agent 运行详情 | 扩展性、复杂运行与嵌套性能 | 调研报告（未复核） |
| [Langfuse](https://github.com/langfuse/langfuse) | Trace 融入工程闭环 | AI 应用观测 | 宏观组织结构与 Trace 的关联能力 | 调研报告（未复核） |
| [DataHub](https://github.com/datahub-project/datahub) | 血缘和上下游影响 | 数据资产关系 | 复杂子图、跨层影响呈现 | 调研报告（未复核） |
| [Apache SkyWalking](https://skywalking.apache.org/) | 拓扑与监控、Trace 联动 | 分布式系统 | 复杂层级与空间视图的使用成本 | 调研报告（未复核） |
| [CNCF Landscape](https://landscape.cncf.io/) | 大规模生态分类与搜索 | 技术、产品生态 | 跨类别关系网络的表达能力 | 调研报告（未复核） |
| [Kumu](https://kumu.io/) | 复杂关系与叙事视图 | 系统映射、知识表达 | 自动结构提取和多层语义管理 | 调研报告（未复核） |
<!-- /gen -->

## 第一批深入研究的 12 个项目

它们覆盖了结构提取、模型驱动、图形引擎、视图投影、运行时可视化、综合产品交互和认知演化等不同问题。不一定是各自领域性能最好的项目，但适合作为第一批建立比较标准的研究样本。

| 顺序 | 项目 | 重点研究什么 |
| --- | --- | --- |
| 1 | LikeC4 | 从统一模型产生多视角架构 |
| 2 | AntV G6 | 嵌套、折叠、复杂关系图布局 |
| 3 | Understand Anything | 从代码、知识提炼可交互结构 |
| 4 | Nx Graph | 静态项目依赖与任务依赖的区别 |
| 5 | Backstage | 实体关系图如何融入完整产品 |
| 6 | AgentEnsemble | 协作 DAG、时间视图与运行事件 |
| 7 | AgentPrism | 独立可复用的 Agent Trace UI |
| 8 | DataHub | 血缘关系、跨层钻取、影响分析 |
| 9 | SkyWalking | 服务拓扑与 Trace、监控的联动 |
| 10 | Landscape2 | 生态地图的数据组织和交互导航 |
| 11 | GraphRAG | 从文本建立分层结构与摘要 |
| 12 | Graphiti | 动态关系、证据来源与认知演化 |
