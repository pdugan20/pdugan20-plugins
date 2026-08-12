# Plugin catalog threat model

Protected assets are plugin identity, marketplace manifests, installer trust, pinned source
integrity, release tags, and user workspaces that consume the catalog. Remote repositories,
plugin metadata, migration text, and dependency updates are untrusted.

Required controls:

- Pin remote plugin sources to reviewed release tags and keep declared versions aligned.
- Keep Claude and Codex manifests synchronized for shared identity, source, version, and
  migration behavior.
- Treat plugin instructions and bundled executables as code: review permission boundaries,
  network behavior, credential use, and destructive actions before catalog admission.
- Keep verification read-only and require explicit authorization for tags, releases, or
  marketplace publication.
- Reject identifier changes without a documented migration that preserves existing installs.

Update this model when catalog identity, source formats, installation behavior, trust
policy, publishing, or a plugin's capabilities change.
