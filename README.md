# pdugan20-plugins

[![CI](https://github.com/pdugan20/pdugan20-plugins/workflows/CI/badge.svg)](https://github.com/pdugan20/pdugan20-plugins/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

A plugin marketplace for [Pat Dugan](https://github.com/pdugan20)'s Claude and
Codex workflows.

## Add the marketplace to Claude

```text
/plugin marketplace add pdugan20/pdugan20-plugins
```

## Add the marketplace to Codex

```text
codex plugin marketplace add pdugan20/pdugan20-plugins
```

## Plugins

| Plugin | Claude | Codex | Description |
| ------ | ------ | ----- | ----------- |
| [claudelint](https://github.com/pdugan20/claudelint) | `/plugin install claudelint@pdugan20-plugins` | — | Lints Claude Code projects: CLAUDE.md, skills, settings, hooks, MCP, plugins |
| [mintlify-docs](https://github.com/pdugan20/mintlify-docs) | `/plugin install mintlify-docs@pdugan20-plugins` | `codex plugin add mintlify-docs@pdugan20-plugins` | House-style toolkit for Mintlify docs sites |

Each plugin lives in its own repository. This repository only hosts the Claude
and Codex marketplace catalogs.
