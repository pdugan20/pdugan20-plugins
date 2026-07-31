# Changelog

All notable changes to this marketplace are documented in this file.

## [Unreleased]

## [3.1.0] - 2026-07-30

### Changed

- Updated Patrick Skills to 2.2.0 for Claude Code and Codex.
- Expanded `feature-delivery` with evidence-first specification, cross-repository coordination, explicit execution modes, and staged rollout guidance.
- Updated Patrick Skills and migration-guide links to their exact 2.2.0 release paths.

## [3.0.0] - 2026-07-30

### Changed

- Updated Patrick Skills to 2.1.0 for Claude Code and Codex, adding the four hardened Mintlify documentation skills to the combined collection.
- Removed the standalone `mintlify-docs` entry from both marketplaces now that its skills are distributed by `patrick-skills`.
- Removed the unused Mintlify cross-marketplace dependency allowlist entry.
- Updated the marketplace installation smoke test to exercise only the packages that remain cataloged.
- Added a release runbook that prevents unpublished source pins and requires both runtime installation checks.

### Migration

- Install `patrick-skills@patrick-plugins`, then remove `mintlify-docs@patrick-plugins`.
- Use `scaffold-mintlify-site`, `review-mintlify-docs`, `generate-mintlify-reference`, and `write-mintlify-changelog`; the old `review-docs`, `document-reference`, and `changelog-writer` names remain only in historical releases.

## [2.0.0] - 2026-07-30

### Changed

- Renamed the repository from `patrick-tools` to `plugins` and the marketplace identifier from `patrick-tools` to `patrick-plugins`.
- Renamed the `patrick-workflows` plugin to `patrick-skills` and pinned it to the canonical `pdugan20/skills` v2.0.0 release.
- Updated Mintlify Docs to 0.3.3 so its install guidance and release helper use the renamed marketplace.
- Updated ClaudeLint to 0.7.1 so its guided installer and documentation use the renamed marketplace.
- Reorganized the README around the shortest Claude Code and Codex installation paths.
- Added migration guidance for both retired marketplace identifiers and the retired skill plugin name.

## [1.0.1] - 2026-07-30

### Changed

- Updated Patrick Workflows to 1.1.0 for Claude Code and Codex.
- Replaced ClaudeLint's repository-validation role with Claude Code's official strict plugin validator; ClaudeLint remains available as a marketplace product.
- Made marketplace release validation derive its version from package metadata instead of hardcoding a release number.
- Added standard release and Node.js badges, a client-oriented installation guide, and direct links to every cataloged skill source.
- Replaced generated commit summaries with curated GitHub Release notes extracted from this matching changelog section.

## [1.0.0] - 2026-07-30

### Changed

- Renamed the repository and marketplace from `pdugan20-plugins` to `patrick-tools`.
- Pinned every plugin source to a matching release tag.
- Updated ClaudeLint to 0.7.0.

### Added

- Added Patrick Workflows 1.0.0 for Claude Code and Codex.
- Added Mintlify Docs 0.3.2 with direct Skills CLI installation and hardened release checks.
- Added cross-runtime catalog validation, install smoke tests, spelling checks, workflow-security analysis, and scheduled link validation.

[unreleased]: https://github.com/pdugan20/plugins/compare/v3.1.0...HEAD
[3.1.0]: https://github.com/pdugan20/plugins/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/pdugan20/plugins/compare/v2.0.0...v3.0.0
[2.0.0]: https://github.com/pdugan20/plugins/compare/v1.0.1...v2.0.0
[1.0.1]: https://github.com/pdugan20/plugins/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/pdugan20/plugins/releases/tag/v1.0.0
