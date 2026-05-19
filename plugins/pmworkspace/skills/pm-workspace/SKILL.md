---
name: pm-workspace
description: |
  PMWorkspace 主入口，面向产品经理和设计师。把产品想法、PRD、Zoon、
  截图、客户洞察或原型请求先收敛为四个动作：对齐、出图、复审、交付。
  入口负责首次引导、更新检查、启动或衔接 controller，并路由到 pm-jobs、
  pm-strategy-review、pm-brief、pm-prototype-shotgun、pm-prototype-review、
  pm-autoplan 或 pm-handoff；复杂产品协议由共享 references 和子 skill 执行。
---

# PMWorkspace

PMWorkspace 是产品方案工作台：对齐、出图、复审、交付。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 manifest 生成；不要手写修改。

- skill：`pm-workspace`；契约版本：`3`；阶段：主入口路由
- 定位：先判断全新功能 / 已有功能迭代，统一进入深度产品对齐，创建或衔接 run，并路由到最小可用的下一技能。

### 统一前置检查

- `_PMW_BIN`、`pmw-update-check`、`pmw-controller`、`usage`、`usage pm-workspace`、`pmw-artifact`

### 必读共享协议

- `../pmworkspace-shared/references/runtime-kernel.md`、`../pmworkspace-shared/references/pm-workbench-map.md`、`../pmworkspace-shared/references/artifact-flow.md`、`../pmworkspace-shared/references/pm-eval-system.md`、`../pmworkspace-shared/references/routing.md`

### 产品表达真源顺序

- 先稳定用户可见产品表达：根 README、routing.md、welcome-guide.md 或对应方法 reference 说明 PMW 对外心智、默认输出和产物命名。
- 再同步 skill 正文和 manifest：生成契约只承接已稳定表达需要共享的阶段、定位、前置检查、必读协议、输出字段和审计字段。
- 然后运行 pmw-gen-skill-docs write/check：让 SKILL.md 生成区块镜像 manifest，防止手写漂移。
- 最后补 eval fixture：把已经稳定的表达锁成防回退断言；不要先写 eval 反向牵引产品表达。

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 摘要：运行前更新检查；PMW 命中先过 trigger guard / operation router；只有 `new_product_workflow` 才 intake，流程内 operation 不重新 intake；STOP gate 必须停住；当前任务绑定 run / `task_digest` / `input_revision`；中文本地化、事实优先、等待门槛和隐私边界不能被跳过。

### 默认用户可见输出字段

- `工作方式`、`本轮价值时刻`、`产品信息对齐`、`产品作业卡`、`关键缺口队列`、`产品路径`、`业务判断`、`当前需要确认`、`补齐后解锁`、`下一步`

### 内部审计字段（默认不展示）

- `当前模式`、`产品路径`、`产品信息对齐包`、`对齐深度`、`当前门槛`、`下一技能`、`为什么`、`run_id`、`证据状态`、`产物流动`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese headings, labels, status values, and recommendations; keep English only for skill ids, commands, file paths, and precise technical terms such as `token`, `API`, `PRD`, `Zoon`, `image-2`, and `URL`.

## Entry Job

`$pm-workspace` 是 PMWorkspace 的入口，不是第二份产品规则表。入口只负责四件事：判断动作、启动或衔接 controller、展示工作方式卡片、路由到下一技能。

默认只向用户暴露四个动作：`对齐`、`出图`、`复审`、`交付`。`$pm-workspace` 不做完整产品发现、不写产品简报正文、不写 image-2 prompt、不生成图片、不做原型复审、不写 PRD。入口硬停短语只保留索引：写图片提示词或生成图片前，必须先完成产品简报对齐。用户提供截图或线上参考时，只更新视觉基线和线上参考状态；已有功能迭代缺线上截图、关键节点截图或等价视觉基线时，不输出 `方案 A / 方案 B / 方案 C`；方向选择 + 新证据输入 不能替代 brief 对齐；复杂协议交给 `pmworkspace-shared/references/`、controller 和被路由到的子 skill。

## Read Before Routing

具体产品任务只读最小真源：

- `../pmworkspace-shared/references/routing.md`：四动作、产品路径、下一技能和工作方式卡片。
- `../pmworkspace-shared/references/runtime-kernel.md`：controller 权威、STOP gate、run owner 和审计边界。
- Read `../pmworkspace-shared/references/welcome-guide.md` only when the user has no concrete task, just installed PMWorkspace, or asks what PMWorkspace can do.

维护、eval、产物流动或端到端地图问题再 Read `../pmworkspace-shared/references/pm-workbench-map.md`、Read `../pmworkspace-shared/references/artifact-flow.md`、`pm-eval-system.md` 或 `../pmworkspace-shared/references/README.md`。

## Runtime Preamble

Run this before routing when shell access is available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-entry-status" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
[ -n "$_PMW_BIN" ] && "$_PMW_BIN/pmw-entry-status" --skill pm-workspace --text "<本轮用户原话和材料摘要>" # trigger guard; internally runs "pmw-update-check" --quick
```

If output contains `UPGRADE_AVAILABLE old new`, tell the user PMWorkspace has an update. If output also contains `UPGRADE_COMMAND <command>`, offer that exact command; otherwise offer `pmw-upgrade --host codex`. If `auto_upgrade` is `true`, upgrade automatically with the detected command and say what changed only after upgrade succeeds.

## Routing

For a concrete task:

1. Decide the visible action: `对齐`、`出图`、`复审` or `交付`.
2. Use `routing.md` to decide `产品路径` and the earliest gate.
3. Hand control to controller; do not call `pmw-run start` directly.
4. If controller returns `ASK_CONFIRMATION`、`NEEDS_BASELINE`、`WRITE_PENDING_BRIEF`、`BRIEF_PENDING`、`D_REQUIRED` or `BLOCKED`, stop and show the work mode card plus the first needed confirmation/evidence.
5. If the workflow continues, route to the next `$pm-*` skill and keep the current controller run/revision for that child skill.

```bash
"$_PMW_BIN/pmw-controller" intake \
  --goal "<本轮产品目标>" \
  --materials "<本轮用户材料摘要>" \
  --skill pm-workspace \
  --product-path "<全新功能|已有功能迭代|待判断>" \
  --depth "deep" \
  --stage intake
"$_PMW_BIN/pmw-controller" next --json
```

Record the full routing contract from `routing.md` in local audit: `当前模式`、`当前门槛`、`下一技能`、`为什么`、`run_id`、`证据状态`. Default user-facing output should show a short `工作方式` card plus `业务判断`、`产品作业卡`、`当前需要确认` and `下一步`; it must now also include `本轮价值时刻` and `补齐后解锁`, so users can see why PMW stops or routes.

## Default Output

```text
工作方式：
当前动作：
本轮价值时刻：
业务判断：
当前需要确认：
补齐后解锁：
下一步：
```

Complete route details, `run_id`, evidence tables, Product Artifact Flow, Zoon state, readiness tables, and internal audit fields stay in local audit unless the user asks to view status, audit, or debugging details.

## Welcome

If the user invokes `$pm-workspace` with no concrete product task, asks what PMWorkspace does, or has just installed it, read `../pmworkspace-shared/references/welcome-guide.md` and give the welcome message plus the first choice menu.

Do not make the user guess the command set. The first response should feel like an app onboarding screen: short orientation, the four actions `对齐 / 出图 / 复审 / 交付`, and one recommended next step. 用户有具体产品任务时，跳过欢迎菜单；if the user provides a product task in the same message, route directly.
