# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.2.x   | ✅ Yes    |
| 0.1.x   | ✅ Yes    |

## Reporting a Vulnerability

Please report vulnerabilities via [GitHub Security Advisories](https://github.com/jrodriguezgar/shortfx/security/advisories/new).

Do **not** open public issues for security vulnerabilities.

### What to include

- Description of the vulnerability
- Steps to reproduce
- Affected version(s)
- Potential impact

### Response timeline

- **Acknowledgement**: within 72 hours
- **Initial assessment**: within 1 week
- **Fix or mitigation**: best effort, typically within 2 weeks

## Security Design Principles

shortfx follows these security guidelines:

- **No `eval()`/`exec()`** — expression evaluation uses AST-based parsing
- **No external network calls** — core library is fully offline
- **No secrets or credentials** — pure computation library with no auth
- **Standard library only** — zero runtime dependencies in core
