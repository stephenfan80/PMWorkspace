# PMWorkspace Runtime Kernel

PMWorkspace 的技能必须像一个产品运行系统，而不是独立 prompt。每次关键工作都应留下可读、可审计、可继续的本地轨迹。

## 统一状态

所有 PMWorkspace 技能共享这些状态：

- `需要补充`：缺少会改变产品方向或交付质量的信息。
- `待确认`：已有推荐、假设或选择题，等待用户确认。
- `基于假设，可讨论`：快速成型轻量包可用于讨论，但不是最终 PRD 或已验证事实。
- `已对齐`：用户确认了产品简报、关键假设或最新 Zoon 内容。
- `可进入原型复审`：已生成原型图片，下一步应复审。
- `可交付`：产品事实、原型选择和待决策项足以生成交付稿。

## 运行审计

平台脚本可用时，在选择模式后启动 run：

```bash
pmw-run start --skill <skill> --mode <quick|deep> --goal "<本轮目标>"
```

关键节点写入事件：

```bash
pmw-run event --type gate --status "待确认" --title "前提确认" --summary "<摘要>"
pmw-run event --type decision --status "已对齐" --title "D1 <标题>" --summary "<用户选择>"
pmw-run event --type evidence --status "需要补充" --title "线上参考" --summary "<缺口>"
pmw-run event --type artifact --status "基于假设，可讨论" --title "轻量包" --summary "<产物>"
pmw-run event --type review --status "需要重出" --title "原型复审" --summary "<问题>"
```

结束时写入下一步：

```bash
pmw-run finish --status "<统一状态>" --next "<建议下一步>"
```

## 输出协议

用户可见输出尽量包含：

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

不要因为脚本不可用而阻断产品流程；脚本不可用时，在输出里标记 `运行审计：未启用`。

