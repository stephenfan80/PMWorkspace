# 原型质量检查

Use this after each image generation batch and before the final response. The goal is to catch beautiful but unusable prototype output.

For Chinese users, report the final check with Chinese labels such as `质量检查`、`已通过`、`需要重出`、`不可虚构`.

## 对照产品简报检查图片

Check:

- 屏幕是否匹配已对齐的产品简报和场景路由？
- 是否遵守移动端优先的画布决策，或清楚说明为什么使用桌面端？
- 是否解决了声明的用户任务？
- 是否优化主目标，同时没有违反反指标？
- 现有功能迭代中，是否保留了当前基线里必须保留的元素？
- 是否避免了不支持的功能、假数据、假按钮或无法兑现的承诺？
- 是否诚实展示了估算、不确定性、资格判断或人工跟进？

## 对照 AutoDesign 检查图片

AutoDesign is the default production baseline. Check:

- Primary blue, commercial orange, text colors, dividers, and background are plausible.
- Typography uses production-like Chinese UI hierarchy.
- Layout uses 8-point structure and 4-point detail rhythm.
- Buttons, forms, NavBar, cards, tags, result modules, and bottom bars look shippable.
- There is one dominant primary action unless comparison is the point.
- 没有过度渐变、过圆卡片、重阴影、装饰性填充或营销海报式布局。
- No overlapping text, cramped rows, broken alignment, distorted assets, or unreadable numbers.

## 检查多方案任务

- 方案必须在产品策略或信息架构上不同，不能只是换颜色。
- 每个方案都要有清楚的名称和取舍。
- 每个方案/屏幕必须单独交付一张图，不能合成拼贴图或比较板。
- 可以把每张独立图片登记到 Prototype Shotgun Board，用表格比较方案；这不是把图片合成一张图。
- 表单/结果页组合必须共享一致的数据、语气和视觉系统。
- 如果某个方案只是另一个方案的轻微视觉变化，修改较弱的概念。

## PM Review Army

批量交付或高风险原型复审时，读取 `pm-review-army.md`，用策略专家、信任 / 风险专家、设计系统专家和数据可行性专家四个视角检查，再合并成 `可通过`、`需要重出` 或 `需要 PM 拍板`。

## 如果原型不合格

If a failure is material:

1. 简短指出问题。
2. 基于已对齐的产品简报修改图片提示词。
3. 只重新生成受影响的屏幕。
4. 不要让用户接受违反可行性、信任或设计系统质量的原型。

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
