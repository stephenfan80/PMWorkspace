# Update Workflow

Every PMWorkspace skill should check for updates before doing product work when platform scripts are available.

## Check

Use `pmw-update-check`.

Possible output:

```text
UPGRADE_AVAILABLE <local> <remote>
JUST_UPGRADED <old> <new>
```

No output means current, disabled, snoozed, offline, or safely skipped.

## User Prompt

When `UPGRADE_AVAILABLE` appears:

```text
PMWorkspace 有新版本：<local> -> <remote>。建议先升级再继续，这样产品路由、状态资产和原型规则保持最新。
```

Offer:

- Upgrade now: run `pmw-upgrade --host codex`.
- Snooze: run `pmw-snooze-update <remote>`.
- Continue this time: proceed without changing config.

If `auto_upgrade: true`, upgrade automatically and report the result.

## Remote Source

Default remote version URL:

```text
https://raw.githubusercontent.com/stephenfan80/PMWorkspace/main/VERSION
```

Users can override with:

```bash
PMW_REMOTE_VERSION_URL=<url>
```

or:

```bash
bin/pmw-config set remote_version_url <url>
```
