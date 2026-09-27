# CONTRIBUTING.md — 贡献指南

感谢参与 MAHEA。贡献前请阅读 `rules/AGENTS.md` 及与改动相关的规则文件。

## 开始之前

1. Fork 本仓库；根目录模块结构即为你的项目起点。
2. 阅读 `rules/ARCHITECTURE.md` 了解分层，避免把逻辑塞进错误模块。
3. 涉及外部资料时遵守 `rules/SOURCE_POLICY.md`。
4. 命名遵守 `rules/NAMING.md`。

## 欢迎的贡献类型

- 补全模块 README / INDEX / 接口占位说明
- 新增或核验 `stock/` 素材卡（`pending` → `verified`）
- 完善 `docs/` 概念文档与融合说明（保持中性，不单点复刻）
- 示例（`examples/`）与无依赖脚本（`scripts/`）
- 治理、评测、观测、沙箱相关的接口与清单

## 不欢迎 / 需先讨论

- 引入未经 Issue/讨论确认的运行时依赖
- 将骨架改造成某一单一 Harness 的复制品
- 添加 `template/` 或数字前缀目录体系
- 大段粘贴受版权保护的原文

## 工作流建议

1. 用 `caps/skills/router` 确认改动应落在哪些模块。
2. 结构性缺口可先跑 `caps/skills/audit` 思路更新或引用 `docs/AUDIT.md`。
3. 提交与推送前阅读并遵守 `rules/git.rules`；用 `caps/skills/retro` 自查清单过一遍。
4. PR 描述写清：动机、触及模块、是否新增 stock、是否需要后续实现（深度 A 之外）。

## PR 检查清单

- [ ] 已阅读相关 `rules/`
- [ ] 模块 README 仍描述职责、接口、关系
- [ ] 新外部引用已登记 `stock/`
- [ ] 无数字前缀；无 `template/`
- [ ] 未擅自添加第三方依赖
- [ ] LICENSE（Apache-2.0）未被改写为不兼容条款

## 行为准则（简）

保持尊重、就事论事；对事不对人。安全与治理相关讨论优先走 `governance/` 与 Issue。
