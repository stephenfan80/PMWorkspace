# Prototype Shotgun Board

Prototype Shotgun Board 用来比较页面方案，但比较对象首先是产品路径和实验假设，不是视觉风格。一个 board item 代表一个完整页面输出单元，同时不改变 image-2 输出规则：一个页面方案 + 一个屏幕仍然是一张独立图片。默认数量由 `brief_lock.image_output_mode` 决定：三页探索 / 三页实验需要 3 个页面输出单元，只有 `single_page_confirmed` 允许 1 个页面输出单元。

单图生成协议：一次 image-2 调用 = 一张图 = 一个完整页面输出单元 + 一个屏幕任务。批量生成只是顺序执行多个单图任务；`three_page_experiment` 必须拆成 3 个输出单元，`single_page_confirmed` 必须拆成 1 个输出单元。

## 记录方式

生成或计划生成每个图片单元前，平台脚本可用时登记：

```bash
pmw-controller preflight --target prototype --json
pmw-prototype-board add \
  --scheme "<方案名>" \
  --screen "<屏幕任务>" \
  --output-mode "<three_page_exploration|three_page_experiment|single_page_confirmed>" \
  --page-variant-role "<A/B/C 局部实验角色；单页时写主方案>" \
  --experiment-hypothesis "<本页面版本验证什么>" \
  --brief-version "<产品简报版本>" \
  --goal "<主目标>" \
  --anti-metric "<反指标>" \
  --non-fiction "<不可虚构项>" \
  --canvas-mode "<standard_first_screen|physical_longboard>" \
  --target-output-pixels "<无线上截图可空；有视觉基线时必须写目标输出画布>" \
  --generation-mode "<screenshot_edit|redraw>" \
  --base-image "<screenshot_edit 时写 visual_baseline 参考截图路径>" \
  --edit-scope "<screenshot_edit 时写只修改的目标区域 / 目标模块>" \
  --preserve-regions "状态栏、顶部导航、车系头图、车型切换、tab、底部吸底 CTA" \
  --product-path "<这条产品路径相信什么产品判断会成立>" \
  --behavior-assumption "<它相信什么用户行为会发生>" \
  --current-loss "<它主要解决什么当前损失>" \
  --tradeoff "<它主动牺牲、后置或不做什么>" \
  --prototype-thinking "<为什么这样设计，以及产品策略取舍>" \
  --information-architecture "<信息架构如何组织>" \
  --user-problem-fit "<如何帮助用户解决问题>" \
  --anti-metric-protection "<解决或保护哪个反指标风险>" \
  --design-score "<0-10 设计完整度评分>" \
  --design-gap "<距离 10/10 最大设计差距>" \
  --ten-out-of-ten-standard "<这张图达到 10/10 的具体标准>" \
  --prompt-design-fix "<本轮 image-2 prompt 如何补齐设计差距>" \
  --anti-ai-slop-constraints "<禁止的模板味 / 泛化视觉模式>" \
  --state-coverage "<默认 / 加载 / 空态 / 错误 / 成功 / 部分结果策略>" \
	  --first-second-third-hierarchy "<用户第一眼 / 第二眼 / 第三眼看到什么>" \
	  --unresolved-design-decision "<仍需 PM 拍板的设计选择，可空>" \
	  --design-spec-target "<用户提供 / AutoDesign / 平台模式库 / PMW 默认假设>" \
	  --design-system-profile "<具体设计系统或 PMW 平台模式库配置>" \
	  --platform-pattern "<Instagram / YouTube / TikTok / 抖音 / 大众点评 / 美团 / 不适用>" \
	  --inspiration-sources "<Dribbble / Pinterest / 公开页面 / 用户截图 / 未使用>" \
	  --inspiration-patterns "<抽象可复用布局、层级、交互、状态和信任模式>" \
	  --no-copy-boundary "<不得复制图片、品牌素材、文案、专有 UI 或未授权资产>" \
	  --image "<图片路径或 URL，可为空>" \
	  --status "计划生成"
```

脚本会把当前 controller 的 `run_id`、`task_digest`、`input_revision` 和 `controller_verdict` 写入 board item。没有当前 controller run，或 board item 只匹配旧任务时，该输出单元只能作为参考方案，不能进入 image-2 prompt、复审或交付。

