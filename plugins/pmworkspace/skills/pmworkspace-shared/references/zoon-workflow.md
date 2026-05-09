# Zoon 工作流

产品简报阶段默认使用 **local-first，Zoon-optional**：先保存本地 Markdown 业务简报和完整本地审计副本，让用户能快速继续原型或交付；本地保存成功后默认推荐 Zoon 的协作价值，并让用户用 A/B 选择是否同步；只有用户明确选择同步到在线协作文档、提供现有 Zoon URL，或当前任务需要多人在线协作时，才创建或更新 Zoon。创建或追加成功后让 `pmworkspace` agent 自动加入协作态，并在成功后自动打开到 Codex 内置浏览器。

这个规则的目标是减少真实执行时间卡点：Zoon 是协作增强，不是每次产品简报的默认阻断门槛。

## 原则

- 不硬编码 host、slug、token 或 agent ID。
- 不复用示例里的 token。
- 不把 Zoon token、用户内容、评论或私密文档写入公开仓库。
- 只读取当前任务需要的内容。
- 除非用户要求，不处理现有评论。
- 原型任务的最终输出仍是图片，但必须先完成产品简报对齐。
- 产品追问后创建的产品简报，默认先写入本地业务简报和本地审计副本；保存成功后必须推荐 Zoon 并解释价值，但不自动同步；如果用户选择在线协作，再同步业务简报版到 Zoon。
- 用户在对话中调整产品简报后，必须重新保存本地简报；只有已启用 Zoon 时才同步到 Zoon，不能只更新对话里的口径。
- 创建或更新 Zoon 成功后，必须先自动加入协作态，再尝试自动打开可编辑 URL；不能只保存本地 Markdown 后结束。
- `pmw-log brief` 默认只记录本地 latest brief 和完整审计副本，并把 `last_zoon_sync_status` 标记为 `disabled`；当 `zoon_sync_on_brief` 或 `PMW_ZOON_SYNC_ON_BRIEF` 显式开启时，再执行 `pmw-zoon sync` 并记录 `last_zoon_sync_status`、`last_zoon_sync_brief`、`last_zoon_join_status` 和 Zoon URL。
- 未启用 Zoon 时，出图 / 交付准备度中的 Zoon 行显示 `未启用，使用本地简报`，不作为阻断；已启用或已有 URL 时，才必须检查同步与漂移。

## 连接步骤

1. 先做可升级协议发现：
   - 默认读取 `<origin>/skill`，再读取 `<origin>/agent-docs`。
   - 使用 `pmw-zoon protocol --host <Zoon host-or-url>` 缓存协议摘要。
   - 网络失败时使用本地缓存；没有缓存时回退到内置 `/documents/*` 契约。
2. 解析 Zoon URL：
   - Host：scheme 和 domain。
   - Slug：`/d/` 后面的片段。
   - Share token：`token` 查询参数。
3. 进入协作态时先调用 `POST <host>/api/agent/<slug>/presence`，使用 `Authorization: Bearer <token>`、`x-share-token: <token>`、`X-Agent-Id: pmworkspace`，body 为 `{"agentId":"pmworkspace","name":"PMWorkspace","status":"active"}`。
4. 创建新文档使用当前协议推荐的 `POST <host>/documents`。
5. 写入时使用 `Authorization: Bearer <token>`、`X-Agent-Id: pmworkspace`、`Idempotency-Key` 和 `by: "ai:pmworkspace"`。
6. 追加产品简报优先使用 `POST <host>/api/agent/<slug>/edit/v2`，默认 `insert_at_end`，不做 rewrite；只有该 endpoint 返回 404/405 时才回退 `POST <host>/documents/<slug>/edit/v2`。
7. 原型或交付前读取最新文档，优先使用 `GET <host>/api/agent/<slug>/snapshot` 取 `markdown/revision/blocks/marks`，失败再回退共享 URL + `Accept: application/json`，最后回退 `Accept: text/markdown`。

## 协作模式

- 从 Zoon 文档中提取产品问题、证据和人工修改。
- 如果用户要求原型图片，先创建或更新产品简报，并确认对齐。
- 对齐完成后，继续生成图片，不用长 PRD 替代原型输出。
- 写入 Zoon 时使用 AI 作者身份，让人类能看到哪些内容由 PMWorkspace 写入。
- 如果 Zoon 中已有产品简报，且用户要求生成原型，先重新读取最新快照，再生成图片提示词。
- 如果本地产品简报和 Zoon 快照不一致，先按 `zoon-drift-check.md` 处理漂移。
- 不要从未确认、未批准为事实来源的 Zoon 产品简报生成原型。

## 产品简报创建

当产品追问已经产出产品简报时，默认先保存本地产品简报。随后必须用一个轻量选择推荐并询问是否同步到 Zoon。推荐文案要说明 Zoon 的好处：多人协作、事实源统一、后续 image-2 原型 / PRD 防漂移；同时说明不自动同步、不作为出图或交付阻断。

```text
Zoon 协作建议：这次简报适合多人评审 / 后续原型或 PRD 复用，建议同步到 Zoon；不同步也不影响继续使用本地 Markdown。

是否同步到在线协作文档（Zoon）？
A. 先不需要，使用本地 Markdown 继续出图 / 交付。
B. 需要，同步到 Zoon 供团队在线修改。
```

