# 原型质量检查

Use this after each image generation batch and before the final response. The goal is to catch beautiful but unusable prototype output.

For Chinese users, report the final check with Chinese labels such as `质量检查`、`已通过`、`需要重出`、`不可虚构`.

## 原型复审控制器

`$pm-prototype-review` 先建立原型复审控制器，再给出逐屏结论。控制器至少记录：

- `复审输入`：图片路径或 URL、方案名、屏幕任务、产品简报版本、Zoon 快照、线上参考、设计系统和 prototype-board item。
- `视觉审计`：有参考截图时记录 `visual_baseline`、参考图尺寸、目标输出像素、`pmw-image-audit` 结果和是否需要重出。
- `输出单元绑定`：每张图必须能追溯到一个 `方案 + 屏幕任务`，并绑定主目标、反指标、不可虚构项和产品简报版本；缺绑定时先标 `需要补充参考`，不能凭视觉印象通过。
- `可插拔专家`：策略、信任 / 风险、设计系统、数据可行性四个底盘专家必须分别给出短结论、最高严重度、证据、一句话判断和行动；不能合并成一段泛泛 PM 总评。
- `专家合并结论`：由 `$pm-prototype-review` 根据四个专家的最高严重度合并为 `可通过`、`需要重出`、`需要 PM 拍板` 或 `需要补充参考`；深度交付、高风险、批量交付、研发交付、生产流程或用户要求多角色 review 时，再追加 Product Review Squad 角色短结论。
- `Product Review Squad`：CEO、Eng、Design、DX、安全、QA、发布工程师七个角色各自输出短结论、最高严重度、证据和行动。
- `判定原因`：把问题归类为产品事实偏离、反指标风险、不可虚构违规、线上参考偏离、设计系统偏离、未决产品取舍或轻微偏好。
- `行动结论`：合并为 `可通过`、`需要重出`、`需要 PM 拍板` 或 `需要补充参考`。
- `修正方向`：对 `需要重出` 的屏幕输出给 `$pm-prototype-shotgun` 的简短修复 brief；只重出受影响的屏幕。
- `PM 拍板`：对用户承诺、数据真实性、范围、实验口径、线索/交易/隐私/合规边界未决的问题，输出一个当前 `D`，不能靠改图解决。
- `偏好沉淀`：只有用户反馈或复审确认的审美/结构偏好才写入 taste；事实错误、反指标、不可虚构项和 Zoon 漂移不能写成偏好。
- `反馈资产化`：把复审和用户反馈分成个人偏好、产品认知、PMWorkspace 进化建议和不应保存项；个人资产写入本地用户记忆，进化建议先生成本地脱敏待审稿。
- `证据状态`：产品简报、Zoon、线上参考、设计系统、prototype-board、图片资产、待决策项和记忆更新状态。

复审控制器的优先级：事实与门槛 > 产品取舍 > 可交付质量 > 用户偏好。偏好只能影响下一轮推荐，不能让违反产品简报、反指标、不可虚构项、线上参考或设计系统的图片通过。

## 对照产品简报检查图片

Check:

- 屏幕是否匹配已对齐的产品简报和场景路由？
- 是否遵守移动端优先的画布决策，或清楚说明为什么使用桌面端？
- 长结果页、报告页或详情页使用 `H > 874` 的移动长板不算违规；真正违规的是宽度不是 `402`、高度低于 `874`、内容被裁切 / 压缩 / 遮挡，或把长内容拆成拼图、多屏故事板。
- 有线上截图时，逻辑宽 `402` 不能代替输出像素审计；生成图宽度低于参考截图 95%、长板高度低于参考截图 95%、或目标输出像素缺失，至少标记 `需要重出`。
- 是否解决了声明的用户任务？
- 是否优化主目标，同时没有违反反指标？
- 现有功能迭代中，是否保留了当前基线里必须保留的元素？
- 是否避免了不支持的功能、假数据、假按钮或无法兑现的承诺？
- 是否诚实展示了估算、不确定性、资格判断或人工跟进？

## 对照 AutoDesign 检查图片

AutoDesign is the default production baseline. Check:

