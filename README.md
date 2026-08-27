# Profile Signal

Modular, config-driven GitHub Profile README widgets generated from public GitHub activity.

[日本語](./README.ja.md) · [Wiki](https://github.com/mizzz-ivr/profile-signal/wiki) · [Releases](https://github.com/mizzz-ivr/profile-signal/releases)

Profile Signal turns a GitHub Profile README into a lightweight development dashboard while keeping the runtime inside your own profile repository.

## Widgets

`LIVE SIGNAL` · `TODAY` · `CURRENT FOCUS` · `DEV PULSE` · `NOW BUILDING` · `ACTIVITY STREAM` · `DEV RECAP`

## Quick start

1. Download `profile-signal-vX.Y.Z.zip` from [Releases](https://github.com/mizzz-ivr/profile-signal/releases).
2. Extract it into `<username>/<username>`.
3. Edit `.github/profile-signal.yml` and set your GitHub username.
4. Commit and push.
5. Run **Actions → Profile Signal → Run workflow** once.

The installed workflow executes the local runtime:

```yaml
- uses: ./.profile-signal
  with:
    config: .github/profile-signal.yml
```

The default distribution is public-only and requires no PAT or API key.

## Presets

`minimal` · `standard` · `full` · `terminal` · `compact` · `developer` · `activity` · `oss`

Presets live in `.profile-signal/presets/*.yml`; explicit widget overrides take precedence.

## Development

```bash
python -m pip install PyYAML==6.0.2
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/build-profile-signal-release.py --version v0.0.0-test
```

The live profile at [github.com/mizzz-ivr](https://github.com/mizzz-ivr) is the primary dogfooding/showcase environment.

## License

MIT. See [LICENSE](./LICENSE).
