# interop — 跨 Harness 互操作

## 职责

与外部 Harness / 运行时互操作的适配面；避免把外部结构泄漏进 kernel。

## 接口占位

- ``InteropAdapter``（占位）`n- 能力发现与消息翻译（预留）

## 与其他模块的关系

- 依赖 ``protocols/*``；见 ``docs/future-trends.md``

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- **跨 Harness**：`InteropAdapter` 负责消息与能力发现的翻译，避免外部目录结构泄漏进 `kernel/`。
- 与 `protocols/mcp`、`protocols/a2a` 组成 **Agent 网关** 的适配侧。

