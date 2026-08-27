# Installation

[English](Installation) | [日本語](Installation-ja)

1. Download `profile-signal-vX.Y.Z.zip` from [Releases](https://github.com/mizzz-ivr/profile-signal/releases).
2. Extract it into `<username>/<username>`.
3. Set `profile.username` in `.github/profile-signal.yml`.
4. Commit and push.
5. Run **Actions → Profile Signal → Run workflow** once.

Installed files include `.profile-signal/`, the config, two workflows, install notes, and a version marker. The archive does not overwrite your README.

## Refresh cadence

Profile Signal installs two workflows with different responsibilities:

- `.github/workflows/profile-signal.yml` — full refresh every 3 hours for TODAY/Search API metrics, DEV PULSE, repository health/CI, history, DEV RECAP, and all enabled widgets.
- `.github/workflows/profile-signal-stream.yml` — lightweight refresh every 30 minutes for `LIVE SIGNAL`, `CURRENT FOCUS`, and `ACTIVITY STREAM`.

The lightweight workflow preserves the heavier analytics state and commits only when the live-facing state changes. GitHub Public Events can be delayed upstream, so ACTIVITY STREAM is latest-public-signal data rather than a real-time guarantee.

To upgrade, replace `.profile-signal/` with the runtime from the new release, review both workflow template diffs, and inspect the generated profile diff before committing.

To uninstall, remove both Profile Signal workflows together with `.profile-signal/` and `.github/profile-signal.yml` so the 30-minute stream job cannot keep invoking a removed runtime.
