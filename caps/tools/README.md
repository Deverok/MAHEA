# caps/tools — 工具

## 职责

可调用工具的描述、schema 与处理器占位。

## 接口占位

- ``ToolSpec`` / ``invoke_tool(name, args)``（占位）

## 与其他模块的关系

- 经 ``layers/action`` 执行；可经 ``protocols/mcp`` 对外暴露

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
