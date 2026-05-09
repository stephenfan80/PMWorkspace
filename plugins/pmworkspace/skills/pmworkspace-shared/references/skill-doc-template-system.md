# PMWorkspace Skill 文档生成体系

PMWorkspace 的 `SKILL.md` 仍保留人工写作的工作流判断，但共享门槛、前置检查和用户可见输出字段由 `pmw-gen-skill-docs` 统一生成和检查，避免 100+ eval fixture 已经进化、skill 文档却停留在旧口径。

## 设计原则

- **manifest 是共享契约源头**：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 定义每个 `$pm-*` skill 的阶段、定位、前置检查、必读共享协议、输出字段和共享门槛。
- **SKILL.md 是提交产物**：生成后的契约区块直接提交到各 `SKILL.md`，运行时无需再生成。
- **共享门槛压缩输出**：每个 `SKILL.md` 只写共享门槛真源和压缩摘要，完整条目留在 manifest，避免 8 个 skill 重复同一段长文。
- **人工工作流仍人工维护**：复杂判断、Q/D 规则、Zoon 流程、image-2 规则和交付边界仍写在正文；生成器只维护容易漂移的共享结构。
- **检查优先于重写**：`check` 会验证生成区块、preamble token、必读 reference 和输出字段，发现漂移直接失败。

## 命令

```bash
bin/pmw-gen-skill-docs list
bin/pmw-gen-skill-docs render --skill pm-brief
bin/pmw-gen-skill-docs write
bin/pmw-gen-skill-docs write --dry-run
bin/pmw-gen-skill-docs check
```

## 维护流程

1. 修改 `skill-docs.manifest.json`，把新增门槛、输出字段或前置检查写到对应 skill。
2. 运行 `bin/pmw-gen-skill-docs write` 更新所有 `SKILL.md` 的 `PMW-GENERATED-CONTRACT` 区块。
3. 运行 `bin/pmw-gen-skill-docs check`，确认生成区块和正文契约一致。
4. 新增或更新 eval fixture，确保关键行为不会回退。

## 漂移处理

如果 `check` 失败：

- `生成契约区块已漂移`：运行 `bin/pmw-gen-skill-docs write`，检查 diff 后提交。
- `前置检查缺少`：补齐 `## Preamble` 中的脚本调用，或从 manifest 删除不再需要的检查。
- `必读共享协议缺少`：在 `Workflow` 或 frontloaded protocol 中补充对应 reference。
- `输出字段缺少`：补齐用户可见输出结构，或修改 manifest 中的字段定义。

不要只手改生成区块；下一次 `write` 会覆盖它。
