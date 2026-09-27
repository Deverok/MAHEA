# MAHEA
MAHEA（Multi-Agent Harness Engineering Architecture）是自我学习后面向多智能体 Harness 工程实践的开源模板：整合提示词、上下文、规则库、工作流、技能包、工具箱、MCP/A2A/CLI、多 Agent 协作、自进化与知识图谱，融合 Claude Code、Codex、DeepSeek Harness 等设计，保留素材来源，提供可复制、可生长的项目骨架，助力构建可控、可审计、可持续演进的 AI 智能体系统。

**模型决定上限，Harness 决定下限。**

本仓库**根目录即骨架**（无 `template/` 子目录）。Fork 后即可按模块扩展。实现深度以文档、目录与接口占位为主（Python 权威占位 + TypeScript 类型说明），默认不引入第三方运行时依赖。

## 开始之前

所有协作与改动请先阅读 [`rules/AGENTS.md`](rules/AGENTS.md) 及任务相关规则。

## 模块地图

| 层 | 路径 |
|----|------|
| 元规则 | [`rules/`](rules/) |
| 核心运行时 | [`kernel/`](kernel/)、[`layers/`](layers/) |
| 能力 | [`caps/`](caps/)（hooks / tools / plugins / skills） |
| 模型 | [`models/`](models/) |
| 源码占位 | [`src/`](src/) |
| Agent | [`agents/`](agents/) |
| 知识 | [`memory/`](memory/)、[`knowbase/`](knowbase/)、[`docs/`](docs/)、[`stock/`](stock/)、[`assets/`](assets/) |
| 协议与互操作 | [`protocols/`](protocols/)、[`interop/`](interop/) |
| 保障 | [`evals/`](evals/)、[`observability/`](observability/)、[`governance/`](governance/)、[`sandbox/`](sandbox/) |
| 辅助 | [`examples/`](examples/)、[`scripts/`](scripts/)、[`.github/`](.github/) |

架构说明：[`rules/ARCHITECTURE.md`](rules/ARCHITECTURE.md)  
审计：[`docs/AUDIT.md`](docs/AUDIT.md)  
融合：[`docs/harness-fusion.md`](docs/harness-fusion.md)  
预留：[`docs/future-trends.md`](docs/future-trends.md)  
素材：[`stock/INDEX.md`](stock/INDEX.md)  
示例走通：[`examples/walkthrough.md`](examples/walkthrough.md)

## 如何 Fork 使用

1. Fork / Clone 本仓库。
2. 阅读 `rules/` 与 `docs/AUDIT.md`。
3. 按需填充各模块实现；接口形状参考 `src/**/protocols.py` 与 `src/shared/types/mahea.d.ts`。
4. 外部资料登记到 `stock/`（见 `rules/SOURCE_POLICY.md`）。
5. 可选：`python scripts/check_skeleton.py` 检查关键路径是否齐全。

## 许可

Apache License 2.0 — 见 [`LICENSE`](LICENSE)。
