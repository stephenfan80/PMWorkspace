# 更新工作流

Every PMWorkspace skill should check for updates before doing product work when platform scripts are available.

## Check

Use `pmw-update-check`. It checks GitHub on every run when `update_check` is enabled:

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

## Install Hosts

- `codex`: legacy skill install under `~/.codex/skills`.
- `codex-plugin`: local Codex plugin install under `~/.agents/plugins/plugins/pmworkspace`, with `~/.agents/plugins/marketplace.json` updated.

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
```

or:

```bash
bin/pmw-config set remote_version_url <url>
```

For repository checks:

```bash
PMW_REPO_URL=<url>
```

or:

```bash
bin/pmw-config set repo_url <url>
```
