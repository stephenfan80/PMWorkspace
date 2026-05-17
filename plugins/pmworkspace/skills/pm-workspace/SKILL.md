---
name: pm-workspace
description: |
  PMWorkspace 主入口，面向产品经理和设计师。用于把产品想法、PRD、Zoon 文档、
  截图、客户洞察或原型请求，先路由到全新功能或已有功能迭代，再统一进入深度
  产品对齐：先完成产品方向审查、产品简报确认和必要证据，再推进移动端优先
  image-2 原型、原型复审、产品设计文档、PRD 或交付稿。负责首次引导、更新检查、
  本地使用记录，并路由到 pm-jobs、pm-strategy-review、pm-brief、
  pm-prototype-shotgun、pm-prototype-review、pm-autoplan 或 pm-handoff。
  也用于用户刚安装 PMWorkspace 后需要欢迎引导、启动话术或选择第一步。v0.2 起
  负责启动 PMWorkspace runtime run，并把证据、决策、产物和下一步写入本地审计轨迹。
---

# PMWorkspace

PMWorkspace 是产品方案工作台：对齐、出图、复审、交付。它用于把原始产品上下文沉淀成可复用资产：产品简述、方案方向、原型提示词、image-2 屏幕、原型复审结论、产品设计文档、PRD 和交付稿。

<!-- PMW-GENERATED-CONTRACT:START -->
## PMWorkspace 生成契约

> 本区块由 `bin/pmw-gen-skill-docs` 根据 `pmworkspace-shared/skill-docs/skill-docs.manifest.json` 生成；不要手写修改。更新共享门槛、前置检查或输出字段后，运行 `bin/pmw-gen-skill-docs write`，再运行 `bin/pmw-gen-skill-docs check`。

- skill：`pm-workspace`
- 契约版本：`2`
- 阶段：主入口路由
- 定位：先判断全新功能 / 已有功能迭代，统一进入深度产品对齐，创建或衔接 run，并路由到最小可用的下一技能。

### 统一前置检查

- `_PMW_BIN`
- `pmw-update-check`
- `pmw-controller`
- `usage`
- `usage pm-workspace`
- `pmw-artifact`

### 必读共享协议

- `../pmworkspace-shared/references/runtime-kernel.md`
- `../pmworkspace-shared/references/pm-workbench-map.md`
- `../pmworkspace-shared/references/artifact-flow.md`
- `../pmworkspace-shared/references/pm-eval-system.md`
- `../pmworkspace-shared/references/routing.md`

### 共享门槛

- 真源：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 的 `shared_gates`。
- 快速更新：每个 skill 运行前用 `pmw-update-check --quick`；如果输出 `UPGRADE_AVAILABLE`，先询问用户是否执行 `UPGRADE_COMMAND`，除非 `auto_upgrade` 为 `true`。
- 运行时入口：每个 PMW 产品任务先过 `pmw-controller intake`，由 controller 判定是否继承或新建 run，并写入 `task_digest` / `input_revision`。
- STOP gate：`pmw-controller next` 返回 `ASK_CONFIRMATION`、`NEEDS_BASELINE`、`WRITE_PENDING_BRIEF`、`BRIEF_PENDING`、`D_REQUIRED` 或 `BLOCKED` 时必须停住，不能进入下游产物；`WRITE_PENDING_BRIEF` 只能路由到产品简报。
- 当前任务绑定：brief、visual baseline、prototype-board、review、handoff 和用户确认必须匹配当前 run、`task_digest` 与 `input_revision`；旧产物只能参考，不能放行。
- 摘要：中文本地化、记忆不覆盖本轮事实、只有 `ALLOW_IMAGE_PROMPT` 才能写 image-2 prompt，方向选择不能替代产品简报确认，禁止泄露 token/ownerSecret/私密资料。

### 默认用户可见输出字段

- `工作方式`
- `本轮价值时刻`
- `产品信息对齐`
- `产品作业卡`
- `关键缺口队列`
- `产品路径`
- `业务判断`
- `当前需要确认`
- `补齐后解锁`
- `下一步`

### 内部审计字段（默认不展示）

- `当前模式`
- `产品路径`
- `产品信息对齐包`
- `对齐深度`
- `当前门槛`
- `下一技能`
- `为什么`
- `run_id`
- `证据状态`
- `产物流动`
<!-- PMW-GENERATED-CONTRACT:END -->

