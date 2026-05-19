# Product Readiness Dashboard

Product Readiness Dashboard 是 PMWorkspace 的出图 / 交付前总控面板。它采用证据化准备度面板的做法：不是把证据散列成清单，而是用 `Required`、`状态`、`证据`、`行动` 和 `Verdict` 统一判断现在能不能继续。默认短 verdict 还必须把第一阻断翻译成产品判断影响，告诉用户补齐后会解锁什么。

## 使用时机

- `$pm-autoplan` 推进到原型准备度或交付准备度时。
- `$pm-prototype-shotgun` 写 image-2 提示词或调用 image-2 前。
- `$pm-handoff` 输出 PRD、设计交付、实验方案或研发验收前。
- `$pm-brief` 准备把下一技能指向 `$pm-prototype-shotgun` 或 `$pm-handoff` 时。

平台脚本可用时优先运行：

```bash
pmw-controller preflight --target prototype --json
pmw-controller preflight --target handoff --json
pmw-dashboard readiness --target prototype
pmw-dashboard readiness --target handoff
pmw-dashboard status
```

`pmw-dashboard status` 默认输出简洁状态摘要，`pmw-dashboard status --details` 才内嵌完整 `PMWorkspace 产品准备度仪表盘`，避免用户只看到后台证据表。

`pmw-dashboard readiness --json` 还必须输出 `diagnostics`，用于恢复而不是继续硬跑：

```json
{
  "diagnostics": {
    "expected_context": {
      "run_id": "...",
      "task_digest": "...",
      "input_revision": "..."
    },
    "first_blocker_fingerprint": "...",
    "candidate_context": [],
    "mismatch_matrix": [],
    "recommended_recovery_command": "..."
  }
}
```

`candidate_context` 只展示旧 brief、旧 board、错 run artifact 等可参考材料；只有匹配 expected context 的 row 才能放行。`mismatch_matrix` 用来解释为什么某个看似存在的产物没有被识别为当前产物。若同一 blocker 连续失败并由 controller 返回 `RECOVERY_REQUIRED`，Agent 必须停住展示 diagnostics，不能继续尝试补写随机事件或重跑出图。

## 固定门槛

仪表盘至少展示以下门槛：

