# caps/plugins — 插件

## 职责

可装载扩展单元；支撑「能力可插拔 / 微内核挂载」类模式的中性落点。

## 接口占位

- ``load_plugin(manifest)``（占位）`n- ``unload_plugin(id)``（占位）

## 与其他模块的关系

- 由 ``kernel/`` 管理生命周期；可聚合 hooks/tools/skills

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
