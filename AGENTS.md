# Repository Instructions

- Keep the Claude Code and Codex marketplace identifiers set to `patrick-plugins`.
- Pin every remote plugin source to a release tag and keep each entry's version synchronized with that tag.
- Keep shared plugin entries synchronized between the two marketplace manifests.
- Update the migration instructions when a marketplace or plugin identifier changes.
- Run `npm run verify` before publishing catalog changes.

## Code Review Rules

- Flag remote plugin sources that are not pinned to a release tag or whose declared
  version does not match that tag.
- Flag Claude/Codex marketplace entries that disagree on shared plugin identity, source,
  or version, including any identifier drift from `patrick-plugins`.
- Flag catalog changes that omit migration instructions for renamed identifiers or that
  introduce a publish/release mutation into ordinary verification.

Do not publish tags or mutate plugin releases without explicit authorization.
