---
name: pm-brief
description: |
  PMWorkspace 产品核心信息契约生成器。用于把产品对齐、产品追问输出、
  策略审查、PRD 笔记、Zoon 文档、截图或客户洞察，压缩成能指导原型、
  复审和交付的关键产品判断，并保留版本、事实来源、门槛和“已对齐”状态。
---

# 产品核心信息契约

创建后续原型、复审、交付稿和实验步骤都必须读取的产品核心信息契约。产品简报不是 PRD、会议纪要或信息仓库；它只把会影响原型、复审或交付的判断压缩准确。

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, call the artifact `产品简报`; keep `brief` only when referring to a technical file or existing English source.

## Preamble

可用时运行平台检查和使用记录：

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin"; do
  if [ -x "$_CANDIDATE/pmw-log" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-update-check" 2>/dev/null || true
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-log" usage pm-brief >/dev/null 2>&1 || true
```

## Workflow

1. Read `../pmworkspace-shared/references/product-plan-handoff.md`.
2. Read `../pmworkspace-shared/references/production-reference-gate.md`，并写入页面类型和线上参考状态。
3. Read `../pmworkspace-shared/references/pm-decision-principles.md` before deciding whether to write a brief, ask a D, or apply memory.
4. Read `../pmworkspace-shared/references/pm-eval-system.md` and preserve the brief gate contracts it lists.
5. Read `../pmworkspace-shared/references/pm-workbench-map.md` and use its 产品简报 stage fields.
6. Read `../pmworkspace-shared/references/runtime-kernel.md`; follow its Run Owner 协议：如果 `pmw-project show` 已有 `current_run_id`，复用当前 run；如果用户直接调用 `$pm-brief` 且没有当前 run，再创建 runtime run.
7. Read `../pmworkspace-shared/references/decision-question-mode.md` and turn PM decision items into choice questions.
8. Read `../pmworkspace-shared/references/internet-best-practice-research.md` and run lightweight internet best-practice research for the dominant scenario when tools are available.
9. Read `../pmworkspace-shared/references/zoon-workflow.md`.
10. Read `../pmworkspace-shared/references/zoon-drift-check.md`.
11. Read `../pmworkspace-shared/references/product-memory.md` and use `pmw-memory summary` when available.
12. 先建立产品简报契约控制器，记录 `来源门槛`、`已完成门槛`、`缺失门槛`、`事实/假设边界`、`策略决策写入`、`简报深度`、`下一技能` 和 `证据状态`；再压缩产品核心信息，避免把材料堆成大文档。
13. 如果来自 `$pm-jobs` 或 `$pm-strategy-review`，先接收上游输出的风险、范围、价值交换、信任/风险、反指标、可行性、定位、业务冲突和待决策队列。
14. 如果基础事实仍缺失，退回 `$pm-jobs`，只展开一个当前 Q，不写完整产品简报；如果策略取舍仍未拍板，退回 `$pm-strategy-review`，只展开一个当前 D。
15. 确认已完成工作目标模式、Q 诊断、前提确认和必要 D 拍板；如果缺失，只输出短对齐摘要、缺失门槛和下一技能，不写完整产品简报。
16. 如果已有 Zoon URL，先运行 `pmw-zoon drift` 或读取最新 Zoon 快照；Zoon 漂移如果改变目标、反指标、不可虚构项、范围、用户承诺或方案方向，确认状态退回 `待确认`，并回到 `$pm-jobs` 或 `$pm-strategy-review`。
17. 根据模糊程度、风险等级和证据状态选择快速版、标准版或深度版产品简报。简报深度只代表证据和风险处理深度，不代表内容越写越长；快速版、标准版、深度版都使用同一套核心信息。
18. 用户可见输出必须先给 `产品核心信息`，再给 `产品简报门槛`，最后给 `支持信息`。核心信息只保留会改变原型结构、复审判断、交付范围或用户承诺的内容；支持信息只承载来源、Zoon、线上参考、检索状态、已保存资产和证据边界，不能压过核心判断。
19. 产品核心信息必须包含一句话判断、目标用户 / 场景、核心问题 / 当前损失、当前替代方案、本次目标、反指标、策略选择、原型重点和不可虚构项。
20. 互联网案例启发只保留 `可借鉴原则`、`不可照搬` 和 `对原型影响`；参考来源放入支持信息。最佳实践不能覆盖当前 brief、Zoon、线上截图、反指标或不可虚构项。
21. 把已拍板的策略取舍写入对抗审查后的设计取舍、方案方向、范围外、决策记录和对原型的影响；未拍板的策略取舍只能放进当前 D 或后续 D 队列。
22. 已对齐且用户要原型时，下一技能是 `$pm-prototype-shotgun`；已对齐且用户要交付时，下一技能是 `$pm-handoff`；未对齐时停在 `$pm-brief` 或回到上游缺失门槛。
23. 从功能名或产品简报标题提炼中文项目名，并用 `pmw-project set-name "<中文项目名>"` 保存。
24. Save the brief with `pmw-log brief <name>` when platform scripts are available. This automatically creates or appends the brief to Zoon when `zoon_sync_on_brief` is enabled.
25. Create or update the Zoon online brief by default:
    - If a Zoon URL is already available, append the brief with `pmw-zoon append --url <url>`.
    - If no Zoon URL exists and `zoon_auto_create` is not explicitly disabled, create one with `pmw-zoon sync --title "产品设计简报：<功能名>"` or `pmw-zoon create --title "产品设计简报：<功能名>"`.
    - After a create or append succeeds, automatically open the editable Zoon URL in the Codex built-in browser when browser tools are available. Do not use HTML, local files, or a macOS default-browser fallback as a substitute for the Zoon online brief.
    - If browser opening fails, still return the editable URL and mark the open status as `打开失败，可手动打开`.
    - Do not leave the Zoon field as a passive uncreated state. If Zoon is disabled or creation fails, write `未启用（原因）` or `创建失败（原因）`.

## Alignment Rule

只有“已对齐”的产品简报才能进入图片提示词。用户未确认时，标记为“待确认”，并在生成原型前停止。未完成前提确认或关键 D 拍板时，确认状态不能写成“已对齐”。如果页面需要线上参考但状态是“缺失待补充”，确认状态不能写成“已对齐”。

如果产品简报契约控制器显示 `缺失门槛`、`策略决策写入：未完成`、`Zoon 漂移检查：有实质变化` 或 `事实/假设边界` 不清，确认状态不能写成“已对齐”，也不能进入 `$pm-prototype-shotgun` 或 `$pm-handoff`。

产品简报不是“已对齐”时，不写 image-2 提示词，不生成图片，不生成 HTML，不输出交付稿。

用户在沟通过程中调整产品简报后，必须重新运行 `pmw-log brief <name>` 保存并自动同步 Zoon；不能只在对话中更新口径。

## 输出

Return the smallest useful brief. 用户可见第一屏必须是核心信息先行，门槛和支持信息随后出现：

```text
产品核心信息：
- 一句话判断：
- 目标用户 / 场景：
- 核心问题 / 当前损失：
- 当前替代方案：
- 本次目标：
- 反指标：
- 策略选择：
- 原型重点：
- 不可虚构项：

产品简报门槛：
- run_id：
- 版本：
- 确认状态：
- 来源门槛：
- 简报深度：
- 缺失门槛：
- 策略决策写入：
- 当前 D：
- 后续 D 队列：
- 下一技能：
- 证据状态：
- 建议下一步：

支持信息：
- 信息来源：
- 事实/假设边界：
- 已确认前提：
- 工作目标模式：
- 页面类型 / 场景路由：
- 线上参考：
- 互联网案例启发：
  - 可借鉴原则：
  - 不可照搬：
  - 对原型影响：
- Zoon：
- Zoon 同步状态：
- Zoon 漂移检查：
- 浏览器打开状态：
- 已保存资产：
- 项目名称：
```
