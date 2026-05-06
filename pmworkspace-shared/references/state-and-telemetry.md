# State And Telemetry

PMWorkspace stores durable product assets locally by default. It should help the user accumulate product judgment and reusable handoff material without leaking sensitive source material.

## Local State Root

Default root:

```text
~/.pmworkspace/
```

Expected structure:

```text
config.yaml
analytics/usage.jsonl
projects/<slug>/briefs/
projects/<slug>/decisions.jsonl
projects/<slug>/prototypes/
projects/<slug>/taste-profile.jsonl
```

## What To Save

- Usage event: skill name, timestamp, project slug.
- Decisions: concise product or design decisions the user approved.
- Briefs: aligned or ready-for-confirmation markdown briefs.
- Prototype manifests: scheme, screen, canvas, brief dependency, prompt summary.
- Taste feedback: approved/rejected direction and the user's reason.

## What Not To Save

- Real tokens, owner secrets, API keys, cookies, auth headers.
- Private customer data, raw call transcripts, internal recordings.
- Sensitive screenshots or unredacted Zoon content.
- Full private PRDs unless the user explicitly asks to store them locally.

## Telemetry Defaults

- `telemetry: local` means write local logs only.
- Remote telemetry requires explicit opt-in.
- Anonymous remote telemetry, when implemented, may include skill name, duration, outcome, version, and coarse OS only.
- Never send project names, file paths, prompt text, screenshots, brief content, or customer data.

Use `bin/pmw-config list` to inspect active settings.