Before user-facing output, read `../pmworkspace-shared/references/language-and-localization.md`. For Chinese users, use Chinese headings, labels, status values, and recommendations; keep English only for skill ids, commands, file paths, and precise technical terms such as `token`, `API`, `PRD`, `Zoon`, `image-2`, and `URL`.

## Entry Job

`$pm-workspace` 是 PMWorkspace 的入口，不是第二份产品规则表。入口只负责四件事：判断动作、启动或衔接 controller、展示工作方式卡片、路由到下一技能。

默认只向用户暴露四个动作：

| 动作 | 用户想完成的事 | 入口默认处理 |
|---|---|---|
| 对齐 | 把想法、PRD、截图或反馈变成可讨论产品判断。 | 判断产品路径和最早门槛，路由到 `$pm-autoplan`、`$pm-jobs`、`$pm-strategy-review` 或 `$pm-brief`。 |
| 出图 | 基于已对齐 brief 生成 image-2 原型图。 | 先交给 controller / readiness 判断；未放行时回到对齐门槛。 |
| 复审 | 判断原型是否可通过、重出或补参考。 | 路由到 `$pm-prototype-review`。 |
| 交付 | 生成产品设计文档、精简 PRD 或研发交付稿。 | 先确认复审和交付门槛，再路由到 `$pm-handoff`。 |

`$pm-workspace` 不做完整产品发现、不写产品简报正文、不写 image-2 prompt、不生成图片、不做原型复审、不写 PRD。复杂协议交给 `pmworkspace-shared/references/`、controller 和被路由到的子 skill。

## Required Sources

用户有具体产品任务时，跳过欢迎菜单，先读取共享真源再路由：

1. Read `../pmworkspace-shared/references/routing.md` as the only source for D0 产品路径、四动作路由、run 衔接和路由输出契约。
2. Read `../pmworkspace-shared/references/runtime-kernel.md` for controller authority, STOP gates, run owner rules, and audit boundaries.
3. Read `../pmworkspace-shared/references/pm-workbench-map.md` for the end-to-end stage map, shared state fields, and eval category alignment.
4. Read `../pmworkspace-shared/references/artifact-flow.md` so routed skills preserve upstream artifacts and downstream-readable handoffs.
5. Read `../pmworkspace-shared/references/pm-eval-system.md` only as a maintenance guardrail when changing PMW behavior or docs.
6. Read `../pmworkspace-shared/references/welcome-guide.md` only when the user has no concrete product task, asks what PMWorkspace can do, or needs first-run onboarding.

## Platform Preamble

Run this before routing when shell access is available:

```bash
_PMW_BIN=""
for _CANDIDATE in "$PWD/bin" "$PWD/pmworkspace-shared/bin" "$HOME/.codex/skills/pmworkspace-shared/bin" "$HOME/.agents/plugins/plugins/pmworkspace/skills/pmworkspace-shared/bin" $(find "$HOME/.codex/plugins/cache" -path "*/pmworkspace/*/skills/pmworkspace-shared/bin" -type d 2>/dev/null | sort -r); do
  if [ -x "$_CANDIDATE/pmw-update-check" ]; then _PMW_BIN="$_CANDIDATE"; break; fi
done
if [ -n "$_PMW_BIN" ]; then
  _UPD=$("$_PMW_BIN/pmw-update-check" --quick 2>/dev/null || true)
  [ -n "$_UPD" ] && echo "$_UPD"
  "$_PMW_BIN/pmw-log" usage pm-workspace >/dev/null 2>&1 || true
  [ -x "$_PMW_BIN/pmw-controller" ] && "$_PMW_BIN/pmw-controller" next --json 2>/dev/null || true
  [ -x "$_PMW_BIN/pmw-dashboard" ] && "$_PMW_BIN/pmw-dashboard" status 2>/dev/null || true
  [ -x "$_PMW_BIN/pmw-artifact" ] && "$_PMW_BIN/pmw-artifact" flow 2>/dev/null || true
fi
```

