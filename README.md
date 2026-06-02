# pdugan20-plugins

[![CI](https://github.com/pdugan20/pdugan20-plugins/workflows/CI/badge.svg)](https://github.com/pdugan20/pdugan20-plugins/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

A Claude Code plugin marketplace for [Pat Dugan](https://github.com/pdugan20)'s
personal plugins.

## Add the marketplace

```text
/plugin marketplace add pdugan20/pdugan20-plugins
```

## Plugins

| Plugin | Install | Description |
|--------|---------|-------------|
| [claudelint](https://github.com/pdugan20/claudelint) | `/plugin install claudelint@pdugan20-plugins` | Lints Claude Code projects: CLAUDE.md, skills, settings, hooks, MCP, plugins |
| [mintlify-docs](https://github.com/pdugan20/mintlify-docs) | `/plugin install mintlify-docs@pdugan20-plugins` | House-style toolkit for Mintlify docs sites |

Each plugin lives in its own repository; this repo only hosts the marketplace
catalog (`.claude-plugin/marketplace.json`).
