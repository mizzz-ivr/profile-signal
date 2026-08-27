# Contributing to Profile Signal

Thanks for considering a contribution.

## Development setup

```bash
python -m pip install PyYAML==6.0.2
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/build-profile-signal-release.py --version v0.0.0-test
```

## Compatibility rules

- Keep `privacy.public_only: true` as the safe default for v0.x.
- Do not change the meaning of an existing preset in a breaking way; add a new preset instead.
- Keep Release ZIP installs self-contained under `.profile-signal/` plus the generated config/workflow templates.
- Preserve existing README marker names unless a migration path is documented.
- Add tests for analytics, preset registry, release packaging, and rendering behavior affected by the change.

## Pull requests

Keep changes focused and include:

- the problem being solved;
- behavior changes;
- tests added or updated;
- documentation or migration notes when user-facing behavior changes.
