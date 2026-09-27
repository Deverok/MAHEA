# stock — 素材来源层

所有分析、融合归因与审计中的外部依据应在此登记。字段约定见 `rules/SOURCE_POLICY.md`。

## 子目录

| 目录 | 用途 |
|------|------|
| `harnesses/` | Harness / Agent 框架与产品参考 |
| `protocols/` | MCP、A2A 等协议 |
| `papers/` | 论文与正式技术报告 |
| `articles/` | 博文、教程、社区知识库 |

## 元数据模板

```yaml
---
id: unique-slug
title: 可读标题
url: https://example.com/...
type: harness | protocol | paper | article
accessed: YYYY-MM-DD
summary: 可核验摘要；未知留空
maps_to:
  - path/in/mahea
status: verified | pending
---
```

导航见 [INDEX.md](INDEX.md)。
