# Standalone repository migration

Profile Signal was originally developed inside `mizzz-ivr/mizzz-ivr`, the maintainer's GitHub Profile Repository.

Starting with v0.3.0, this repository is the Source of Truth for:

- runtime source;
- tests and CI;
- release packaging;
- release notes;
- GitHub Wiki source;
- preset registry;
- installation templates.

`mizzz-ivr/mizzz-ivr` remains a consumer/showcase repository and keeps only the installed `.profile-signal/` runtime, profile configuration, update workflows, generated assets/data, and profile-specific content.

Historical v0.1.0/v0.2.0 releases belonged to the profile repository. New releases start from this standalone repository.