If output contains `UPGRADE_AVAILABLE old new`, tell the user PMWorkspace has an update. If output also contains `UPGRADE_COMMAND <command>`, offer that exact command; otherwise offer `pmw-upgrade --host codex`. If `auto_upgrade` is `true`, upgrade automatically with the detected command and say what changed only after upgrade succeeds.

## Routing Flow

After D0 and routing choose 产品路径, `$pm-workspace` must hand control to the runtime controller. Do not call `pmw-run start` directly for a product task; the controller decides whether the active project/run can be inherited or whether the new user materials require a new run / revision:

```bash
"$_PMW_BIN/pmw-controller" intake \
  --goal "<本轮产品目标>" \
  --materials "<本轮用户材料摘要>" \
  --skill pm-workspace \
  --product-path "<全新功能|已有功能迭代>" \
  --depth "deep" \
  --stage intake
"$_PMW_BIN/pmw-controller" next --json
```

If `pmw-controller next` returns `ASK_CONFIRMATION`、`NEEDS_BASELINE`、`WRITE_PENDING_BRIEF`、`BRIEF_PENDING`、`D_REQUIRED` or `BLOCKED`, stop at that gate and show the work mode card plus the first needed confirmation/evidence. If a child skill continues the workflow, do not finish the run in `$pm-workspace`; the child skill must reuse the current controller run/revision and finish only at a terminal readiness state. If scripts are unavailable, mark `运行审计：未启用`.

Record the full routing contract from `routing.md` in local audit: `当前模式`、`当前门槛`、`下一技能`、`为什么`、`run_id`、`证据状态`. Default user-facing output should show a short `工作方式` card plus `业务判断`、`产品作业卡`、`当前需要确认` and `下一步`; it must now also include `本轮价值时刻` and `补齐后解锁`, so users can see why PMW stops or routes.

## Welcome And First Run

If the user invokes `$pm-workspace` with no concrete product task, asks what PMWorkspace does, or has just installed it, read `../pmworkspace-shared/references/welcome-guide.md` and give the welcome message plus the first choice menu.

Do not make the user guess the command set. The first response should feel like an app onboarding screen: short orientation, the four actions `对齐 / 出图 / 复审 / 交付`, and one recommended next step.

If the user provides a product task in the same message, skip the welcome menu and route directly.

## Entry Hard Stops

These are entrance guardrails, not the full protocol. When one applies, stop and route to the source file / child skill listed in the generated contract.

- 写图片提示词或生成图片前，必须先完成产品简报对齐。
- 用户提供截图或线上参考时，只更新视觉基线和线上参考状态；不要自动产出完整方案、HTML 或原型图。
- 已有功能迭代缺线上截图、关键节点截图或等价视觉基线时，不输出 `方案 A / 方案 B / 方案 C`；先请求证据并解释补齐后解锁什么。
- 用户选择某个方案方向后再上传截图时，只代表“方向选择 + 新证据输入”，不代表产品简报已对齐；先进入 `线上基线接收`，再回到 `$pm-brief` 确认。
- 入口层默认只解释 5 个公开产品资产：`product_brief`、`visual_baseline`、`prototype_manifest`、`prototype_review`、`handoff`；完整 Product Artifact Flow 写入本地审计。
- 不要把真实 token、私密客户数据、内部录音、敏感截图或未脱敏 Zoon 内容保存到本地资产。

## Shared Source Index

Use `../pmworkspace-shared/references/README.md` as the index. Keep detailed rules out of this entry file:

| 真源 | 入口何时读取 |
|---|---|
| `routing.md` | 判断四动作、产品路径、下一技能和工作方式卡片。 |
| `runtime-kernel.md` | controller 权威、STOP gate、run owner 和审计边界。 |
| `pm-workbench-map.md` | 端到端阶段、共享状态字段和 eval 分类地图。 |
| `product-discovery-gate.md`、`production-reference-gate.md` | 已有功能、线上截图、产品作业卡和线上基线接收门槛。 |
| `artifact-flow.md`、`product-readiness-dashboard.md` | 产品资产流、出图 / 交付前 readiness 和默认简洁 verdict。 |
| `welcome-guide.md` | 空泛请求、刚安装或用户问 PMWorkspace 能做什么时。 |
| `pm-eval-system.md`、`skill-doc-template-system.md`、`update-workflow.md` | 维护、生成、评估、打包和升级时。 |
