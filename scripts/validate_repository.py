#!/usr/bin/env python3
"""Validate marketplace identity, source pins, and cross-runtime parity."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
EXPECTED_CLAUDE = {"claudelint", "mintlify-docs", "patrick-workflows"}
EXPECTED_CODEX = {"mintlify-docs", "patrick-workflows"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def entries(manifest: dict) -> dict[str, dict]:
    return {entry["name"]: entry for entry in manifest.get("plugins", [])}


def validate(release_tag: str | None = None) -> list[str]:
    errors: list[str] = []
    claude_manifest = load(ROOT / ".claude-plugin" / "marketplace.json")
    codex_manifest = load(ROOT / ".agents" / "plugins" / "marketplace.json")
    claude = entries(claude_manifest)
    codex = entries(codex_manifest)

    if claude_manifest.get("name") != "patrick-tools":
        errors.append("Claude marketplace name must be patrick-tools")
    if codex_manifest.get("name") != "patrick-tools":
        errors.append("Codex marketplace name must be patrick-tools")
    if claude_manifest.get("version") != "1.0.0":
        errors.append("Claude marketplace version must be 1.0.0")
    if release_tag is not None and release_tag != f"v{claude_manifest.get('version')}":
        errors.append(f"release tag {release_tag!r} must match the marketplace version")
    if set(claude) != EXPECTED_CLAUDE:
        errors.append(f"Claude plugins must be {sorted(EXPECTED_CLAUDE)}")
    if set(codex) != EXPECTED_CODEX:
        errors.append(f"Codex plugins must be {sorted(EXPECTED_CODEX)}")

    for name, entry in claude.items():
        version = entry.get("version")
        ref = entry.get("source", {}).get("ref")
        if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
            errors.append(f"Claude plugin {name} has an invalid version")
        if ref != f"v{version}":
            errors.append(f"Claude plugin {name} source ref must equal v{version}")

    for name, entry in codex.items():
        source = entry.get("source", {})
        expected_ref = f"v{claude[name]['version']}"
        if source.get("ref") != expected_ref:
            errors.append(f"Codex plugin {name} source ref must equal {expected_ref}")
        if entry.get("policy", {}).get("installation") != "AVAILABLE":
            errors.append(f"Codex plugin {name} must be available")
        if entry.get("policy", {}).get("authentication") not in {"ON_INSTALL", "ON_USE"}:
            errors.append(f"Codex plugin {name} must declare authentication timing")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "pdugan20/pdugan20-plugins" in readme:
        errors.append("README contains the retired repository path")
    if "pdugan20/patrick-tools" not in readme:
        errors.append("README must document the renamed marketplace")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-tag")
    args = parser.parse_args()
    errors = validate(args.release_tag)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Marketplace validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
