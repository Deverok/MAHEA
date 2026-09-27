# SOURCE_POLICY.md — 素材与引用策略

> 涉及外部链接、项目对比、融合归因前请阅读本文件。

## 核心要求

1. **素材可追溯**：所有分析、融合说明、审计中的外部依据，必须在 `stock/` 中有来源记录。
2. **禁止编造**：不得伪造 URL、作者、日期、引用内容或未核验的产品能力。
3. **无法核验时标记 pending**：保留 URL，`status: pending`，摘要可留空或写「待核实」。

## stock 目录

| 子目录 | 用途 |
|--------|------|
| `stock/harnesses/` | Harness / Agent 框架类开源或产品参考 |
| `stock/protocols/` | MCP、A2A 等协议与互操作规范 |
| `stock/papers/` | 论文与正式技术报告 |
| `stock/articles/` | 博文、教程、社区知识库条目 |

详见 `stock/README.md`。

## 统一元数据字段

每条素材文件建议使用 YAML frontmatter：

```yaml
---
id: unique-slug
title: 可读标题
url: https://example.com/...
type: harness | protocol | paper | article
accessed: YYYY-MM-DD
summary: 一两句可核验摘要；未知则留空
maps_to:
  - modules/or/docs/paths
status: verified | pending
---
```

| 字段 | 说明 |
|------|------|
| `id` | 稳定短标识，文件名建议与 id 一致 |
| `title` | 来源标题 |
| `url` | 原始链接；无公开 URL 则说明获取方式，勿假造 |
| `type` | 与所属子目录一致 |
| `accessed` | 登记或最后核验日期 |
| `summary` | 仅写可核验事实；禁止臆测 |
| `maps_to` | 映射到 MAHEA 模块或文档路径 |
| `status` | `verified` 已核验；`pending` 待核实 |

## 引用写法

- 文档中引用外部项目时，优先链接到对应 `stock/...` 条目，其次给原始 URL。
- 飞书 Wiki 等可能需登录的来源：允许登记 URL，默认 `pending`，不臆造正文摘要。
- 融合归因（「X 贡献了 Y 模式」）必须能在 `docs/harness-fusion.md` 与 `stock/` 交叉核对。

## 禁止事项

- 复制大量受版权保护的全文到本仓库（摘要与结构说明即可）。
- 将未登记来源写成「已验证事实」。
- 用数字前缀伪装「权威排序」替代 `maps_to` 与 INDEX 导航。
