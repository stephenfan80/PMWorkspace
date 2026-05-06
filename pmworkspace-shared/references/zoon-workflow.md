# Zoon Workflow

Use this when the user provides a Zoon document URL or asks to collaborate through Zoon.

## Principles

- Never hardcode host, slug, token, or agent ID.
- Do not reuse tokens from examples.
- Do not publish Zoon tokens, user content, comments, or private docs in open-source artifacts.
- Read only what is needed for the user's current task.
- Do not process existing comments unless the user asks.
- For prototype tasks, image generation remains the final output, but product-plan alignment happens first.
- 产品追问后创建的产品简报，应在有 Zoon 文档时写入 Zoon，方便用户在图片生成前修改。

## Connection Steps

1. Parse the Zoon URL:
   - Host: scheme and domain.
   - Slug: the segment after `/d/`.
   - Share token: the `token` query parameter.
2. Fetch the protocol once from `<host>/skill`.
3. Choose or generate an agent ID for this session.
4. Announce presence with the protocol's presence endpoint.
5. Use the required headers from the invite/protocol on every API request, usually:
   - `x-share-token: <share-token>`
   - `X-Agent-Id: <agent-id>`
6. Fetch the document snapshot only after the user gives a task that requires reading it.

## Design Collaboration Pattern

- Extract product problems and evidence from the Zoon doc.
- If the user asks for prototype images, first create or update the product brief and confirm alignment.
- Keep the plan concise; do not replace images with a long PRD once alignment is complete.
- If editing Zoon content, write new content as AI-authored additions where supported so the human can review or revise.
- 如果 Zoon 中已有产品简报，且用户要求生成原型，先重新读取最新快照，再生成图片提示词。
- Do not generate prototypes from a Zoon brief that has not been confirmed or explicitly approved as the source of truth.

## 产品简报创建

当产品追问已经产出产品简报，且用户需要可在线编辑资产时使用。如果用户提供了 Zoon 文档，优先自动写入该文档。

### Existing Zoon Doc

If the user supplied a Zoon doc:

1. Use the existing host, slug, and token.
2. Append the brief to the doc unless the user asks for a new doc.
3. Prefer append operations for product briefs; they do not require a snapshot or block refs.
4. Tell the user the doc is now the source of truth for the next prototype step.

### New Zoon Doc

If there is no existing doc:

1. Use the user's provided Zoon host if available.
2. If no host is provided, default to `https://zoon.up.railway.app`.
3. Create the document with:

```http
POST <host>/api/public/documents
Content-Type: application/json

{
  "title": "产品设计简报：<功能>",
  "markdown": "<产品简报 Markdown>"
}
```

4. Return only the editable `url` from the response.
5. Keep `ownerSecret` private if present.
6. Do not hand-assemble invite messages or expose raw tokens.

### Failure Handling

If Zoon creation or update fails:

- Keep the brief available in chat.
- Explain the failure in one sentence.
- Continue only if the user wants to retry or proceed without Zoon.

## Avoid

- Pre-reading a doc before the user gives a task.
- Listing doc-specific suggestions before being asked.
- Treating the Zoon doc as public data.
- Assuming the same endpoint shape across all Zoon deployments without reading `<host>/skill`.
- Generating prototypes from stale chat when the user has edited the Zoon brief.
