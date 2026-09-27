# layers/action — 行动层

## 职责

工具调用与副作用边界；可挂接审批、沙箱执行结果回传。

## 接口占位

- ``execute_action(plan_step)``（占位）`n- ``request_approval(action)``（占位）

## 与其他模块的关系

- 使用 ``caps/tools``、``caps/hooks```n- 执行隔离协作 ``sandbox/```n- 事件上报 ``observability/``

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
