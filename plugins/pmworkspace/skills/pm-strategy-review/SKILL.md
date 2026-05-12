---
name: pm-strategy-review
description: |
  PMWorkspace 产品方向审查。用于产品方向、产品简报、PRD、原型概念或范围决策
  在设计或交付前需要被挑战时，先做前提挑战、现状替代、不做推演和路径对比，
  再用扩大、选择性扩大、保持、收缩或转向判断应该保留、删除、扩大或拍板什么。
---

# 产品方向审查

在原型或交付前挑战产品方向。目标不是默认堆更多功能，而是先审前提、比较路径，再用明确范围模式判断方向应该扩大、选择性扩大、保持、收缩还是转向，并把范围或承诺变化转成一个 PM 可拍板的取舍。每轮必须做产品判断对抗校验，明确“如果现在直接做会错在哪里”，把最危险的产品误判转成范围模式、当前 D 或补证据动作。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-strategy-review`
- 契约版本：`2`
- 阶段：产品方向审查
- 定位：挑战产品方向，给出路径对比和范围模式，并把范围、承诺、实验或交付变化转成一个当前 D。

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

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 摘要：中文本地化、复用 `current_run_id`、记忆不覆盖本轮事实、等待 Q/D/证据/确认时停住、禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `策略审查结论`
- `产品信息对齐状态`
- `路径对比`
- `最大策略矛盾`
- `如果现在直接做会错在哪里`
- `产品判断对抗校验`
- `范围模式`
- `建议姿态`
- `本周期怎么验证`
- `本周期验证价值`
- `当前 D`
- `下一步`

### 内部审计字段（默认不展示）

- `产品信息对齐包`
- `前提挑战`
- `现状替代`
- `不做推演`
- `路径对比`
- `产品判断对抗校验`
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
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
fi
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-strategy-review >/dev/null 2>&1 || true
[ -n "$_PMW_BIN" ] && [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
```

## Workflow

1. 读取当前产品简报或 `$pm-jobs` 对齐结果。
2. Read `../pmworkspace-shared/references/adversarial-review.md`.
3. Read `../pmworkspace-shared/references/decision-question-mode.md`.
4. Read `../pmworkspace-shared/references/scenario-experts.md` and use the dominant scenario lens.
5. Read `../pmworkspace-shared/references/product-memory.md`; use memory only as preference signal, not as fact source.
6. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 策略审查 stage fields.
7. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-strategy-review` 且没有当前 run，再创建 runtime run.
8. 先读取或建立 `产品信息对齐包`，再 Build the 产品方向审查控制器 from `adversarial-review.md`: 来源门槛、已确认事实、产品信息对齐状态、前提挑战、现状替代、不做推演、路径对比、最大策略矛盾、如果现在直接做会错在哪里、产品判断对抗校验、范围模式、建议姿态、本周期验证、本周期验证价值、产品动作、策略取舍、当前 D / 后续 D 队列、下一技能.
9. 如果来自 `$pm-jobs`，只接住产品追问交出的策略门槛：范围、价值交换、信任/风险、反指标、可行性、定位或业务冲突；不要重新展开 Q 诊断全流程。
10. `$pm-strategy-review` 不展开研发能力依赖长清单；只判断能力前提是否改变方向、范围或承诺。详细数据 / 接口 / 算法 / 后台 / 运营依赖交给 `$pm-handoff` 的研发可行性反问。
11. If basic facts such as user, problem, main goal, anti-metric, or non-fiction boundary are missing, route back to `$pm-jobs` with one focused `Q`; do not use strategy review to invent missing facts.
12. Select 3-5 challenge lenses relevant to the strategy risk type and scenario, then identify one 最大策略矛盾. 把最大策略矛盾翻译成 `如果现在直接做会错在哪里`，说明直接进入 brief、原型或交付会误伤真实问题、价值交换、反指标、不可虚构边界或本周期承诺中的哪一项。随后完成 `产品判断对抗校验`：最危险的产品误判、我担心的想当然、可能的理解偏差、证据不足处、需要降级为假设的判断和建议动作。如果某个审查项无明显问题，明确写 `无明显问题` 或在审计标记已覆盖，不能跳过。
13. Before choosing a mode, present 2-3 paths from adversarial-review.md: 最小路径、增强路径、收缩 / 转向路径. Each path must state current loss, tradeoff, validation signal, failure signal, and non-fiction boundary.
14. Select one 范围模式 from adversarial-review.md: 扩大模式、选择性扩大模式、保持模式、收缩模式 or 转向模式. Explain why this mode fits the 最大策略矛盾 and 产品判断对抗校验结论, and how it changes scope, value exchange, anti-metric protection, and non-fiction boundaries.
15. Present concrete strategy choices. Do not silently change scope, add promises, move anti-metrics, or include unsupported capabilities.
16. Convert every selected review lens into a product action: 删除、前置、后置、标注、禁止 or 实验验证.
17. 把“需要 PM 拍板”的点转成选择题；每轮只展开一个完整 `D`，其余只提示后续标题队列。策略 `D` 必须包含推荐项、选项、风险、会影响什么、进入产品简报的写法。
18. Add 时间推演: 单功能默认 `1-2 周`，大规划默认 `1-3 个月`; write what must be verified in this cycle, what cannot become this-cycle commitment, and `本周期验证价值`: 验证后 PM 能决定继续、收缩、删除、转向、进入原型还是进入交付。
19. If strategy review resolves the tradeoff, route next to `$pm-brief` by default so the decision becomes part of the product contract. Handoff must include 范围模式、选中路径、策略决策、最大策略矛盾、产品判断对抗校验、范围外、用户承诺边界、反指标保护、本周期验证、对原型的影响. If the brief is already aligned and only direction review was requested, route next to `$pm-prototype-shotgun` or `$pm-handoff`.
20. Log accepted strategy decisions with `pmw-log question` and `pmw-log decision` when platform scripts are available.

## Review Lenses

- 问题真实性和证据。
- 现状替代方案。
- 不做推演。
- 路径对比。
- 扩大、选择性扩大、保持、收缩还是转向。
- 高摩擦或高成本动作前，是否先给价值。
- 信任、隐私和数据可信度。
- 业务冲突或指标游戏。
- 可行性和无法支持的承诺。
- 边界情况和失败状态。
- 设计系统匹配度。

## 输出

```text
策略审查结论：
- 产品信息对齐状态：
- 我不赞成：
- 我建议：
- 最大策略矛盾：
- 如果现在直接做会错在哪里：
- 产品判断对抗校验：
  - 最危险的产品误判：
  - 我担心的想当然：
  - 可能的理解偏差：
  - 证据不足处：
  - 需要降级为假设的判断：
  - 建议动作：
- 路径对比：
- 范围模式：扩大模式 / 选择性扩大模式 / 保持模式 / 收缩模式 / 转向模式
- 建议姿态：扩大 / 选择性扩大 / 保持 / 收缩 / 转向
- 为什么：
- 本周期怎么验证：
- 本周期验证价值：
- 当前必须拍板：
- 进入产品简报的写法：

内部产品方向审查控制面板（默认不展示，写入审计）：
- 状态：
- run_id：
- 来源门槛：
- 策略风险类型：
- 前提挑战：
- 现状替代：
- 不做推演：
- 路径对比：
- 产品判断对抗校验：
- 范围模式：
- 如果现在直接做会错在哪里：
- 使用视角：
- 证据状态：
- 最强前提：
- 最弱假设：
- 本周期验证：
- 本周期验证价值：
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
