# PMWorkspace Runtime Kernel

PMWorkspace 的技能必须像一个产品运行系统，而不是独立 prompt。每次关键工作都应留下可读、可审计、可继续的本地轨迹。

## 统一状态

所有 PMWorkspace 技能共享这些状态：

- `需要补充`：缺少会改变产品方向或交付质量的信息。
- `待确认`：已有推荐、假设或选择题，等待用户确认。
- `需要 PM 拍板`：存在会改变用户承诺、数据真实性、范围、实验口径、线索/交易/隐私/合规或验收标准的取舍。
- `基于假设，可讨论`：快速成型轻量包可用于讨论，但不是最终 PRD 或已验证事实。
- `已对齐`：用户确认了产品简报、关键假设或最新 Zoon 内容。
- `可进入原型复审`：已生成原型图片，下一步应复审。
- `需要补充参考`：缺少线上截图、设计系统、输出单元绑定或真实数据边界，不能凭印象继续。
- `需要重出`：原型违反产品简报、反指标、不可虚构项、线上参考或设计系统，需要回到原型方案重出。
- `可通过`：原型复审未发现硬违规，可进入交付准备。
- `可交付`：产品事实、原型选择和待决策项足以生成交付稿。

## 运行审计

平台脚本可用时，在选择模式后启动 run：

```bash
pmw-run start --skill <skill> --mode <quick|deep> --goal "<本轮目标>"
```

### Run Owner 协议

- `$pm-workspace` 是路由型会话的 run owner：完成 D0 工作方式判定和路由后，先创建 run，并记录当前门槛、证据状态和下一技能。
- 子 skill 发现已有当前 run 时复用当前 run，不再调用 `pmw-run start` 创建新 run。
- 用户直接调用子 skill 且没有当前 run 时，子 skill 才创建 run，skill id 使用自己的名称。
- 检查当前 run 时，可用 `pmw-project show` 查看 `current_run_id`；复用时 `pmw-run event` 可以省略 `--run`，由平台写入当前 run。
- 只有到达本轮终态时才调用 `pmw-run finish`；如果只是路由到下一技能、等待 D0/Q/D 回答或停在证据门槛，先记录 gate/evidence 事件，保留当前 run 供下一轮复用。

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

共享状态字段和阶段字段以 `pm-workbench-map.md` 为准；各技能可以追加自己的 controller 字段，但不能省略当前阶段的门槛、下一技能和证据状态。

不要因为脚本不可用而阻断产品流程；脚本不可用时，在输出里标记 `运行审计：未启用`。