如果用户选择 A，不创建 Zoon，不打开浏览器，继续使用本地已对齐产品简报。
如果用户选择 B 或提供现有 Zoon URL，按下列 Zoon 流程执行。

### 可升级协议发现

Zoon 会升级，PMWorkspace 不应只依赖写死接口。平台脚本可用时，先运行：

```bash
pmw-zoon protocol --host "https://zoon.up.railway.app"
```

规则：

- 动态模式 `zoon_protocol_mode: dynamic`：缓存未过期时使用缓存，过期后重新拉取 `/skill` 和 `/agent-docs`。
- 缓存模式 `zoon_protocol_mode: cached`：只使用本地缓存，适合离线或固定版本调试。
- 内置模式 `zoon_protocol_mode: builtin`：使用 PMWorkspace 内置 `/api/agent/*` 优先契约，并保留 `/documents/*` 兼容路由。
- 默认缓存 TTL 是 `zoon_protocol_cache_ttl: 300` 秒。
- 兼容路由只做兜底；新集成优先 `/api/agent/<slug>/presence`、`/api/agent/<slug>/edit/v2`、`/api/agent/<slug>/snapshot`、内容协商和 `X-Agent-Id`。

### 自动加入协作态

当 Zoon create 或 append 成功并拿到可编辑 URL 后：

1. 先运行 `pmw-zoon join --url "<Zoon URL>"`，或由 `pmw-zoon create|append|sync|read` 内部自动触发同等 presence 调用。
2. 加入成功时记录 `last_zoon_join_status: joined`；presence endpoint 返回 404/405 时记录 `unsupported` 并按兼容路径继续。
3. presence 返回 401/403/422 或网络失败时记录 `failed` 和脱敏原因；出图 / 交付准备度中的 Zoon 门槛不通过。
4. 不把 `ownerSecret`、`agentInviteMessage`、Authorization header、`x-share-token` 或未脱敏 token 写入本地状态。

### 自动打开

当 Zoon create 或 append 成功并拿到可编辑 URL 后：

1. 确认 `pmworkspace` agent 已 joined 或 presence 明确 unsupported 后，优先使用 Codex 内置浏览器 / Browser Use 工具导航到该 URL。
2. 不要用本地 HTML、Markdown 文件或系统默认浏览器代替内置浏览器中的 Zoon 在线简报。
3. 如果内置浏览器工具不可用或打开失败，仍返回 Zoon URL，并在输出中写明 `浏览器打开状态：打开失败，可手动打开`。
4. 如果打开成功，在输出中写明 `浏览器打开状态：已打开`。

### 已有 Zoon 文档

如果用户提供了 Zoon 文档：

1. 使用现有 host、slug 和 token。
2. 除非用户要求新建，否则把产品简报追加到该文档。
3. 优先使用 append 操作；产品简报不需要块引用。
4. 追加成功后自动加入协作态，并自动打开该文档的可编辑 URL。
5. 告诉用户：这个 Zoon 文档现在是下一步原型的事实来源。

### 新建 Zoon 文档

如果没有现有文档：

1. 如果用户提供 Zoon host，使用用户提供的 host。
2. 如果没有 host，使用配置 `zoon_host`，默认 `https://zoon.up.railway.app`。
3. 用平台脚本创建文档，或显式开启同步：

```bash
pmw-zoon create --title "产品设计简报：<功能名>"
PMW_ZOON_SYNC_ON_BRIEF=true PMW_ZOON_AUTO_CREATE=true pmw-zoon sync --title "产品设计简报：<功能名>"
```

4. 只向用户返回可编辑 URL，不展示 API 原始响应。
5. 用 `pmw-project link-zoon <url>` 把链接保存到本地项目记录。
6. 推荐先使用 `pmw-log brief <功能名>` 保存本地产品简报；如果用户选择同步，再用 `PMW_ZOON_SYNC_ON_BRIEF=true PMW_ZOON_AUTO_CREATE=true pmw-log brief <功能名>` 或直接 `pmw-zoon create|sync` 发布业务简报版。
7. 创建成功后自动加入协作态，再自动打开可编辑 URL。
8. 如果创建失败，保留本地 Markdown，不阻塞下一步，并说明失败原因。

### 生成原型或交付前

如果本地项目记录里有 Zoon URL：

1. 使用 `pmw-zoon read --url <Zoon URL>` 读取最新 Markdown。
2. 把最新 Markdown 作为产品事实来源。
3. 如果用户修改了方向、约束或 PM 决策，更新本地产品简报版本。
4. 不只依赖过期聊天上下文。

### 漂移检查

原型或交付前运行：

```bash
pmw-zoon drift --url "<Zoon URL>"
```

如果返回 `DRIFT`，读取最新 Zoon 快照，递增产品简报版本，并把变化同步回本地资产。用户在对话中修改 brief 后，重新执行：

```bash
pmw-log brief "<功能名>"
```

### 失败处理

如果 Zoon 创建、追加或读取失败：

- 本地 brief 仍作为失败兜底保存。
- 简短说明“Zoon 创建失败，可稍后重试”或“Zoon 读取失败，暂用本地产品简报”。
- 如果已经拿到 URL 但浏览器打开失败，说明“Zoon 已创建，浏览器打开失败，可手动打开”。
- 不打印 token、ownerSecret 或 API 原始响应。
- 继续保存本地资产，避免中断工作流。
