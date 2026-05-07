# Zoon 漂移检查

产品简报创建后，用户可能在对话或 Zoon 里继续调整 brief。PMWorkspace 必须把 Zoon 视为可编辑事实来源，并在原型或交付前检查本地 brief 是否落后。

## 什么时候检查

- `$pm-autoplan` 进入产品简报或原型准备度前。
- `$pm-prototype-shotgun` 写图片提示词前。
- `$pm-prototype-review` 复审图片前。
- `$pm-handoff` 生成交付稿前。
- 用户说“我改了 brief / 我在 Zoon 里调整了 / 按最新文档来”时。

## 工具优先

平台脚本可用时运行：

```bash
pmw-zoon drift --url "<Zoon URL>"
```

`pmw-zoon drift` 读取 Zoon 时应先对共享 URL 使用 `Accept: application/json`，从响应中提取 `markdown`、`revision`、`_links` 和 `agent` 信息；如果 JSON 内容协商失败，再回退到 `Accept: text/markdown`。不要假设固定 markdown 端点永远稳定。

结果含义：

- `IN_SYNC`：本地最新 brief 已同步到 Zoon，可继续。
- `DRIFT`：Zoon 或本地 brief 已出现差异；读取 Zoon 最新 Markdown，并递增产品简报版本。
- `NO_ZOON_URL`：没有在线事实来源；按本地 brief 推进，但标记 Zoon 状态。
- `NO_LOCAL_BRIEF`：缺少本地 brief；先生成或读取 Zoon 快照。
- `READ_FAILED`：Zoon 读取失败；不要假装已读取最新内容。

## 同步规则

保存产品简报时使用：

```bash
pmw-log brief "<功能名>"
```

`pmw-log brief` 会保存本地 Markdown，并在 `zoon_sync_on_brief` 未关闭时自动调用 `pmw-zoon sync`：

- 已有 Zoon URL：追加最新 brief。
- 没有 Zoon URL 且 `zoon_auto_create: true`：创建新 Zoon 文档。
- 同步失败：本地 brief 仍然有效，但输出必须标记 `Zoon 同步失败`。

同步前会按 `zoon_protocol_mode` 做协议发现：

- `dynamic`：默认，读取或刷新 `/skill` 和 `/agent-docs` 缓存。
- `cached`：只用缓存。
- `builtin`：只用内置 `/documents/*` 契约。

如果用户在对话中调整 brief，必须重新保存并同步；不能只在对话中改口径而不更新 Zoon。

## 版本规则

- 每次实质调整 brief，递增版本或写明“基于 Zoon 最新快照”。
- 如果 Zoon 中的人工修改改变目标、反指标、不可虚构项、屏幕范围或方案方向，回到对应 `Q` 或 `D`。
- 图片提示词必须引用最新已对齐版本；不能引用过期 brief。
