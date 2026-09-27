# Skill: audit

## 职责

对照多智能体 Harness 领域的核心概念，扫描仓库「已有 / 缺失 / 建议落点」，并输出或更新审计文档（通常为 `docs/AUDIT.md`）。

## 何时使用

- 任务一或任何「先审计后动手」节点
- 融合新参考项目后复查覆盖度
- 大版本结构调整前

## 输入

- 仓库根路径
- 参考概念清单（见下；可扩展，扩展项需能在 `stock/` 追溯）
- 既有 `docs/AUDIT.md`（若有）

## 输出

- 审计表：概念 → 状态（已有/缺失/部分）→ 建议模块路径 → 备注
- 优先级建议（骨架缺口优先于实现细节）
- 需新建的 `stock/` 条目提示（不编造摘要）

## 核心概念对照清单（基线）

| 概念簇 | 示例关键词 |
|--------|------------|
| 能力扩展 | hooks, tools, plugins, skills |
| 运行时节奏 | Thread / Turn / Step, loop, graph |
| 模型接入 | provider, adapter, config |
| 多智能体 | Agent, Crew/Flow, orchestration |
| 内核与规划 | kernel, planner, DI/container |
| 工作流 | workflows, event-driven |
| 记忆与知识 | memory, knowbase, RAG 边界 |
| 协议 | MCP, A2A, CLI |
| 保障 | evals, observability, governance, sandbox |
| 互操作 | interop, 跨 harness |

## 约束

- 只陈述仓库内可观察事实；外部能力描述以 `stock/` 核验状态为准。
- 无法核验的外部细节写「待核实」，不编造。
- 审计建议落点必须符合 `rules/ARCHITECTURE.md` 与 `NAMING.md`。

## 与规则的关系

必读 `rules/AGENTS.md`、`ARCHITECTURE.md`、`SOURCE_POLICY.md`。本技能产出供建设阶段使用，不直接修改业务实现逻辑。
