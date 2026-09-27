# 分层总览

权威说明见 [`rules/ARCHITECTURE.md`](../rules/ARCHITECTURE.md)。本文是面向人类与 Agent 的短地图。

```text
agents / rules
        ↓
protocols + interop
        ↓
caps (hooks / tools / plugins / skills)
        ↓
layers (context → orchestration → action)
        ↓
kernel
        ↓
models (providers / configs / adapters)
        ↓
knowledge (memory / knowbase / docs / stock / assets)
        ↓
assurance (evals / observability / governance / sandbox)
```

源码占位：[`src/`](../src/)（Python 权威）+ [`src/shared/types/`](../src/shared/types/)（TS 形状）。

融合原则：[`harness-fusion.md`](harness-fusion.md)。预留接口：[`future-trends.md`](future-trends.md)。
