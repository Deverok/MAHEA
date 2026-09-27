# ARCHITECTURE.md — MAHEA 分层架构

> 修改结构前请先读 `rules/AGENTS.md` 与本文件。

## 定位

MAHEA 是可 fork 的最小多智能体 Harness **工程骨架**。根目录模块即项目起点；实现深度以接口占位与文档为主，运行时细节由 fork 方填充。

## 分层总览

```text
+------------------------------------------------------------------+
|                         agents / rules                           |
+------------------------------------------------------------------+
| protocols (mcp / a2a / cli)  |  interop                          |
+------------------------------------------------------------------+
| caps: hooks / tools / plugins / skills                           |
+------------------------------------------------------------------+
| layers: context  |  orchestration  |  action                     |
+------------------------------------------------------------------+
|                         kernel                                   |
+------------------------------------------------------------------+
| models: providers / configs / adapters                           |
+------------------------------------------------------------------+
| knowledge: memory / knowbase / docs / stock / assets             |
+------------------------------------------------------------------+
| assurance: evals / observability / governance / sandbox          |
+------------------------------------------------------------------+
| src/*  —  Python 权威占位 + shared TS 类型说明                     |
+------------------------------------------------------------------+
```

顺序通过 `INDEX.md` 与模块间引用表达，不使用数字前缀目录名。

## 模块职责（摘要）

| 层 | 目录 | 职责 |
|----|------|------|
| 核心运行时 | `kernel/` | 生命周期、会话/回合调度入口、插件总线挂载点 |
| 上下文层 | `layers/context/` | 上下文装配、裁剪、注入 |
| 编排层 | `layers/orchestration/` | 多步计划、图/循环编排预留 |
| 行动层 | `layers/action/` | 工具调用、副作用边界、审批钩子 |
| 能力层 | `caps/*` | hooks / tools / plugins / skills |
| 模型层 | `models/*` | Provider、配置、适配器 |
| 源码占位 | `src/*` | 与上述概念对应的 Python/TS 接口 |
| 知识层 | `memory/` `knowbase/` `docs/` `stock/` `assets/` | 记忆、知识、文档、素材、静态资源 |
| Agent | `agents/` | Agent 角色与编排描述 |
| 规则 | `rules/` | 元规则与协作约定 |
| 协议 | `protocols/*` `interop/` | MCP / A2A / CLI 与跨 harness 互操作 |
| 保障 | `evals/` `observability/` `governance/` `sandbox/` | 评测、观测、治理、沙箱 |
| 辅助 | `examples/` `scripts/` `.github/` | 示例、脚本、协作模板 |

## 设计约束

1. **多项目融合，非单点复刻**：模式来源见 `docs/harness-fusion.md`，落点分散到中性模块名。
2. **能力可插拔**：hooks / tools / plugins / skills 为扩展面；kernel 保持薄。
3. **知识可追溯**：分析结论必须能映射到 `stock/` 条目。
4. **保障层一等公民**：评测、观测、治理、沙箱与运行时并列，而非事后补丁。
5. **未来接口预留**：Loop/Graph、跨 harness、信任工程、Agent 网关、仿真、观测闭环——见 `docs/future-trends.md`。

## 双语言占位

- Python：`src/` 包与 `Protocol`/空签名为权威。
- TypeScript：`src/shared/types/` 描述稳定公共形状；不强制构建链。

## 与其他规则的关系

- 命名：`rules/NAMING.md`
- 素材：`rules/SOURCE_POLICY.md`
- 贡献：`rules/CONTRIBUTING.md`
