# PMWorkspace Runtime Kernel

PMWorkspace 的技能必须像一个产品运行系统，而不是独立 prompt。每次关键工作都应留下可读、可审计、可继续的本地轨迹。

## 统一状态

所有 PMWorkspace 技能共享这些状态：

- `需要补充`：缺少会改变产品方向或交付质量的信息。
- `待确认`：已有推荐、假设或选择题，等待用户确认。
- `需要 PM 拍板`：存在会改变用户承诺、数据真实性、范围、实验口径、线索/交易/隐私/合规或验收标准的取舍。
- `待确认`：已有推荐或候选简报，但本轮产品事实、前提或视觉基线仍未确认，不能出图或交付。
- `已对齐`：用户确认了产品简报、关键假设或最新 Zoon 内容。
- `可进入原型复审`：已生成原型图片，下一步应复审。
- `需要补充参考`：缺少线上截图、设计系统、输出单元绑定或真实数据边界，不能凭印象继续。
- `需要重出`：原型违反产品简报、反指标、不可虚构项、线上参考或设计系统，需要回到原型方案重出。
- `可通过`：原型复审未发现硬违规，可进入交付准备。
- `可交付`：产品事实、原型选择和待决策项足以生成交付稿。

## Controller Authority

PMWorkspace 的运行时真源是 `pmw-controller`，不是单个 skill 的口头判断、全局 `current-project` 或历史 latest artifact。每个产品任务进入 PMW 时都必须先完成 intake：

```bash
pmw-controller intake \
  --goal "<本轮目标>" \
  --materials "<本轮用户材料摘要>" \
  --skill <skill> \
  --product-path "<全新功能|已有功能迭代>" \
  --depth "deep" \
  --stage "<当前阶段>"
pmw-controller next --json
```

controller 会写入 `project.json` 的 `current_task_digest`、`current_input_revision`、`current_task_goal`、`current_stage`、`allowed_next_action` 和 `last_controller_verdict`。如果当前 active run 已完成、目标语义不匹配或材料 revision 变化，controller 必须创建新 run 或新 revision；旧 brief、旧 board、旧 review 只能作为参考，不能放行本轮。

`pmw-controller next --json` 必须返回 `workflow_stage`、`allowed_next_skill`、`allowed_user_visible_action`、`first_blocker`、`required_user_action`、`can_write_brief`、`can_register_prototype_units`、`can_issue_image_permit` 和 `can_handoff`。skill 只看这些能力位推进：`can_write_brief=false` 时不能保存已对齐 brief；`can_register_prototype_units=false` 时不能登记 prototype-board；`can_issue_image_permit=false` 时不能写 image-2 prompt；`can_handoff=false` 时不能输出 PRD / 产品设计文档。

正式阶段顺序固定为：

```text
intake
-> path_pending
-> goal_mode_pending
-> autoplan_review
-> product_direction_review
-> strategy_review
-> discovery_pending
-> brief_pending
-> brief_confirmation_pending
-> design_spec_pending
-> prototype_readiness_pending
-> prototype_units_pending
-> image_prompt_allowed
-> prototype_generated
-> prototype_review_pending
-> handoff_readiness_pending
-> delivered
```

`discovery_pending` 中的线上 / 视觉基线是“已对齐 brief、原型和交付”的硬门槛，不再提前拦住 `$pm-jobs`。已有功能迭代缺当前生产截图、关键节点截图、线上 URL、Figma / 设计稿或等价视觉基线时，controller 仍会在写已对齐 brief 前返回 `NEEDS_BASELINE`；但自动产品评审之后必须先允许产品方向审查和必要策略审查，把缺基线写入产品作业卡和后续阻断。

`pmw-controller next` 返回以下动作时是 STOP gate：`ASK_CONFIRMATION`、`NEEDS_BASELINE`、`WRITE_PENDING_BRIEF`、`BRIEF_PENDING`、`D_REQUIRED`、`BLOCKED`、`GOAL_MODE_REQUIRED`、`AUTOPLAN_REQUIRED`、`PRODUCT_DIRECTION_REQUIRED`、`STRATEGY_REVIEW_REQUIRED`、`DESIGN_SPEC_REQUIRED`、`REGISTER_PROTOTYPE_UNITS`。skill 必须停住并向用户展示当前最早门槛，不能继续进入下游产物、image-2 prompt、原型图、PRD 或交付稿。`WRITE_PENDING_BRIEF` 只表示下一步应进入 `$pm-brief` 写候选产品简报并等待用户对齐，不是原型许可。

只有 `ALLOW_IMAGE_PROMPT` 是 image-2 出图许可。实际生成前还必须基于它签发单图 `image_permit_id`。`方案方向确认`、用户回复 `A/B/C`、`按这些假设继续`、`REGISTER_PROTOTYPE_UNITS` 或 `WRITE_PENDING_BRIEF` 都不能替代当前 `input_revision` 下的产品简报确认。

出图和交付前统一跑 preflight：

```bash
pmw-controller preflight --target prototype --json
pmw-controller preflight --target handoff --json
pmw-controller preflight --target brief --json
```

`preflight --target handoff` 除了读取 Product Readiness Dashboard，还必须由 controller 自己核验当前 revision 已有 `prototype_manifest` 和 `prototype_review=可通过 / 可交付`，且没有需要重出、PM 拍板或补参考项。任一项缺失时，controller 返回 `HANDOFF_ARTIFACTS_REQUIRED`，`can_handoff=false`。

关键确认用 controller 写当前 revision 事件：

