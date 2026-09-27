# sandbox — 沙箱

## 职责

不安全副作用的隔离执行环境边界。

## 接口占位

- ``SandboxExecutor.run(command_or_tool)``（占位）

## 与其他模块的关系

- 服务 ``layers/action``；审批可接 governance/CLI

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- **仿真环境**：`sim` 模式标志下无真实外部副作用，供 `evals/` 使用。
- 与 `layers/action`、`governance` 审批链集成。

