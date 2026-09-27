# 示例：模块地图走通

本示例说明 fork 后如何阅读骨架（非可执行 Agent）。

1. 阅读 `rules/AGENTS.md` 与 `rules/ARCHITECTURE.md`
2. 用 `caps/skills/router` 路由任务到模块
3. 查看 `kernel/` → `layers/` → `caps/` → `models/`
4. 协议与保障：`protocols/`、`interop/`、`evals/`、`observability/`、`governance/`、`sandbox/`
5. 溯源与融合：`stock/`、`docs/harness-fusion.md`

对应接口形状：`src/kernel/protocols.py` 与 `src/shared/types/mahea.d.ts`。
