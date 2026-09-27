# models/adapters — 适配器

## 职责

将提供方差异适配为内核统一调用面。

## 接口占位

- ``complete(request) -> response``（占位）`n- ``stream(request)``（预留）

## 与其他模块的关系

- 对接 ``models/providers``；被 ``src/models`` 镜像

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
