# memory — 记忆

## 职责

短时 / 长时记忆的接口边界与存放约定（占位）。

## 接口占位

- ``MemoryStore.read/write/search``（占位）

## 与其他模块的关系

- 供 ``layers/context`` 使用；与 ``knowbase/`` 区分（记忆偏会话态，知识库偏沉淀）

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
