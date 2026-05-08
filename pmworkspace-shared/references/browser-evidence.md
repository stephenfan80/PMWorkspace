# 线上证据采集

PMWorkspace Browser Evidence Capture Lite 是轻量证据协议，不是新的浏览器自动化子系统。PMWorkspace 做原型前，应尽量把线上页面、竞品页面、Zoon 文档或可访问参考页转成可复用证据，而不是只依赖口头描述。

v1 保持简洁：不新增专用 CLI，不新增专用状态文件；统一复用 `pmw-artifact` 的 `browser_evidence` 产物和 `pmw-run event --type evidence` 的门槛事件。

## 适用场景

- 用户提供 URL、线上页面、Zoon、竞品页面或参考产品。
- 新页面承接现有流程、结果页、状态页、活动页或生产样式。
- 现有功能迭代需要保留生产视觉基线。
- 用户要求“参考这个页面”“按线上样式来”“像某个竞品”。

## 采集内容

用浏览器工具或截图能力获取：

- 页面目的和主要动作。
- 信息架构、模块顺序、状态区、底部动作。
- 字体层级、颜色、间距、组件密度、按钮模式。
- 表单字段、结果承诺、错误/空/成功状态。
- 必须保留和可以改动的区域。

## 记录方式

成功采集到线上流程截图、状态页、竞品参考或 Zoon 漂移证据时，登记为 Product Artifact Flow 的轻量产物：

```bash
pmw-artifact add --kind browser_evidence --title "线上参考：<页面/流程>" --status "已采集" --source-skill pm-brief --path "<截图路径>" --url "<线上 URL>" --summary "<页面任务、可复用基线、必须保留、可以挑战、不可复制>"
```

如果无法打开、缺少权限、用户尚未提供截图，或当前页面需要线上参考但材料不足，继续使用 run evidence 事件记录阻断原因：

```bash
pmw-run event --type evidence --status "缺失待补充" --title "线上参考" --summary "线上参考状态：读取失败/待补充"
```

`browser_evidence` 只保存可安全展示的 URL、脱敏路径和摘要；私密截图本体、内部 Zoon 正文、cookie、token、ownerSecret 和 API 原始响应不写入公开仓库。

## 输出结构

```text
线上证据摘要：
- 来源：
- 页面任务：
- 可复用视觉基线：
- 可复用交互模式：
- 必须保留：
- 可以挑战：
- 不可直接复制：
- 对产品简报的影响：
```

## 规则

- 线上证据只更新事实来源和视觉基线，不等于产品简报已对齐。
- 线上证据服务于 brief、原型、复审和交付准备度，不单独发展成采集平台。
- `pmw-dashboard readiness` 的 `线上参考` 行优先读取最新 `browser_evidence`；没有该产物时，回退到 `pmw-run event --type evidence` / `gate`。
- 内部页面、私密文档和客户截图只做脱敏摘要，不写入公开仓库。
- 竞品参考只能启发结构和表达，不复制品牌内容或私有素材。
- 如果无法打开或读取页面，标记 `线上参考状态：读取失败`，不要假装已看过。
