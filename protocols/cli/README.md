# protocols/cli — CLI

## 职责

命令行入口与人机审批交互边界（占位）。

## 接口占位

- ``main(argv)`` 入口说明（占位）

## 与其他模块的关系

- 可触发 ``kernel`` turn；审批流可接 ``governance/``

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。

## 未来预留

- 人机审批与网关的本地入口；可触发 governance 策略与 sandbox 执行。

