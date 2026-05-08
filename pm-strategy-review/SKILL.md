---
name: pm-strategy-review
description: |
  PMWorkspace 策略取舍裁判。用于产品方向、产品简报、PRD、原型概念或范围决策，
  在设计或交付前需要被挑战时。审查野心、范围、定位、价值交换、信任、
  反指标、可行性、风险，并用扩大、保持、收缩或转向四种范围模式判断
  应该删除什么、保留什么、扩大什么，以及哪些必须由 PM 拍板。
---

# 策略取舍裁判

在原型或交付前挑战产品方向。目标是用明确的范围模式判断方向应该扩大、保持、收缩还是转向，并把最大策略矛盾转成一个 PM 可拍板的取舍，而不是默认堆更多功能。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-strategy-review`
- 契约版本：`1`
- 阶段：策略审查
- 定位：识别最大策略矛盾，选择范围模式，并把策略取舍转成产品动作。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `usage`
- `usage pm-strategy-review`
- `pmw-dashboard`
- `pmw-artifact`

### 必读共享协议

- `../pmworkspace-shared/references/adversarial-review.md`
- `../pmworkspace-shared/references/pm-decision-principles.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/runtime-kernel.md`

### 共享门槛

- 先读语言与本地化协议，中文用户默认使用中文字段、中文状态和中文建议。
- 复用 runtime run：子 skill 发现已有 current_run_id 时不得重新创建 run。
- 历史偏好、记忆和默认规则不能覆盖本轮事实、brief、Zoon、反指标、不可虚构项或证据门槛。
- 等待 Q、D、证据或用户确认时必须停住；不能假装已对齐、可出图或可交付。
- 不得把真实 token、ownerSecret、私密客户资料、内部录音、未脱敏截图或未脱敏 Zoon 内容写进公开仓库。

### 默认用户可见输出字段

- `策略审查结论`
- `最大策略矛盾`
- `范围模式`
- `建议姿态`
- `当前 D`
- `下一步`

### 内部审计字段（默认不展示）

- `产品动作`
- `策略取舍`
- `下一技能`
- `证据状态`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, avoid English labels; use Chinese headings, status values, and recommendations.

## Preamble

Run update and usage checks when platform scripts are available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-strategy-review >/dev/null 2>&1 || true
```

## Workflow

1. 读取当前产品简报或 `$pm-jobs` 对齐结果。
2. Read `../pmworkspace-shared/references/adversarial-review.md`.
3. Read `../pmworkspace-shared/references/decision-question-mode.md`.
4. Read `../pmworkspace-shared/references/scenario-experts.md` and use the dominant scenario lens.
5. Read `../pmworkspace-shared/references/product-memory.md`; use memory only as preference signal, not as fact source.
6. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 策略审查 stage fields.
7. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-strategy-review` 且没有当前 run，再创建 runtime run.
8. Build the 策略取舍控制器 from `adversarial-review.md`: 来源门槛、已确认事实、策略风险类型、3-5 个审查视角、最大策略矛盾、范围模式、建议姿态、产品动作、策略取舍、当前 D / 后续 D 队列、下一技能.
9. 如果来自 `$pm-jobs`，只接住产品追问交出的策略门槛：范围、价值交换、信任/风险、反指标、可行性、定位或业务冲突；不要重新展开 Q 诊断全流程。
10. If basic facts such as user, problem, main goal, anti-metric, or non-fiction boundary are missing, route back to `$pm-jobs` with one focused `Q`; do not use strategy review to invent missing facts.
11. Select 3-5 challenge lenses relevant to the strategy risk type and scenario, then identify one 最大策略矛盾.
12. Select one 范围模式 from adversarial-review.md: 扩大模式、保持模式、收缩模式 or 转向模式. Explain why this mode fits the 最大策略矛盾 and how it changes scope, value exchange, anti-metric protection, and non-fiction boundaries.
13. Present concrete strategy choices. Do not silently change scope, add promises, move anti-metrics, or include unsupported capabilities.
14. Convert every selected review lens into a product action: 删除、前置、后置、标注、禁止 or 实验验证.
15. 把“需要 PM 拍板”的点转成选择题；每轮只展开一个完整 `D`，其余只提示后续标题队列。策略 `D` 必须包含推荐项、选项、风险、会影响什么、进入产品简报的写法。
16. If strategy review resolves the tradeoff, route next to `$pm-brief` by default so the decision becomes part of the product contract. Handoff must include 范围模式、策略决策、最大策略矛盾、范围外、用户承诺边界、反指标保护、对原型的影响. If the brief is already aligned and only direction review was requested, route next to `$pm-prototype-shotgun` or `$pm-handoff`.
17. Log accepted strategy decisions with `pmw-log question` and `pmw-log decision` when platform scripts are available.

## Review Lenses

- 问题真实性和证据。
- 现状替代方案。
- 扩大范围还是收缩范围。
- 高摩擦或高成本动作前，是否先给价值。
- 信任、隐私和数据可信度。
- 业务冲突或指标游戏。
- 可行性和无法支持的承诺。
- 边界情况和失败状态。
- 设计系统匹配度。

## 输出

```text
策略审查结论：
- 我建议：
- 最大策略矛盾：
- 范围模式：扩大模式 / 保持模式 / 收缩模式 / 转向模式
- 建议姿态：扩大 / 保持 / 收缩 / 转向
- 为什么：
- 当前必须拍板：
- 进入产品简报的写法：

内部策略取舍控制面板（默认不展示，写入审计）：
- 状态：
- run_id：
- 来源门槛：
- 策略风险类型：
- 范围模式：
- 使用视角：
- 证据状态：
- 最强前提：
- 最弱假设：
- 产品动作：
- 策略取舍：
- 范围外：
- 用户承诺边界：
- 反指标保护：
- 对原型的影响：
- 当前 D：
- 后续 D 队列：
- 下一技能：
- 建议下一步：
```