| 门槛 | 出图前 | 交付前 | 判断 |
|---|---|---|---|
| 当前任务 | Required | Required | 必须存在 controller active run，且 run 不能是已完成 / 可交付等 terminal 状态；`current_task_digest` 和 `current_input_revision` 是本轮唯一合法上下文。 |
| 产品简报 | Required | Required | 必须是当前 run / 当前 `task_digest` / 当前 `input_revision` 下的 `brief_lock=locked`；候选 brief、旧 aligned brief 或 Markdown 状态行只能显示为“待确认 / 可参考，不可放行”。 |
| 产品简报确认 | Required | Required | 当前 run 必须有 `brief_lock=locked`；不能只凭 Markdown 中出现 `已对齐` 放行。`boundary_change` 会把简报改成 `needs_relock`，只要求重新确认受影响边界。 |
| 当前操作 | Conditional | no | 存在 `prototype_revision` operation 时展示 operation 类型、继承的 locked brief / 设计规范 / 源图和本轮最小门槛；局部修改不得重跑目标模式、自动评审、产品方向或策略审查。 |
| 编辑合同 | Conditional | no | `prototype_revision` 必须有 `source_image`、`edit_scope`、`preserve_scope`，且修改区域和保留区域不能冲突；若 `boundary_change=true`，不签发 permit，退回 brief relock。 |
| Zoon | Conditional | Conditional | 未启用时使用本地已对齐 Markdown，不阻断出图 / 交付；已启用、已有 URL 或用户选择在线协作时，必须已同步且无实质漂移。 |
| 线上参考 | Required | Required | 已提供线上参考、已确认无线上参考，或明确不适用；未判断时不继续。优先读取最新 `browser_evidence` 产物，没有时回退到 run evidence / gate 事件。 |
| 视觉基线 | Conditional | Conditional | 已采集线上截图或生产视觉参考时必须登记 `visual_baseline`，包含参考尺寸和目标输出像素；缺视觉基线或缺目标像素时不写 image-2 prompt。新概念页且用户确认无参考时显示不适用。 |
| 输出单元绑定 | Conditional | Conditional | 已登记 prototype-board 输出单元时，必须匹配当前 run、`task_digest`、`input_revision`、`brief_path` 和 `brief_version`；旧 brief 版本的输出单元不能放行出图，旧任务的输出单元也不能放行出图。 |
| 输出画布 | Conditional | Conditional | 有 `visual_baseline` 时，当前 run 的 prototype-board 输出单元必须写 `canvas_mode=physical_longboard` 和 `target_output_pixels`，且不得含 `pmw-prototype-prompt-check` 定义的短画布锚点。 |
| 截图编辑模式 | Conditional | Conditional | 有 `visual_baseline` 且是已有功能迭代 / 视觉还原优先时，输出单元必须使用 `screenshot_edit`，绑定 `base_image`、`edit_scope`、`preserve_regions`；不能默认从零重画整页。 |
| 线上截图路径分析 | Conditional | Conditional | 有 `visual_baseline` 时，输出单元必须先说明线上截图信息架构、用户浏览路径、用户完成任务路径，再决定局部改造范围；未分析时不写 image-2 prompt。 |
| 生产基线改动证明 | Conditional | Conditional | 有 `visual_baseline` 时，输出单元必须说明当前线上问题、改动区域、为什么优于当前线上、保留 / 删除边界；证明不成立时不写 image-2 prompt。 |
| 方案差异 | Required | Required | 新原型工作流的输出数量和页面方案由 `brief_lock.image_output_mode` 决定；三页探索 / 三页实验必须是 3 张独立完整页面，单页主方案必须来自 `single_page_confirmed`。`prototype_revision` 使用 operation 的 `expected_output_units`，不强制三页实验。 |
| 原型设计完整度 | Required | Conditional | 出图前必须完成；交付前如存在 prototype-board 输出单元，则每个输出单元必须记录设计评分、主要设计差距、10/10 原型标准、prompt 设计修正、状态覆盖、第一眼 / 第二眼 / 第三眼和反 AI 模板味约束。缺失时不写 image-2 prompt，也不能把该原型作为交付依据。 |
| 设计规范目标 | Required | Conditional | 出图前必须明确并确认设计规范目标：用户提供、AutoDesign、平台模式库或 PMW 默认假设；每个输出单元必须写入设计系统 / 平台模式、灵感来源摘要和禁止照搬项。缺失或未确认时先给用户设计规范目标卡，或确认默认假设。 |
| 方案方向确认 | Required | Required | 当前 run 必须记录用户已确认或批准默认方案方向；未确认时不写 image-2 prompt。 |
| 不可虚构项 | Required | Required | 必须明确不能展示的能力、数据、承诺或动作。 |
| 数据佐证 | no | no | 有数据时登记 `data_evidence`；没有数据时不阻断，但必须提示 `未提供，存在未验证风险`，并把风险写入 brief 与原型不可虚构项。 |
| 原型图片审计 | Conditional | Conditional | 出图后若 `pmw-prototype-board image` 或 `pmw-image-audit` 返回 `需要重出`，该图不能作为交付结果展示，必须重出。 |
| 复审状态 | no | Required | 出图前展示但不阻断；交付前必须是 `可通过`，不能有需要重出、PM 拍板或补参考项。 |
| 研发可行性反问 | no | Required | 交付前必须完成能力依赖审查：功能承诺背后的数据、接口、算法 / 推荐、规则、权限、后台、运营、埋点、异常 / 空态和合规边界已分类处理。普通缺口可待补充；影响承诺或验收的能力缺口必须转当前 `D`、降级方案或退回 `$pm-strategy-review`。 |

可以追加 `待决策项`、`设计系统`、`交付资产` 等行，但不能省略以上固定行。

## Verdict 规则

- `READY_FOR_PROTOTYPE / 可出图`：新原型工作流中，产品简报、产品简报确认、线上参考、必要的视觉基线、输出画布、截图编辑模式、线上截图路径分析、生产基线改动证明、方案差异、原型设计完整度、设计规范目标及确认、方案方向确认和不可虚构项都通过；Zoon 未启用时使用本地简报，已启用时必须同步且无漂移；数据佐证缺失只提示未验证风险；复审状态仅展示，不阻断出图。`prototype_revision` 中，locked brief、设计规范目标、source image、edit scope、preserve scope 和 operation-scoped permit 通过即可出受影响单图 / 多状态图。
- `READY_FOR_HANDOFF / 可交付`：出图前门槛全部通过，且原型复审为 `可通过`，研发可行性反问已完成，关键 D 已拍板，交付缺口不会改变承诺或验收。
- `NOT_READY / 不可出图 / 不可交付`：任一 required 行未通过。输出必须给出第一条阻断行的行动建议，并路由到能补齐它的最早技能。

Dashboard 只读取 controller 当前 active run。若只找到旧 run、旧 product_brief、旧 visual_baseline、旧 prototype-board 或旧 review，状态必须写成 `可参考，不可放行`；不得因为资料充足就推断本轮产品已对齐。

## 默认输出契约

默认用户可见输出是一句人话 verdict，不展示完整门槛表：

