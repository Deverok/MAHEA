# AGENTS.md — MAHEA 协作入口

MAHEA（Multi-Agent Harness Engineering Architecture）是面向多智能体 Harness 工程实践的开源骨架。  
核心理念：**模型决定上限，Harness 决定下限。**

## 强制前置

**所有后续工作（审计、模块建设、文档、素材、代码占位）必须先阅读 `rules/` 下与当前任务相关的规则文件。**

建议最小阅读集：

1. 本文件 `rules/AGENTS.md`
2. `rules/ARCHITECTURE.md`（涉及结构/模块时）
3. `rules/SOURCE_POLICY.md`（涉及外部引用或素材时）
4. `rules/NAMING.md`（涉及新建路径或文件名时）
5. `rules/CONTRIBUTING.md`（涉及贡献或 PR 时）
6. `rules/git.rules`（涉及 `git commit` / `git push` / 开 PR 时）

未阅读相关规则即修改仓库，视为违反协作约定。

## 工作原则

1. **根目录即骨架**：仓库根目录模块结构即为 fork 起点；禁止创建 `template/` 子文件夹承载骨架。
2. **分阶段推进**：按任务序列执行；每阶段完成自查后再进入下一阶段（自动化批量建设时以完整自查清单收束）。
3. **先审计，后动手**：重大结构变更前对照 `docs/AUDIT.md` 与参考概念。
4. **保留来源**：凡分析、融合、归因必须在 `stock/` 有对应记录（见 SOURCE_POLICY）。
5. **不破坏现有内容**：扩展 README 与已有文件，避免无故清空定位文案或改动 LICENSE。
6. **不编造**：禁止伪造链接、数据、项目能力或未核验的实现细节。
7. **不过度设计**：深度以文档 + 目录 + 接口占位为主；未经确认不引入第三方依赖。
8. **中性融合**：不将 MAHEA 设计为任一单一 Harness 的复刻；融合原则见 `docs/harness-fusion.md`。

## 能力技能入口

基础技能包位于 `caps/skills/`：

| 技能 | 用途 |
|------|------|
| `router` | 按意图路由到模块、规则与文档 |
| `retro` | 阶段结束复盘与自查 |
| `audit` | 对照参考概念扫描仓库缺口 |

执行对应工作流前，读取该技能目录下的 `SKILL.md`。

## 语言与占位约定

- **Python**：`src/` 下包结构与协议桩为权威占位。
- **TypeScript**：仅公共接口/类型说明（如 `src/shared/types/*.d.ts`），不强制完整 TS 工程与 npm 依赖。

## 提交前自查（摘要）

完整 Git 流程与安全协议见 [`rules/git.rules`](git.rules)。摘要：

- [ ] 已阅读本次改动相关的 `rules/` 文件（含 `git.rules`）
- [ ] 无数字前缀模块/文档名；无 `template/` 目录
- [ ] 外部引用已在 `stock/` 登记或标记 pending
- [ ] 未引入未经确认的新依赖
- [ ] 未破坏 LICENSE 与根 README 既有定位句
- [ ] 无机密文件进入暂存区
