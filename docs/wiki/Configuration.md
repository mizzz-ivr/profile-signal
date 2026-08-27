# Configuration

[English](Configuration) | [日本語](Configuration-ja)

Main file: `.github/profile-signal.yml`

```yaml
version: 1
profile:
  username: YOUR_GITHUB_USERNAME
  timezone: Asia/Tokyo
privacy:
  public_only: true
preset: standard
theme: signal
widgets: {}
readme:
  path: README.md
  auto_insert_markers: true
  insert_before: ""
  empty_disabled: true
```

`privacy.public_only: true` is required in v0. Explicit widget settings override the selected preset.