```text
产品准备度结论：<可出图 / 不可出图 / 可交付 / 不可交付>（<出图前 / 交付前>）。<关键门槛已通过 / 卡在 第一条阻断门槛>；<判断价值 / 阻断影响>：<为什么这个 verdict 对当前产品判断重要>；解锁动作：<用户或 Agent 补齐什么后能继续>；下一步：<继续 / 补截图 / 回到产品简报 / 先复审>。
```

完整门槛表属于内部审计输出。用户明确要求“看状态 / 看审计 / 调试 / 展开证据”时，或开发者运行 `pmw-dashboard readiness --details` 时才展示。

## 详细输出契约

详细输出使用中文字段：

```text
PMWorkspace 产品准备度仪表盘：
- 目标：<出图前 / 交付前>
- 当前 run：
- Verdict：<可出图 / 不可出图 / 可交付 / 不可交付>
- 下一步：

| 门槛 | Required | 状态 | 证据 | 行动 |
|---|---|---|---|---|
| 当前任务 | YES | ... | ... | ... |
| 产品简报 | YES | ... | ... | ... |
| 产品简报确认 | YES | ... | ... | ... |
| Zoon | YES/no | ... | ... | ... |
| 线上参考 | YES | ... | ... | ... |
| 视觉基线 | YES/no | ... | ... | ... |
| 输出单元绑定 | YES/no | ... | ... | ... |
| 输出画布 | YES/no | ... | ... | ... |
| 截图编辑模式 | YES/no | ... | ... | ... |
| 线上截图路径分析 | YES/no | ... | ... | ... |
| 生产基线改动证明 | YES/no | ... | ... | ... |
| 方案差异 | YES | ... | ... | ... |
| 原型设计完整度 | YES | ... | ... | ... |
| 设计规范目标 | YES | ... | ... | ... |
| 方案方向确认 | YES | ... | ... | ... |
| 不可虚构项 | YES | ... | ... | ... |
| 数据佐证 | no | ... | ... | ... |
| 原型图片审计 | YES/no | ... | ... | ... |
| 复审状态 | YES/no | ... | ... | ... |
| 研发可行性反问 | YES/no | ... | ... | ... |
```

如果仪表盘显示缺口，不要用图片、PRD 或“后续补充”绕过。默认输出只给一句人话 verdict：第一条阻断原因、阻断影响、解锁动作和下一步；内部审计记录完整表格。把缺口转成一个 `Q`、一个 `D`，或退回 `$pm-brief`、`$pm-prototype-shotgun`、`$pm-prototype-review`、`$pm-handoff` 中最早能修复的技能。

仪表盘可以展示 Zoon URL 的存在和同步状态，但不得暴露 `token`、`ownerSecret`、Authorization header 或 API 原始响应内部信息。

## 与 Evidence Dashboard 的关系

Evidence Dashboard 回答“现在有哪些证据”；Product Readiness Dashboard 回答“基于这些证据，现在能不能出图或交付”。前者是证据页，后者是 gate verdict。两者可以同屏展示，但 Product Readiness Dashboard 必须放在出图 / 交付判断之前。

浏览器证据属于 Product Artifact Flow 的轻量产物：用 `pmw-artifact add --kind browser_evidence` 登记线上流程截图、状态页、竞品参考、设计启发或 Zoon 漂移证据。仪表盘只读取它的状态、URL / 路径和摘要，不引入新的证据库或浏览器自动化命令。设计启发场景必须在摘要中标明可复用模式、不可照搬项和版权边界，不能把外部图片、文案、品牌素材或专有 UI 当作可复制资产。

视觉基线属于出图控制产物：用 `pmw-artifact add --kind visual_baseline` 或 `pmw-image-audit baseline --reference <截图路径> --register` 登记参考图尺寸、截图倍率、逻辑点宽、目标输出像素、字号层级、页面边距、模块间距、底部栏高度和参考优先级。汽车之家 / AutoDesign 生产页中，线上截图基线高于泛化 AutoDesign token；默认使用参考截图原始物理像素和 3x 字体 / 间距比例，生成后还要用 `pmw-image-audit audit` 做尺寸 / 长板审计。视觉还原优先时，Product Readiness Dashboard 还会要求 prototype-board 输出单元使用 `generation_mode=screenshot_edit`，并绑定 `base_image`、`edit_scope` 和 `preserve_regions`。

有 `visual_baseline` 时，还必须登记 `线上截图路径分析`：当前截图的信息架构、用户浏览路径、用户完成任务路径；再登记 `生产基线改动证明`：当前线上方案哪里真的有问题、这张图只改哪些区域、为什么改完会优于当前线上、哪些区域必须保留或删除。用户只选择一个方向，或只补了截图，不等于已经证明新方案更好；证明不成立时应回到 `$pm-brief` / `$pm-strategy-review` 继续对齐，而不是把 Agent 的想象画成原型。
