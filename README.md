# Plugins

[![CI](https://github.com/pdugan20/plugins/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/plugins/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/plugins?logo=github)](https://github.com/pdugan20/plugins/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

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
| [Patrick Skills](https://github.com/pdugan20/skills/tree/v2.1.0) | Design exploration, feature delivery, production hardening, and Mintlify documentation skills |
| [ClaudeLint](https://github.com/pdugan20/claudelint/tree/v0.7.1) | Claude Code project and plugin linting |

ClaudeLint is currently available only in the Claude Code marketplace.

## Migrating

Remove any old marketplace registrations named `pdugan20-plugins` or `patrick-tools`, then add `pdugan20/plugins` and reinstall plugins with the commands above. GitHub redirects the old repository URLs, but marketplace and plugin IDs do not redirect.

The renamed skill plugin is `patrick-skills@patrick-plugins`.

The retired `mintlify-docs@patrick-plugins` package has been consolidated into
Patrick Skills. Install `patrick-skills@patrick-plugins`, then remove the old
plugin. See the [skill migration guide](https://github.com/pdugan20/skills/blob/v2.1.0/docs/migrations/mintlify-docs.md) for the current skill names.

## Development

```bash
npm ci
npm run verify
```

Each source is pinned to a release tag. Marketplace releases use the matching section of [CHANGELOG.md](CHANGELOG.md) as their GitHub Release notes; see the [release guide](RELEASING.md) for sequencing and installation checks.