`--output-mode`、`--page-variant-role`、`--experiment-hypothesis`、`--product-path`、`--behavior-assumption`、`--current-loss` 和 `--tradeoff` 是新写入记录的关键字段；这里的 product path 记录产品路径判断。脚本可从 brief lock 和方案名补默认值，但新输出单元必须能被 readiness 读成“一个完整页面实验版本”。

设计完整度字段第一阶段为可选字段，旧记录缺失时展示为 `未记录`。但 `$pm-prototype-shotgun` 的新输出必须写入 `--design-score`、`--design-gap`、`--ten-out-of-ten-standard`、`--prompt-design-fix`、`--anti-ai-slop-constraints`、`--state-coverage` 和 `--first-second-third-hierarchy`；否则只能标记 `方案比较板：设计完整度未写入`，不能声称已完成设计完整度判断。

设计规范目标字段为向后兼容的可选 CLI 参数，旧记录缺失时展示为 `未记录`。但新输出必须写入 `--design-spec-target`、`--design-system-profile`、`--platform-pattern` 和 `--no-copy-boundary`；如果使用 Dribbble、Pinterest、公开页面或平台模式库启发，还必须写入 `--inspiration-sources` 和 `--inspiration-patterns`。没有使用灵感来源时，显式写 `未使用 / 不适用`，避免下游误以为已经完成参考采集。

有 `visual_baseline` 时，`--canvas-mode` 必须是 `physical_longboard`，`--target-output-pixels` 必须写与当前 visual_baseline 一致的物理长板目标，例如 `1179 x >=2556` 或 `1179px 宽，高度不得低于 2556px`；不得写短画布锚点，具体禁用模式以 `pmw-prototype-prompt-check` 为准。

视觉还原优先、现有生产截图或截图修改任务默认使用 `--generation-mode screenshot_edit`。脚本在当前 run 有 `visual_baseline` 且未显式指定模式时会默认写入 `screenshot_edit`，并把 `--base-image` 默认绑定为 visual_baseline 参考图，`--preserve-regions` 默认绑定为 `状态栏、顶部导航、车系头图、车型切换、tab、底部吸底 CTA`。`--edit-scope` 必须由助手写清本次只改的目标区域；缺失时 Product Readiness Dashboard 不可出图。产品探索或大幅重构才显式使用 `--generation-mode redraw`。

生成后把图片路径或 URL 补写到同一个方案/屏幕单元：

```bash
pmw-image-preflight check --json
pmw-image-preflight issue-permit \
  --scheme "<方案名>" \
  --screen "<屏幕任务>" \
  --json
pmw-prototype-board image \
  --scheme "<方案名>" \
  --screen "<屏幕任务>" \
  --image-permit-id "<image_permit_id>" \
  --image "<图片路径或 URL>" \
  --status "已生成"
```

`image_permit_id` 是一次性的出图许可证（image_permit_id 是一次性的出图许可证）；每张图一个，必须匹配当前 run、`task_digest`、`input_revision`、方案名和屏幕任务。没有 permit、permit 不匹配或 permit 已使用时，图片只能作为普通对话附件，不能进入 prototype manifest、原型复审或交付。

如果当前 run 有 `visual_baseline` 且输出单元是 `physical_longboard`，`pmw-prototype-board image` 会自动调用 `pmw-image-audit`。审计失败时图片状态必须写成 `需要重出`，命令返回非 0；助手不能把这张图展示为交付结果。

`pmw-prototype-board image` 必须绑定回同一个当前 run / 当前 `task_digest` / 当前 `input_revision` 的输出单元。若没有 `ALLOW_IMAGE_PROMPT` preflight、没有 `image_permit_id`、或当前任务没有匹配输出单元，图片标为 `对话附件，不是 PMW 原型产物`：不能写入 prototype_manifest，不能进入 `$pm-prototype-review`，也不能被 `$pm-handoff` 当作交付依据。

用户反馈后记录评分：

```bash
pmw-prototype-board score --scheme "<方案名>" --score 4 --note "<用户评论>"
```

查看比较板：

```bash
pmw-prototype-board list
```

