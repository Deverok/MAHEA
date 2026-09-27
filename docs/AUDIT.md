# AUDIT.md — 仓库现状审计

> 审计方法见 `caps/skills/audit/SKILL.md`。审计前已阅读 `rules/AGENTS.md`、`ARCHITECTURE.md`、`SOURCE_POLICY.md`。  
> 审计时点：任务零完成后、任务二模块建设前。  
> 外部能力细节以后续 `stock/` 核验为准；未核验处标记「待核实」。

## 1. 仓库快照（可观察事实）

| 路径 | 状态 |
|------|------|
| `LICENSE` | 已有（Apache-2.0） |
| `README.md` | 已有（项目定位段） |
| `.gitignore` | 已有（偏 Python） |
| `rules/AGENTS.md` 等五件套 | 已有（任务零） |
| `caps/skills/{router,retro,audit}` | 已有（任务零） |
| `kernel/`、`layers/`、`models/`、`src/` 等 | **缺失** |
| `docs/`（除本文件外） | **缺失**（本文件为审计产出） |
| `stock/` | **缺失** |
| `protocols/`、`interop/`、保障层、辅助层 | **缺失** |
| 第三方依赖清单 | **无**（符合深度 A） |
| `template/` | **不存在**（符合约束） |

## 2. 概念对照表

| 概念簇 | 示例关键词 | 状态 | 建议落点 | 备注 |
|--------|------------|------|----------|------|
| 元规则 / 协作 | AGENTS, ARCHITECTURE | 已有 | `rules/` | 任务零完成 |
| 技能包 | skills, router/retro/audit | 部分 | `caps/skills/` | 基线三技能已有；扩展技能待定 |
| Hooks | PreToolUse / PostToolUse 等 | 缺失 | `caps/hooks/`、`src/capabilities/` | 模式来源见融合文档；待 stock |
| Tools | 工具注册与调用 | 缺失 | `caps/tools/`、`layers/action/` | |
| Plugins | 一切皆插件 / 微内核挂载 | 缺失 | `caps/plugins/`、`kernel/` | DeepSeek Harness 等理念待 stock 登记 |
| Kernel | 薄内核、生命周期 | 缺失 | `kernel/`、`src/kernel/` | |
| Thread / Turn / Step | 会话节奏 | 缺失 | `kernel/`、`layers/orchestration/` | Codex 等节奏模型；待核实细节 |
| Context | 上下文装配 | 缺失 | `layers/context/` | |
| Orchestration | Crew/Flow、图/循环 | 缺失 | `layers/orchestration/` | |
| Action | 副作用、审批 | 缺失 | `layers/action/`、`sandbox/` | Grok Build 审批/沙箱理念待 stock |
| Model Provider | providers / adapters | 缺失 | `models/*`、`src/models/` | |
| Memory | ST/LT memory | 缺失 | `memory/` | AutoGPT 等；待 stock |
| Knowbase / Docs | 知识与文档 | 部分 | `knowbase/`、`docs/` | 仅有本审计文档 |
| Stock / 溯源 | 素材库 | 缺失 | `stock/*` | SOURCE_POLICY 已定义字段 |
| Agents | 角色与协作描述 | 缺失 | `agents/` | |
| MCP | 工具协议 | 缺失 | `protocols/mcp/` | |
| A2A | Agent 间协议 | 缺失 | `protocols/a2a/` | |
| CLI | 命令行界面 | 缺失 | `protocols/cli/` | |
| Interop | 跨 harness | 缺失 | `interop/` | 未来预留重点 |
| Evals | 评测 | 缺失 | `evals/` | |
| Observability | 观测闭环 | 缺失 | `observability/` | |
| Governance | 信任 / 策略 | 缺失 | `governance/` | |
| Sandbox | 隔离执行 | 缺失 | `sandbox/` | |
| Examples / Scripts / CI | 辅助 | 缺失 | `examples/`、`scripts/`、`.github/` | |
| 融合说明 | harness-fusion | 缺失 | `docs/harness-fusion.md` | 任务四/五 |
| 未来趋势 | future-trends | 缺失 | `docs/future-trends.md` | 任务六 |
| 双语言占位 | Python + TS types | 缺失 | `src/**`、`src/shared/types/` | |
| Assets | 静态资源 | 缺失 | `assets/` | |

## 3. 参考来源覆盖（登记状态）

以下链接来自建设任务说明；审计时点 **尚未** 写入 `stock/`（任务三处理）。文档中暂列 URL，细节「待核实」。

### Harness 工程知识库

- https://github.com/Conn-Ho/harness-engineering
- https://www.idao.fun/blog/2026-05-16-harness-engineering-deep-coding-tutorial
- https://cipherhub.cloud/posts/ai-agent/harness-engineering/

### 社区与知识库

- https://my.feishu.cn/wiki/UFTcwkaVriL04UkcZj8cQRkRnDg （可能需登录 → 预期 pending）
- https://gotoaiworld.feishu.cn/wiki/GZYYwfOnKif9JxkqZeKcGmd8nMg （可能需登录 → 预期 pending）
- https://github.com/charliedream1/ai_wiki
- https://luuman.github.io/ai-doc/docs
- https://segmentfault.com/a/1190000047720515

### 开源 / 产品参考（融合对象）

- Claude Code、Codex、DeepSeek Harness、OpenHarness、Grok Build、CrewAI、Semantic Kernel、LlamaIndex、LangChain、AutoGPT  
  （具体 URL 见任务说明与后续 `stock/harnesses/` 卡片）

## 4. 优先级建议（供任务二施工）

1. **P0 — 目录与 README 骨架**：按 `rules/ARCHITECTURE.md` 补齐根模块，消除上表「缺失」。
2. **P0 — `src/` 双语言占位**：Python 包 + `src/shared/types` TS 接口说明。
3. **P1 — `stock/` 素材卡**：登记任务说明中的 URL，能核验则 `verified`，否则 `pending`。
4. **P1 — `docs/harness-fusion.md` + `future-trends.md`**：完成中性融合与接口预留。
5. **P2 — examples / scripts / .github**：辅助协作，不引入依赖。

## 5. 审计结论

- 元规则与基础技能已就绪，具备继续建设的协作约束。
- 运行时、能力扩展面（除 skills）、模型层、协议层、保障层、知识溯源层均为空缺，与「可 fork 骨架」目标差距明确。
- **建议**：以本文件第 2 节为任务二施工清单；不在深度 A 范围内实现可运行 Agent。

## 6. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-09-27 | 任务零后初版审计 |
| 2026-09-27 | 任务二–六完成后：模块骨架、stock、融合与预留文档已落地；概念表中原「缺失」项多为目录级已有，实现仍为占位 |
