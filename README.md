# plugins

[![CI](https://github.com/pdugan20/plugins/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/pdugan20/plugins/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/plugins)](https://github.com/pdugan20/plugins/releases/latest)
[![License](https://img.shields.io/github/license/pdugan20/plugins)](LICENSE)

Versioned plugins for Claude Code and Codex.

## Claude Code

```text
/plugin marketplace add pdugan20/plugins
/plugin install patrick-skills@patrick-plugins
```

## Codex

```text
codex plugin marketplace add pdugan20/plugins
codex plugin add patrick-skills@patrick-plugins
```

## Plugins

| Plugin | What it provides |
| --- | --- |
| [Patrick Skills](https://github.com/pdugan20/skills/tree/v3.0.0) | Repository setup, design exploration, design-system alignment and auditing, UI video analysis, feature validation and delivery, and Mintlify documentation |
| [ClaudeLint](https://github.com/pdugan20/claudelint/tree/v0.7.1) | Claude Code project and plugin linting |

ClaudeLint is currently available only in the Claude Code marketplace.

## Migrating

Remove any old marketplace registrations named `pdugan20-plugins` or `patrick-tools`, then add `pdugan20/plugins` and reinstall plugins with the commands above. GitHub redirects the old repository URLs, but marketplace and plugin IDs do not redirect.

The renamed skill plugin is `patrick-skills@patrick-plugins`.

## Development

```bash
npm ci
npm run verify
```

Each source is pinned to a release tag. Marketplace releases use the matching section of [CHANGELOG.md](CHANGELOG.md) as their GitHub Release notes; see the [release guide](RELEASING.md) for sequencing and installation checks.
