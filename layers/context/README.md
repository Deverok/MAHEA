# layers/context — 上下文层

## 职责

上下文装配、裁剪、注入与回合记忆拼装。

## 接口占位

- ``build_context(turn)``（占位）`n- ``trim_context(context, budget)``（占位）

## 与其他模块的关系

- 读取 ``memory/``、``knowbase/``、``rules/``、``agents/```n- 供 ``layers/orchestration`` 与模型调用使用

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
