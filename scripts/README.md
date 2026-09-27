# scripts — 脚本

## 职责

无第三方依赖的辅助脚本（校验结构、生成清单等）。

## 接口占位

- 脚本应可在标准 shell/Python 标准库下运行

## 与其他模块的关系

- 不替代 CI；可被 ``.github/`` 文档引用

## 实现深度

深度 A：本目录以说明与占位为主，不引入第三方依赖。权威代码占位见 `src/`（Python）与 `src/shared/types`（TypeScript 类型说明）。
