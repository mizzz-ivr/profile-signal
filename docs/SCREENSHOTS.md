# Screenshot guide

This guide defines the recommended screenshots for the Profile Signal OSS article and documentation.

## 1. Standalone repository

Open the repository root:

https://github.com/mizzz-ivr/profile-signal

Capture the area that shows:

- repository name `mizzz-ivr/profile-signal`
- root tree including `.github/`, `.profile-signal/`, `distribution/`, `docs/`, `release-notes/`, `scripts/`, and `tests/`
- the repository description / About area when it fits naturally

Avoid including the full browser chrome if it makes the code tree too small.

## 2. Release package CI

Open the successful workflow run that published `v0.4.0` and capture the workflow summary/jobs area.

The screenshot should make these points readable:

- workflow name / release run
- successful conclusion
- package validation / smoke test
- release publish job

Do not include logs containing tokens, authorization headers, or unrelated account information.

## 3. v0.4.0 Release

Open:

https://github.com/mizzz-ivr/profile-signal/releases/tag/v0.4.0

Capture one frame containing:

- `Profile Signal v0.4.0`
- Latest badge when visible
- the short release summary
- `profile-signal-v0.4.0.zip` in Assets

Prefer a single screenshot over stitching multiple release-page images.

## 4. Generated sample profile

Open:

https://github.com/mizzz-ivr/profile-signal/tree/main/examples/sample-profile

Capture the rendered README, not the raw Markdown source.

A good frame includes:

- `Profile Signal — Sample Profile`
- the static sample-data notice
- `LIVE SIGNAL`
- `TODAY`
- `CURRENT FOCUS`
- the top of `DEV PULSE`

A second screenshot is unnecessary unless the article specifically discusses lower widgets. Link to the sample page for the full output.

## Profile overview policy

Do not use a full screenshot of `github.com/mizzz-ivr`; the page is too tall to remain readable in an article. Link readers directly to the live profile instead.
