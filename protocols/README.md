# protocols — 接口协议层

## 职责

MCP / A2A / CLI 等对外与对内协议边界。

## 接口占位

见各子目录；索引见 [INDEX.md](INDEX.md)。

## 与其他模块的关系

- 与 ``interop/`` 共同支撑跨 harness`n- 工具面连接 ``caps/tools``

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- **Agent 网关**：CLI / MCP / A2A 统一路由表（文档 + 后续实现），入口收敛到 `kernel.handle_turn`。
- 跨运行时细节下放 `interop/`，协议模块只保留 wire 契约说明。

