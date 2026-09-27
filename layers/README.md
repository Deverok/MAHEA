# layers — 分层运行时

## 职责

将上下文、编排与行动从内核中拆出，保持 kernel 精简。

## 接口占位

子模块各自暴露装配/执行占位接口；见各子目录 README。

## 与其他模块的关系

- 上承 ``kernel/``，下接 ``caps/`` 与 ``models/```n- 顺序说明见 [INDEX.md](INDEX.md)

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
