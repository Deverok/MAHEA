# future-trends — 未来兼容与接口预留

> 均为**占位契约**，非实现。深度 A 只保证目录、README 与类型形状可挂接。

## 预留总表

| 方向 | 意图 | 主落点 | 协作落点 | 占位接口（名称级） |
|------|------|--------|----------|-------------------|
| Loop Engineering | 可配置的验证/修复循环（沉默即成功、有限重试） | `layers/orchestration/` | `kernel/`、`evals/`、`scripts/` | `run_loop(loop_def)` |
| Graph Engineering | 显式图编排与状态转移 | `layers/orchestration/` | `agents/`、`kernel/` | `run_graph(graph_def)` |
| 跨 Harness | 外部运行时互操作，避免结构泄漏进内核 | `interop/` | `protocols/*` | `InteropAdapter.translateInbound/Outbound` |
| 信任工程 | 策略、权限、审计证据 | `governance/` | `evals/`、`observability/` | `PolicyEngine.allow`、评测门禁 |
| Agent 网关 | 统一入口：路由到 Agent/协议/工具 | `protocols/`、`interop/` | `agents/`、`protocols/cli` | 网关路由表（文档级）+ A2A/MCP 桥 |
| 仿真环境 | 无真实副作用的演练与回归 | `sandbox/` | `evals/` | `SandboxExecutor.run`（sim 模式标志） |
| 可观测性闭环 | 轨迹 → 评测 → 策略反馈 | `observability/` | `evals/`、`governance/` | trace/metric 事件面 + eval 结果回灌 |

## 与类型占位的对应

见 [`src/shared/types/mahea.d.ts`](../src/shared/types/mahea.d.ts) 与 Python `Protocol`：

- `OrchestrationLayer.runLoop` / `runGraph`
- `InteropAdapter`
- `ActionLayer.requestApproval`
- `Kernel.registerCapability`

## 演进原则

1. **先挂接口，后填实现**；实现时再开依赖讨论。
2. **中性命名**；不因单一产品更新而改根目录结构。
3. 新方向必须能在 `stock/` 找到动机来源或记为内部 ADR（未来可放 `docs/`）。

## 模块 README 中的预留小节

下列模块 README 含「未来预留」小节（与本表一致）：

- `kernel/`、`layers/orchestration/`
- `interop/`、`protocols/`（及 mcp/a2a/cli）
- `governance/`、`evals/`、`sandbox/`、`observability/`
