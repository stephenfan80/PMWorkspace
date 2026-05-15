# 更新工作流

Every PMWorkspace skill should run a fast update check before doing product work when platform scripts are available.

## PMW 版本身份

PMWorkspace 有两个版本层级，避免把工具版本、插件包和业务产品简报版本混在一起：

- `VERSION`：PMW 产品 / Codex plugin 的语义版本，根目录 `VERSION` 是真源，`plugins/pmworkspace/.codex-plugin/plugin.json` 的 `version` 必须保持一致。
- `REVISION`：当前插件包对应的打包源码提交，由 `bin/pmw-revision` 按进入插件包的 source path 计算。
- 展示身份：`VERSION@revision7`，例如 `0.1.15@abcdef1`，用于让用户和 Agent 快速判断当前本地 PMW 是哪个版本、对应哪次源码。
- 业务产品简报中的 `v1 / v2` 是用户项目资产版本，不是 PMW 工具版本。

本地版本信息统一使用：

```bash
bin/pmw-version
bin/pmw-version --json
bin/pmw-version --check
```

`pmw-version` 只读取本地版本身份；`--check` 会额外调用 `pmw-update-check --force` 和远端更新源对比。Agent 不应再通过猜测 Codex plugin cache 路径来判断 PMW 版本。

## Check

Use `pmw-update-check --quick` in every skill preamble. Quick mode is intentionally fast:

- It reuses a fresh cached result for `update_check_quick_ttl_seconds` seconds, default 300.
- It uses `PMW_UPDATE_CHECK_QUICK_TIMEOUT`, default 1.5 seconds, for each remote metadata request.
- It checks the remote `VERSION` and packaged `REVISION`; full branch checks remain available through `pmw-update-check --force` or `pmw-version --check`.
- It never blocks product work when offline, disabled, snoozed, or current.

Use `pmw-update-check --force` only when the user explicitly asks to verify against remote now. It checks GitHub when `update_check` is enabled:

- `VERSION` via the configured remote version URL.
- `main` branch commit via the configured repository URL.

This means PMWorkspace can detect both formal version bumps and same-version documentation / skill-rule updates.

Possible output:

```text
UPGRADE_AVAILABLE <local> <remote> <host>
UPGRADE_COMMAND pmw-upgrade --host <codex|codex-plugin>
JUST_UPGRADED <old> <new>
```

No output means current, disabled, snoozed, offline, or safely skipped.

## 用户提示

When `UPGRADE_AVAILABLE` appears:

```text
PMWorkspace 有新版本：<local> -> <remote>。建议先升级再继续，这样产品路由、状态资产和原型规则保持最新。
```

Offer:

- Upgrade now: run the exact `UPGRADE_COMMAND` emitted by `pmw-update-check`.
- Snooze: run `pmw-snooze-update <remote>`.
- Continue this time: proceed without changing config.

If `auto_upgrade: true`, upgrade automatically and report the result.

Do not upgrade silently when `auto_upgrade` is not true. Ask the user first, and only execute the emitted `UPGRADE_COMMAND` after the user confirms.

## Upgrade Cleanup

`pmw-upgrade` installs the latest PMWorkspace package into the selected host and deletes the old PMWorkspace-owned install directory before copying new files, so stale files removed in the new release cannot remain active locally.

- `--host codex`: removes the old `pm-*` skills and `pmworkspace-shared` under `CODEX_SKILLS_DIR` / `~/.codex/skills`, then installs the latest files.
- `--host codex-plugin`: removes the old local plugin package under `CODEX_PLUGINS_DIR/plugins/pmworkspace` / `~/.agents/plugins/plugins/pmworkspace`, then writes the latest plugin package and marketplace entry.
- Optional cache purge: set `PMW_PURGE_CODEX_PLUGIN_CACHE=true` to remove the PMWorkspace Codex plugin cache directory before reinstalling. Public Codex plugin users should normally update from the Codex Plugins UI, which manages its own cache.

`pmw-upgrade` never deletes `~/.pmworkspace` project state, product briefs, prototypes, handoff assets, Zoon links, or local audit history.

## Local GitHub Plugin Contract

The local GitHub plugin path is explicit-upgrade only:

- `pmw-update-check` can detect a newer `VERSION` or packaged `REVISION`, but it must only emit `UPGRADE_AVAILABLE` and `UPGRADE_COMMAND`.
- When the user explicitly confirms upgrade, run the emitted command, normally `pmw-upgrade --host codex-plugin`.
- `pmw-upgrade --host codex-plugin` must clone the configured `repo_url` / `PMW_REPO_URL` with `GIT_TERMINAL_PROMPT=0`, build the Codex plugin package from that clone, then install it into the local plugin package path.
- The default `repo_url` is `https://github.com/stephenfan80/PMWorkspace.git`.
- It must not silently pull code, overwrite the local plugin, or purge Codex plugin cache from a normal product workflow.

## Install Hosts

- `codex`: legacy skill install under `~/.codex/skills`.
- `codex-plugin`: local Codex plugin marketplace install via `codex plugin marketplace add/upgrade`, plus a `~/.agents/plugins` fallback package for agent-compatible local installs.

Public Codex plugin users should normally update from the Codex Plugins UI. The `codex-plugin` host is for GitHub/local beta installs and team testing.

## Remote Source

Default remote version URL:

```text
https://raw.githubusercontent.com/stephenfan80/PMWorkspace/main/VERSION
```

Default repository URL:

```text
https://github.com/stephenfan80/PMWorkspace.git
```

Users can override with:

```bash
PMW_REMOTE_VERSION_URL=<url>
PMW_REMOTE_REVISION_URL=<url>
```

or:

```bash
bin/pmw-config set remote_version_url <url>
bin/pmw-config set remote_revision_url <url>
```

For repository checks:

```bash
PMW_REPO_URL=<url>
```

or:

```bash
bin/pmw-config set repo_url <url>
```
