# Security Policy

Profile Signal is designed for public GitHub profile data.

## Supported scope

The v0.x runtime requires:

```yaml
privacy:
  public_only: true
```

Private repository data is intentionally out of scope. The default release package does not require a PAT or API key.

## Reporting a vulnerability

Please avoid opening a public issue for vulnerabilities that could expose credentials, private repository metadata, or other sensitive information.

Use GitHub's private security reporting feature for this repository when available.

When reporting, include the affected Profile Signal version, expected behavior, actual behavior, and the minimum reproduction steps needed to validate the issue.
