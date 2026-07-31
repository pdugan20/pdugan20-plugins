# Releasing

The marketplace pins every plugin source to a published tag. Never merge a
marketplace ref before that upstream tag exists and passes its installation
checks.

## Prepare the release

1. Confirm each changed source release exists. For Patrick Skills, run:

   ```bash
   npx --yes skills@1.5.21 add "pdugan20/skills@v$SKILLS_VERSION" --list
   ```

2. Update the Claude and Codex marketplace entries together. Keep source refs,
   advertised plugin versions, descriptions, and runtime membership in parity.
3. Bump `package.json`, `package-lock.json`, and the Claude marketplace version.
   Removing a cataloged plugin is a breaking marketplace release.
4. Move the completed changelog entries into a dated version section.
5. Run:

   ```bash
   npm ci
   npm run verify
   python3 scripts/validate_repository.py --release-tag "v$VERSION"
   python3 scripts/release_notes.py "$VERSION"
   actionlint
   zizmor --pedantic --min-severity medium --min-confidence medium --no-online-audits .
   ```

6. Open a pull request. Require `Lint`, `Marketplace install smoke test`, and
   `Audit workflow security` before merging.

## Publish and verify

After the release commit is merged:

```bash
git switch main
git pull --ff-only
git tag -a "v$VERSION" -m "v$VERSION"
git push origin "v$VERSION"
gh run watch --repo pdugan20/plugins \
  "$(gh run list --repo pdugan20/plugins --workflow Release --limit 1 --json databaseId --jq '.[0].databaseId')" \
  --exit-status
```

Confirm the GitHub Release notes match the changelog. Refresh the published
marketplace in clean Claude Code and Codex profiles, install each remaining
entry, and verify that no removed entry is advertised. Only then update
`agent-tooling` or deprecate an old source repository.

If a source tag is missing or an installation test fails, keep the marketplace
release unpublished. Fix the source first rather than weakening the pin.
