# Patrick's Tools

[![CI](https://github.com/pdugan20/patrick-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/patrick-tools/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

A versioned plugin marketplace for [Pat Dugan](https://github.com/pdugan20)'s Claude Code and Codex tools.

## Add the marketplace

Claude Code:

```text
/plugin marketplace add pdugan20/patrick-tools
```

Codex:

```text
codex plugin marketplace add pdugan20/patrick-tools
```

## Plugins

| Plugin | Version | Claude Code | Codex | Direct skill install |
| --- | --- | --- | --- | --- |
| [claudelint](https://github.com/pdugan20/claudelint) | 0.7.0 | `/plugin install claudelint@patrick-tools` | Not packaged | Not applicable |
| [mintlify-docs](https://github.com/pdugan20/mintlify-docs) | 0.3.2 | `/plugin install mintlify-docs@patrick-tools` | `codex plugin add mintlify-docs@patrick-tools` | `npx skills add pdugan20/mintlify-docs` |
| [patrick-workflows](https://github.com/pdugan20/patrick-workflows) | 1.0.0 | `/plugin install patrick-workflows@patrick-tools` | `codex plugin add patrick-workflows@patrick-tools` | `npx skills add pdugan20/patrick-workflows` |

Every catalog source is pinned to a release tag. Individual plugin repositories remain the canonical source for their skills and release notes.

## Migrating from `pdugan20-plugins`

GitHub redirects the old repository URL, but the marketplace identifier changed to `patrick-tools`. Remove the old registration, add the renamed marketplace, and reinstall plugins using the commands above.

Claude Code:

```text
/plugin marketplace remove pdugan20-plugins
/plugin marketplace add pdugan20/patrick-tools
```

Codex:

```text
codex plugin marketplace remove pdugan20-plugins
codex plugin marketplace add pdugan20/patrick-tools
```

## Development

```bash
npm ci
npm run verify
```

The Claude Code and Codex catalogs are validated together so shared plugins cannot silently drift.
