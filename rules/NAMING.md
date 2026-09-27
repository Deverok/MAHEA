# NAMING.md — 命名约定

> 新建目录、模块或文档前请阅读本文件。

## 原则

1. **语义化命名**：名称表达职责（如 `orchestration`、`observability`），不使用无意义缩写。
2. **禁止数字前缀**：不得使用 `01-kernel`、`1_audit.md` 等形式。顺序通过：
   - 目录内 `INDEX.md`
   - 文档交叉链接
   - `stock` 的 `maps_to` 与架构说明中的引用关系
3. **根目录即骨架**：模块放在仓库根下；禁止用 `template/` 承载可 fork 结构。
4. **小写与连字符/下划线**：
   - 目录与文档文件：优先 `kebab-case` 或单一词（如 `knowbase`、`harness-fusion.md`）。
   - Python 包与模块：`snake_case`。
   - TypeScript 类型文件：`camelCase` 或与概念一致的 `PascalCase` 类型名；文件可用 `kebab-case.d.ts`。

## 推荐词汇（中性）

| 使用 | 避免（易绑定单一产品） |
|------|------------------------|
| kernel, layers, caps | 直接照搬某产品内部私有目录名作为唯一结构 |
| hooks, tools, plugins, skills | 仅服务单一厂商的扩展名 |
| providers, adapters | 绑定单一模型品牌的顶层命名 |
| stock（素材库） | 无来源的「资料堆」目录 |

## INDEX.md

需要表达阅读或加载顺序时，在该目录创建 `INDEX.md`，用有序列表或表格说明，而不是改文件夹名。

## 文件后缀习惯

| 类型 | 后缀 |
|------|------|
| 规则与模块说明 | `.md` |
| 技能定义 | `SKILL.md` |
| 素材卡 | `.md`（含 frontmatter） |
| Python 占位 | `.py` |
| TS 接口说明 | `.d.ts` 或 `interfaces.md` |
