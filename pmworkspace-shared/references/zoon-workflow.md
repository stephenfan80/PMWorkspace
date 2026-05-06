# Zoon 工作流

产品简报阶段默认自动创建或更新 Zoon 在线文档，并在创建/更新成功后自动打开到 Codex 内置浏览器，方便用户继续编辑。用户提供 Zoon URL 时，直接把该文档作为事实来源；用户未提供时，使用 `zoon_host` 创建新文档。

## 原则

- 不硬编码 host、slug、token 或 agent ID。
- 不复用示例里的 token。
- 不把 Zoon token、用户内容、评论或私密文档写入公开仓库。
- 只读取当前任务需要的内容。
- 除非用户要求，不处理现有评论。
- 原型任务的最终输出仍是图片，但必须先完成产品简报对齐。
- 产品追问后创建的产品简报，应在有 Zoon 文档时写入 Zoon，方便用户在图片生成前修改。
- 创建或更新 Zoon 成功后，必须尝试自动打开可编辑 URL；不能只保存本地 Markdown 后结束。
- 只有用户明确关闭 Zoon、平台脚本不可用或创建失败时，才能把 Zoon 状态标为未创建，并说明原因。

## 连接步骤

1. 解析 Zoon URL：
   - Host：scheme 和 domain。
   - Slug：`/d/` 后面的片段。
   - Share token：`token` 查询参数。
2. 写入时使用 `Authorization: Bearer <token>` 和 `X-Agent-Id: pmworkspace`。
3. 创建新文档使用 `POST <host>/documents`。
4. 追加产品简报使用 `POST <host>/documents/:slug/edit/v2`。
5. 原型或交付前读取最新文档，优先使用共享 URL + `Accept: text/markdown`。

## 协作模式

- 从 Zoon 文档中提取产品问题、证据和人工修改。
- 如果用户要求原型图片，先创建或更新产品简报，并确认对齐。
- 对齐完成后，继续生成图片，不用长 PRD 替代原型输出。
- 写入 Zoon 时使用 AI 作者身份，让人类能看到哪些内容由 PMWorkspace 写入。
- 如果 Zoon 中已有产品简报，且用户要求生成原型，先重新读取最新快照，再生成图片提示词。
- 不要从未确认、未批准为事实来源的 Zoon 产品简报生成原型。

## 产品简报创建

当产品追问已经产出产品简报时，默认创建或更新 Zoon 文档，让用户在线修改对齐。

### 自动打开

当 Zoon create 或 append 成功并拿到可编辑 URL 后：

1. 优先使用 Codex 内置浏览器 / Browser Use 工具导航到该 URL。
2. 不要用本地 HTML、Markdown 文件或系统默认浏览器代替内置浏览器中的 Zoon 在线简报。
3. 如果内置浏览器工具不可用或打开失败，仍返回 Zoon URL，并在输出中写明 `浏览器打开状态：打开失败，可手动打开`。
4. 如果打开成功，在输出中写明 `浏览器打开状态：已打开`。

### 已有 Zoon 文档

如果用户提供了 Zoon 文档：

1. 使用现有 host、slug 和 token。
2. 除非用户要求新建，否则把产品简报追加到该文档。
3. 优先使用 append 操作；产品简报不需要块引用。
4. 追加成功后自动打开该文档的可编辑 URL。
5. 告诉用户：这个 Zoon 文档现在是下一步原型的事实来源。

### 新建 Zoon 文档

如果没有现有文档：

1. 如果用户提供 Zoon host，使用用户提供的 host。
2. 如果没有 host，使用配置 `zoon_host`，默认 `https://zoon.up.railway.app`。
3. 用平台脚本创建文档：

```bash
pmw-zoon create --title "产品设计简报：<功能名>"
```

4. 只向用户返回可编辑 URL，不展示 API 原始响应。
5. 用 `pmw-project link-zoon <url>` 把链接保存到本地项目记录。
6. 创建成功后自动打开可编辑 URL。
7. 如果创建失败，保留本地 Markdown，不阻塞下一步，并说明失败原因。

### 生成原型或交付前

如果本地项目记录里有 Zoon URL：

1. 使用 `pmw-zoon read --url <Zoon URL>` 读取最新 Markdown。
2. 把最新 Markdown 作为产品事实来源。
3. 如果用户修改了方向、约束或 PM 决策，更新本地产品简报版本。
4. 不只依赖过期聊天上下文。

### 失败处理

如果 Zoon 创建、追加或读取失败：

- 在对话中保留产品简报。
- 简短说明“Zoon 创建失败，可稍后重试”或“Zoon 读取失败，暂用本地产品简报”。
- 如果已经拿到 URL 但浏览器打开失败，说明“Zoon 已创建，浏览器打开失败，可手动打开”。
- 不打印 token、ownerSecret 或 API 原始响应。
- 继续保存本地资产，避免中断工作流。
