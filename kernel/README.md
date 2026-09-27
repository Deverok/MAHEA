# kernel — 核心运行时

## 职责

薄内核：生命周期、会话入口、能力挂载点与回合调度边界。不承载具体业务工具实现。

## 接口占位

- ``boot()`` / ``shutdown()``：进程级生命周期（占位）`n- ``handle_turn(input)``：单回合入口（占位）`n- ``register_capability(kind, handler)``：挂载 hooks/tools/plugins/skills（占位）

## 与其他模块的关系

- 调用 ``layers/*`` 完成上下文、编排与行动`n- 通过 ``caps/*`` 扩展行为`n- 经 ``models/*`` 访问模型提供方`n- 受 ``governance/``、``sandbox/``、``observability/`` 约束与观测

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- Loop / Graph 调度入口：将 `layers/orchestration` 的 `run_loop` / `run_graph` 挂到 `handle_turn` 之后的调度器（见 `docs/future-trends.md`）。
- 能力总线保持稳定，供 Agent 网关与跨 harness 适配器注册，而不膨胀内核业务逻辑。

