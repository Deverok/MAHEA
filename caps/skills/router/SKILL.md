# Skill: router

## 职责

根据用户意图或任务描述，路由到应阅读的 `rules/`、应修改的模块目录、以及相关 `docs/` / `stock/` 条目。

## 何时使用

- 任务开始、范围不清时
- 不确定改动应落在 kernel / layers / caps / protocols / assurance 哪一层时

## 输入

- 任务简述（目标、约束、是否涉及外部引用）

## 输出

- 必读规则列表（路径）
- 目标模块列表（路径）
- 建议技能（audit / retro 等）
- 明确「不要改」的区域（若有）

## 路由提示（简表）

| 意图关键词 | 优先路径 |
|------------|----------|
| 规则、协作、Agent 行为 | `rules/AGENTS.md` |
| 分层、模块职责 | `rules/ARCHITECTURE.md` |
| 命名、目录 | `rules/NAMING.md` |
| git 提交、推送、PR | `rules/git.rules`、`rules/CONTRIBUTING.md` |
| 引用、素材、来源 | `rules/SOURCE_POLICY.md`、`stock/` |
| hooks/tools/plugins/skills | `caps/` |
| 上下文 / 编排 / 行动 | `layers/` |
| 模型提供方 | `models/` |
| MCP / A2A / CLI | `protocols/`、`interop/` |
| 评测 / 观测 / 治理 / 沙箱 | `evals/`、`observability/`、`governance/`、`sandbox/` |
| 融合、参考项目 | `docs/harness-fusion.md` |
| 未来预留 | `docs/future-trends.md` |

## 与规则的关系

执行本技能前阅读 `rules/AGENTS.md`。路由结果不得违反 ARCHITECTURE / NAMING / SOURCE_POLICY。