比较板列表必须展示完整出图判断：产品路径字段、设计评分、主要设计差距、10/10 原型标准、prompt 设计修正、状态覆盖、第一眼 / 第二眼 / 第三眼、反 AI 模板味约束、未决设计选择、设计规范目标、平台模式、灵感来源和禁止照搬项。缺字段时显示 `未记录`，方便 `$pm-prototype-review` 和 `$pm-handoff` 判断哪些内容不能作为最终交付依据。

## 方案要求

- 多方案必须在产品策略、信息架构、交互模型、信任模型或关键任务路径上不同。
- 多方案必须能落到不同产品策略、信息架构、交互模型、信任模型或关键任务路径。
- 不把配色、插画、圆角、卡片样式或风格皮肤包装成多方案。
- 出图数量必须满足 `brief_lock.image_output_mode`：三页探索 / 三页实验为 3 个完整页面输出单元，单页主方案为 1 个完整页面输出单元；旧的少于 3 条路径豁免文本不再放行。
- 每个方案必须包含 `产品路径`、`用户行为假设`、`要赢过的现状替代`、`当前损失`、`删除 / 牺牲 / 后置项`、`验证信号`、`失败信号`、`原型思考`、`信息架构设计思考`、`用户问题解决逻辑`、`反指标保护` 和 `不可虚构边界`。
- 每个方案必须说明它相信什么用户行为、要赢过哪个现状替代、解决什么当前损失、牺牲什么、保护哪个反指标，以及哪些内容不可虚构。
- 每个方案必须包含 `设计完整度评分`、`为什么是这个分数`、`距离 10/10 的最大差距`、`10/10 原型标准`、`本轮 prompt 如何补齐`、`反 AI 模板味约束`、`状态覆盖策略` 和 `第一眼 / 第二眼 / 第三眼信息层级`。
- 每个方案必须包含 `设计规范目标`、`设计系统 / 平台模式`、`灵感来源摘要`、`禁止照搬项` 和 `版权边界`。设计启发可以来自 Dribbble、Pinterest、公开页面、用户截图或平台模式库，但只能沉淀抽象模式，不能复制素材。
- 三页探索 / 三页实验必须同时是三种页面级设计判断：局部模块策略、信息架构、交互模型、信任模型、状态策略或降噪策略至少一项不同。不能只是在同一产品路径下替换配色、圆角、插画、卡片密度或文案语气。
- 方案质量规则不局限留资业务；社区、直播、产品库、交易、内容、工具、看板等场景也必须适用。
- 默认输出“方案对比表 + 单图清单”，不是拼图。
- 不允许把多个方案或多个屏幕合成一张三联图、并排比较图、一图多屏或多屏故事板。
- 只有用户明确要求展示材料时，才可以额外做展示板。
- 方案比较板是审计和比较记录，不是 image-2 图片的替代物。
- 每个 board item 必须能追溯到已对齐产品简报版本、主目标、反指标和不可虚构项。
- 每个 board item 必须能追溯到方案的产品路径、产品策略、信息架构、交互模型、信任模型或关键任务路径差异，不能只有视觉风格差异。
- 每个 board item 应能追溯到设计完整度目标：当前评分、10/10 标准、prompt 修正方向和反模板味约束。生成图复审时 `$pm-prototype-review` 要读取这些字段判断是否达标。
- 每个 board item 应能追溯到设计规范目标：用户提供、AutoDesign、平台模式库或 PMW 默认假设；平台模式和灵感来源不得替代产品路径差异。
- 每个 board item 在有线上截图视觉基线时，必须能追溯到 `canvas_mode=physical_longboard`、`target_output_pixels`、`generation_mode`、`base_image`、`edit_scope` 和 `preserve_regions`。
- 每个 board item 必须保留独立状态：`计划生成`、`已生成`、`生成失败`、`待重试` 或 `需要重出`；批量成功不能掩盖单张失败。
- 已登记的 board item 必须绑定当前 run、`task_digest`、`input_revision`、latest brief 的 `brief_path` 和 `brief_version`；旧版本 brief 或旧任务 revision 的输出单元必须重新登记，不能靠旧方案确认放行。
- 如果 `pmw-prototype-board add` 或 `pmw-prototype-board image` 不可用，原型计划必须写明 `方案比较板：未写入（原因）`，不能假装已经记录。