```bash
pmw-controller confirm --kind goal_mode --value "<验证价值|优化线上指标|业务评审|设计评审|研发交付>"
pmw-controller confirm --kind autoplan --summary "<自动产品评审结论和最早门槛>"
pmw-controller confirm --kind product_direction --summary "<PM 判断摘要>"
pmw-controller confirm --kind strategy --summary "<范围模式和策略 D>"
pmw-controller confirm --kind design_spec --value "<AutoDesign|用户截图/Figma/线上基线|PMW 推荐规范>"
pmw-controller confirm --kind brief --summary "<关键前提已确认或按标注假设推进>"
```

`confirm` 不是“盖章命令”。`autoplan` 必须写入 `我建议 / 当前最早门槛 / 下一技能`，`product_direction` 必须写入 `前提 / 现状替代 / 当前损失 / PM 判断`，`strategy` 必须写入 `范围模式 / 最大策略矛盾 / 策略 D`。缺结构字段时 controller 必须拒绝确认，避免用一句“已确认”伪造中段产品判断。

下游脚本写正式产物前必须读取 controller 能力位：

```bash
pmw-controller assert --capability write_brief
pmw-controller assert --capability register_prototype_units
pmw-controller assert --capability issue_image_permit
pmw-controller assert --capability handoff
```

所有正式产物和确认都必须绑定当前 `task_digest` / `input_revision`。脚本可用时，`pmw-run event`、`pmw-artifact` 和 `pmw-prototype-board` 会自动 stamp 当前 controller verdict；脚本不可用时，助手也必须在审计中声明这些绑定，不能把旧 run 的确认搬到新任务上。

历史资产默认分为 `candidate_context`，状态显示为 `历史资产：可参考，不可放行`。只有用户明确确认沿用、controller 记录当前 `input_revision` 的 `adopt_history` 事件、再运行 `pmw-controller adopt-history --kind <artifact-kind>` 把产物重新 stamp 当前 run / task / revision，并重新通过 readiness，才能成为 `current_artifact`。

## 运行审计

平台脚本可用时，在选择模式后由 controller 启动或继承 run；不要绕过 controller 直接用 `pmw-run start` 放行产品任务。底层 run 命令仍用于记录事件和终态：

```bash
pmw-controller intake --goal "<本轮目标>" --materials "<本轮材料摘要>" --skill <skill> --depth deep
```

### Run Owner 协议

- `$pm-workspace` 是路由型会话的 run owner：完成 D0 工作方式判定和路由后，先调用 `pmw-controller intake`，并记录当前门槛、证据状态和下一技能。
- 子 skill 发现已有当前 run 时复用当前 run，但必须先通过 controller 检查当前 `task_digest` / `input_revision` 是否匹配；匹配才复用，不匹配则由 controller 建立新 run 或 revision。
- 用户直接调用子 skill 且没有当前 run 时，子 skill 也先调用 `pmw-controller intake`，skill id 使用自己的名称。
- 检查当前 run 时，可用 `pmw-project show` 查看 `current_run_id`；复用时 `pmw-run event` 可以省略 `--run`，由平台写入当前 run。
- 只有到达本轮终态时才调用 `pmw-run finish`；如果只是路由到下一技能、等待 D0/Q/D 回答或停在证据门槛，先记录 gate/evidence 事件，保留当前 run 供下一轮复用。

关键节点写入事件：

```bash
pmw-run event --type gate --status "待确认" --title "前提确认" --summary "<摘要>"
pmw-run event --type decision --status "已对齐" --title "D1 <标题>" --summary "<用户选择>"
pmw-run event --type evidence --status "需要补充" --title "线上参考" --summary "<缺口>"
pmw-run event --type artifact --status "待确认" --title "候选产物" --summary "<产物>"
pmw-run event --type review --status "需要重出" --title "原型复审" --summary "<问题>"
pmw-run event --type task_intake --status "已记录" --title "任务入口" --summary "<目标与材料摘要>"
pmw-run event --type task_revision --status "已更新" --title "任务材料更新" --summary "<revision 摘要>"
pmw-run event --type workflow_transition --status "已进入" --title "<阶段>" --summary "<下一合法动作>"
pmw-run event --type stop_gate --status "待确认" --title "<STOP gate>" --summary "<为什么停住>"
pmw-run event --type preflight_verdict --status "不可出图" --title "prototype preflight" --summary "<第一阻断>"
```

结束时写入下一步：

```bash
pmw-run finish --status "<统一状态>" --next "<建议下一步>"
```

## 输出协议

用户可见输出默认只包含业务判断、当前需要用户确认的一件事、已生成的可用产物和下一步：

```text
- 结论：
- 当前需要确认：
- 已生成产物：
- 下一步：
```

运行字段默认进入本地审计，不直接展示给用户：

```text
- run_id：
- 模式：
- 状态：
- 当前门槛：
- 已确认假设：
- 证据状态：
- 已记录决策：
- 产物清单：
- 建议下一步：
```

共享状态字段和阶段字段以 `pm-workbench-map.md` 为准；各技能可以追加自己的 controller 字段，但默认写入 `pmw-run`、`pmw-dashboard --details` 或本地审计副本。只有用户明确要求“看状态 / 看审计 / 调试 / 展开证据”时，才输出 run、门槛、证据状态或产物流动表。

不要因为脚本不可用而阻断产品流程；脚本不可用时，优先继续业务流程，只有影响可追溯交付时才简短说明 `运行审计未启用`。
