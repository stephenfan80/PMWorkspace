# product_agent 能力地图

本文件是 product_agent 的能力索引。Agent 处理路由或用户使用问题时优先读取本文件。

| 能力 | 典型用户说法 | 输入 | 输出 | 禁止跳转 |
|---|---|---|---|---|
| `product-agent-workspace` | “不知道从哪里开始”“帮我判断这个想法怎么推进” | 零散材料、目标、截图、PRD | 工作方式卡片、下一能力 | 不能直接出图或交付 |
| `product-agent-problem` | “这个想法值不值得做”“用户问题不清楚” | 想法、反馈、用户场景 | 真实问题、当前替代、损失、待确认问题 | 不能替用户拍板范围承诺 |
| `product-agent-autoplan` | “按推荐流程推进”“一次跑完整评审” | 产品任务和材料 | 当前最早门槛、建议路径、必要 Q/D | 不能跳过阻断门槛 |
| `product-agent-strategy-review` | “挑战一下范围”“风险在哪里”“是否该收缩” | 已知问题、目标、约束 | 范围模式、策略矛盾、当前 D | 不能在事实不足时写 brief |
| `product-agent-brief` | “整理成产品简报”“更新 brief” | 已确认判断、证据、策略决策 | `product_brief` 草稿或已对齐版本 | 未对齐不能放行原型 |
| `product-agent-prototype` | “做 3 个原型方向”“基于截图改方案” | 已对齐 brief、视觉基线、设计约束 | `prototype_manifest` 和单图任务 | 不能无 brief 写 prompt |
| `product-agent-prototype-review` | “看看这些图能不能用”“需不需要重出” | 原型图、brief、manifest、参考 | `prototype_review`、重出建议、PM 拍板项 | 不能只凭视觉通过 |
| `product-agent-handoff` | “整理成 PRD”“交给研发 / 设计” | 已对齐 brief、复审结论、补充材料 | `handoff`、精简 PRD、待补充项 | 不能虚构接口、埋点或验收 |

路由原则：先处理最早缺失门槛，再进入下游产物。

行业任务按需读取 `product-agent-shared/references/industries/` 下的场景包；这些场景包只补行业判断，不新增 skill，也不进入默认路由。
