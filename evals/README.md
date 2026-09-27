# evals — 评测

## 职责

任务评测集、回归用例与评分接口占位。

## 接口占位

- ``run_eval(suite)``（占位）

## 与其他模块的关系

- 结果可进入 ``observability/``；策略阈值协作 ``governance/``

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- 回归套件驱动 Loop 退出条件；仿真模式下对接 `sandbox/`。
- 评测结果回灌 `observability/` 与 `governance/`（可观测性闭环）。

