# layers/orchestration — 编排层

## 职责

多步计划、多 Agent 协作节奏；为 Loop/Graph Engineering 预留扩展点。

## 接口占位

- ``plan(goal, context)``（占位）`n- ``next_step(state)``（占位）`n- ``run_graph(graph_def)`` / ``run_loop(loop_def)``（预留占位）

## 与其他模块的关系

- 驱动 ``layers/action```n- 可引用 ``agents/`` 与 ``caps/skills```n- 未来图/循环工程见 ``docs/future-trends.md``

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- **Loop Engineering**：`run_loop(loop_def)` — 验证/修复循环、有限重试与升级人类。
- **Graph Engineering**：`run_graph(graph_def)` — 显式节点/边与状态转移。
- 详细契约索引：`docs/future-trends.md`。

