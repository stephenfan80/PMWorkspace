# PMWorkspace Skill 文档生成体系

PMWorkspace 的 `SKILL.md` 仍保留人工写作的工作流判断，但共享门槛、前置检查和用户可见输出字段由 `pmw-gen-skill-docs` 统一生成和检查，避免 100+ eval fixture 已经进化、skill 文档却停留在旧口径。

## 设计原则

- **产品表达先于生成器**：先在 README、`routing.md`、`welcome-guide.md` 和对应方法 reference 中稳定用户心智、四动作、产物命名和默认输出，再同步 manifest 和生成区块。
- **manifest 是共享契约源头**：`pmworkspace-shared/skill-docs/skill-docs.manifest.json` 定义每个 `$pm-*` skill 的阶段、定位、前置检查、必读共享协议、输出字段和共享门槛。
- **manifest 不是第二套产品方法**：manifest 只镜像已稳定的共享字段、前置检查和审计字段；不要在 manifest 里发明新业务规则、用户话术或产品流程。
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

1. 先改用户可见产品表达：根 README、`routing.md`、`welcome-guide.md` 或对应方法 reference，确认 PMW 对外心智、默认输出和产物命名已经稳定。
2. 再修改 `skill-docs.manifest.json`，只把已稳定表达需要共享的门槛、输出字段或前置检查写到对应 skill。
3. 运行 `bin/pmw-gen-skill-docs write` 更新所有 `SKILL.md` 的 `PMW-GENERATED-CONTRACT` 区块。
4. 运行 `bin/pmw-gen-skill-docs check`，确认生成区块和正文契约一致。
5. 最后新增或更新 eval fixture，把已经稳定的产品表达锁成防回退断言；不要为了先让 eval 通过而反向改产品表达。

## 漂移处理

如果 `check` 失败：

- `生成契约区块已漂移`：运行 `bin/pmw-gen-skill-docs write`，检查 diff 后提交。
- `前置检查缺少`：补齐 `## Preamble` 中的脚本调用，或从 manifest 删除不再需要的检查。
- `必读共享协议缺少`：在 `Workflow` 或 frontloaded protocol 中补充对应 reference。
- `输出字段缺少`：补齐用户可见输出结构，或修改 manifest 中的字段定义。

不要只手改生成区块；下一次 `write` 会覆盖它。
