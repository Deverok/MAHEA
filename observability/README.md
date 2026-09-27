# observability — 可观测性

## 职责

轨迹、指标、日志与闭环反馈的挂载点。

## 接口占位

- ``trace`` / ``metric`` / ``log`` 事件面（占位）

## 与其他模块的关系

- 贯穿 kernel/layers/caps；与 evals 形成闭环（预留）

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- **可观测性闭环**：trace/metric/log → eval 评分 → governance 策略调整建议（人工或半自动）。
- 贯穿 kernel / layers / caps 的事件字段保持稳定，便于后续实现。

