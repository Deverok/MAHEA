# governance — 治理与信任

## 职责

策略、权限、审批与信任工程相关约定。

## 接口占位

- ``PolicyEngine.allow(action)``（占位）

## 与其他模块的关系

- 约束 action/tools；与 sandbox、evals 协同

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- **信任工程**：策略决策、权限边界、审计证据保留；与 `evals/` 门禁阈值联动。
- `PolicyEngine.allow` 结果应可被 `observability/` 记录。

