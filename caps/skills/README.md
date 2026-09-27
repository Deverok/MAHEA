# caps/skills — 技能包

技能是面向协作与工程流程的可复用工作说明，不是运行时强制插件。

## 基础技能

| 技能 | 目录 | 职责 |
|------|------|------|
| router | `router/` | 按意图路由到规则、模块与文档 |
| retro | `retro/` | 阶段结束复盘与自查 |
| audit | `audit/` | 对照参考概念审计仓库缺口 |

顺序与选用关系见 [INDEX.md](INDEX.md)。每个技能以 `SKILL.md` 为入口。

## 关系

- 受 `rules/` 约束；不替代架构规则。
- 可被 `agents/`、`layers/orchestration/` 在未来编排中引用（占位）。
- 与 `caps/hooks`、`caps/tools`、`caps/plugins` 并列，同属能力层。