- If a production screenshot exists, run `pmw-image-audit audit --image <生成图> --reference <参考图>` before visual judgment. `需要重出` 的尺寸审计不能被“看起来还行”覆盖。
- Autohome screenshot baseline overrides generic AutoDesign tokens for typography hierarchy, spacing rhythm, card density, chart density, and bottom toolbar height.
- Primary blue, commercial orange, text colors, dividers, and background are plausible.
- Typography uses production-like Chinese UI hierarchy.
- Layout uses 8-point structure and 4-point detail rhythm.
- Buttons, forms, NavBar, cards, tags, result modules, and bottom bars look shippable.
- There is one dominant primary action unless comparison is the point.
- 没有过度渐变、过圆卡片、重阴影、装饰性填充或营销海报式布局。
- No overlapping text, cramped rows, broken alignment, distorted assets, or unreadable numbers.
- 中文字号、价格数字、车型标题、CTA、标签和辅助文字不得明显小于参考图；不能通过压缩文字和间距把更多模块塞进短图。

## 检查多方案任务

- 方案必须在产品策略或信息架构上不同，不能只是换颜色。
- 每个方案都要有清楚的名称和取舍。
- 每个方案/屏幕必须单独交付一张图，不能合成拼贴图或比较板。
- 可以把每张独立图片登记到 Prototype Shotgun Board，用表格比较方案；这不是把图片合成一张图。
- 表单/结果页组合必须共享一致的数据、语气和视觉系统。
- 如果某个方案只是另一个方案的轻微视觉变化，修改较弱的概念。

## PM Review Army / Product Review Squad

所有原型复审都读取 `pm-review-army.md`，先用策略专家、信任 / 风险专家、设计系统专家和数据可行性专家四个可插拔专家独立检查；平台脚本可用时用 `pmw-review-specialist add` 记录每个专家短结论，再用 `pmw-review-specialist summary` 汇总。批量交付或高风险原型复审时，再用 CEO、Eng、Design、DX、安全、QA、发布工程师七个 Product Review Squad 角色各自输出短结论，最后合并成 `可通过`、`需要重出`、`需要 PM 拍板` 或 `需要补充参考`。

专家和角色短结论必须独立表达，不能只写“同上”。合并结论使用最高严重度，不做平均分。

## 如果原型不合格

If a failure is material:

1. 简短指出问题。
2. 基于已对齐的产品简报和视觉基线修改图片提示词。
3. 只重新生成受影响的屏幕。
4. 不要让用户接受违反可行性、信任或设计系统质量的原型。

尺寸 / 长板硬失败包括：生成图宽度低于参考截图 95%、高度低于参考长板 95%、目标输出像素缺失、底部栏遮挡、内容裁切、中文字体明显压缩、图表坐标轴不可读。命中任一项时，复审结论至少是 `需要重出`。

## 偏好沉淀边界

复审后记录偏好时：

- `approved`：只记录用户明确喜欢或复审确认可复用的方案方向、信息架构、信任表达、视觉密度或文案风格。
- `rejected`：记录用户明确拒绝的方向或复审中发现的可复用反模式，必须脱敏并标明适用范围。
- 不要把“违反不可虚构项”“缺线上参考”“未决承诺口径”写成普通审美偏好；这些是门槛或 D 拍板。
- 如果同类偏好重复出现，再用 `pmw-memory add-learning` 沉淀短 learning，并注明适用边界。

## 反馈资产化

原型复审结束后，输出：

```text
反馈资产化：
- 可沉淀为个人偏好：
- 可沉淀为产品认知：
- 可回流 PMWorkspace：
- 不应保存：
- 已保存到：
```

分类规则：

- `个人偏好`：信息密度、信任表达、视觉风格、表单摩擦、结果页结构等表达偏好，写入 `pmw-memory add-feedback --type preference`。
- `产品认知`：可复用产品判断、反指标、不可虚构边界、场景机制经验，写入 `pmw-memory add-feedback --type product-cognition`。
- `PMWorkspace 进化建议`：值得产品化的技能规则、eval、输出结构或门槛判断，写入 `pmw-memory add-feedback --type pmworkspace-improvement`，必要时用 `pmw-memory draft-github-feedback` 生成本地待审稿。
- `不应保存`：事实错误、反指标风险、不可虚构违规、线上参考缺失、未决用户承诺、数据真实性、隐私或合规边界。

GitHub 回流默认只生成本地脱敏待审稿，不自动提交。草稿不得包含真实项目名、Zoon 正文、截图内容、客户信息、token、内部 URL 或未脱敏 PRD。

## 交付清单

After acceptable images are produced, keep the final note compact:

```text
原型交付清单：
- 产品简报来源：
- 简报版本 / 状态：
- 场景路由：
- 已生成屏幕：
- 方案方向：
- 质量检查：
- 关键假设：
- 不可虚构：
- PM 待决策：
```

交付说明只保留下一位产品经理、设计师或助手继续工作所需的信息。除非用户要求，不要写长篇理由。
