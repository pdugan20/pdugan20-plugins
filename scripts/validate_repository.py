#!/usr/bin/env python3
"""Validate marketplace identity, source pins, and cross-runtime parity."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
EXPECTED_CLAUDE = {"claudelint", "mintlify-docs", "patrick-skills"}
EXPECTED_CODEX = {"mintlify-docs", "patrick-skills"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def entries(manifest: dict) -> dict[str, dict]:
    return {entry["name"]: entry for entry in manifest.get("plugins", [])}


def validate(release_tag: str | None = None, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    package = load(root / "package.json")
    package_lock = load(root / "package-lock.json")
    claude_manifest = load(root / ".claude-plugin" / "marketplace.json")
    codex_manifest = load(root / ".agents" / "plugins" / "marketplace.json")
    claude = entries(claude_manifest)
    codex = entries(codex_manifest)

    marketplace_version = claude_manifest.get("version")
    package_version = package.get("version")
    lock_version = package_lock.get("version")
    lock_package_version = package_lock.get("packages", {}).get("", {}).get("version")

    if package.get("name") != "patrick-plugins":
        errors.append("package name must be patrick-plugins")
    if package_lock.get("name") != package.get("name"):
        errors.append("package-lock name must match the package name")
    if package_lock.get("packages", {}).get("", {}).get("name") != package.get("name"):
        errors.append("package-lock root package name must match the package name")
    if claude_manifest.get("name") != "patrick-plugins":
        errors.append("Claude marketplace name must be patrick-plugins")
    if codex_manifest.get("name") != "patrick-plugins":
        errors.append("Codex marketplace name must be patrick-plugins")
    if not isinstance(marketplace_version, str) or not VERSION_RE.fullmatch(
        marketplace_version
    ):
        errors.append("Claude marketplace version must be a stable semantic version")
    if package_version != marketplace_version:
        errors.append("package version must match the Claude marketplace version")
    if lock_version != package_version or lock_package_version != package_version:
        errors.append("package-lock versions must match the package version")
    if release_tag is not None and release_tag != f"v{marketplace_version}":
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
        if name not in claude:
            errors.append(f"Codex plugin {name} must have a matching Claude entry")
            continue
        expected_ref = f"v{claude[name]['version']}"
        if source.get("ref") != expected_ref:
            errors.append(f"Codex plugin {name} source ref must equal {expected_ref}")
        if entry.get("policy", {}).get("installation") != "AVAILABLE":
            errors.append(f"Codex plugin {name} must be available")
        if entry.get("policy", {}).get("authentication") not in {"ON_INSTALL", "ON_USE"}:
            errors.append(f"Codex plugin {name} must declare authentication timing")

    readme = (root / "README.md").read_text(encoding="utf-8")
    if "pdugan20/plugins" not in readme:
        errors.append("README must document the canonical marketplace repository")
    if "patrick-skills@patrick-plugins" not in readme:
        errors.append("README must document the canonical skill plugin install")
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
