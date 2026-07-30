# Patrick's Tools

[![CI](https://github.com/pdugan20/patrick-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/pdugan20/patrick-tools/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pdugan20/patrick-tools?logo=github)](https://github.com/pdugan20/patrick-tools/releases/latest)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D22.22.2-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

A versioned plugin marketplace for [Pat Dugan](https://github.com/pdugan20)'s Claude Code and Codex tools. Each catalog entry is pinned to an independently released plugin version.

## Catalog

| Plugin | Version | Clients | Included capabilities |
| --- | --- | --- | --- |
| [ClaudeLint](https://github.com/pdugan20/claudelint/tree/v0.7.0) | 0.7.0 | Claude Code | Claude project, skill, settings, hook, MCP, and plugin linting |
| [Mintlify Docs](https://github.com/pdugan20/mintlify-docs/tree/v0.3.2) | 0.3.2 | Claude Code, Codex, Skills CLI | [Scaffold](https://github.com/pdugan20/mintlify-docs/tree/v0.3.2/skills/scaffold-mintlify-site), [review](https://github.com/pdugan20/mintlify-docs/tree/v0.3.2/skills/review-docs), [changelog](https://github.com/pdugan20/mintlify-docs/tree/v0.3.2/skills/changelog-writer), and [reference](https://github.com/pdugan20/mintlify-docs/tree/v0.3.2/skills/document-reference) workflows |
| [Patrick Workflows](https://github.com/pdugan20/patrick-workflows/tree/v1.1.0) | 1.1.0 | Claude Code, Codex, Cursor, Skills CLI | [UI ideation](https://github.com/pdugan20/patrick-workflows/tree/v1.1.0/skills/code-native-ui-ideation), [feature delivery](https://github.com/pdugan20/patrick-workflows/tree/v1.1.0/skills/feature-delivery), and [production hardening](https://github.com/pdugan20/patrick-workflows/tree/v1.1.0/skills/production-hardening) |

The linked plugin tags and skill directories are the canonical source for instructions and release notes.

## Install

Use the marketplace when you want Claude Code or Codex to manage complete plugins. Use the Skills CLI when you want individual portable skills, a Cursor install, or a release pin independent of the marketplace.

### Claude Code marketplace

Register the marketplace once, then install any listed plugin:

```text
/plugin marketplace add pdugan20/patrick-tools
/plugin install patrick-workflows@patrick-tools
```

Replace `patrick-workflows` with `mintlify-docs` or `claudelint` as needed.

### Codex marketplace

```text
codex plugin marketplace add pdugan20/patrick-tools
codex plugin add patrick-workflows@patrick-tools
```

Replace `patrick-workflows` with `mintlify-docs` as needed. ClaudeLint is currently packaged only for Claude Code.

### Direct Skills CLI

The Skills CLI supports Claude Code, Codex, Cursor, and other compatible clients:

```bash
npx skills add pdugan20/patrick-workflows
npx skills add pdugan20/mintlify-docs
```

Each collection README documents individual-skill selection, client targeting, global versus project scope, and reproducible tagged installs.

## Versioning

The marketplace has its own semantic version. Every plugin retains an independent release stream, and both marketplace manifests pin the same plugin tag. Updating a plugin therefore requires a marketplace patch release but does not change the other plugins.

GitHub Release notes come from the matching section of this repository's [changelog](CHANGELOG.md). Skill behavior changes remain documented by each canonical plugin repository rather than being duplicated here.

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

Verification checks package and manifest versions, exact tagged source pins, Claude/Codex catalog parity, Claude's official strict marketplace validation, tests, Markdown, and formatting. CI also runs real marketplace installation smoke tests for both clients.
