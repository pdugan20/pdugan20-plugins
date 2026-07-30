#!/usr/bin/env python3
"""Tests for marketplace validation."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        for relative_path in (
            ".claude-plugin/marketplace.json",
            ".agents/plugins/marketplace.json",
            "package.json",
            "package-lock.json",
            "README.md",
        ):
            source = validate_repository.ROOT / relative_path
            destination = self.root / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def read_json(self, relative_path: str) -> dict:
        return json.loads((self.root / relative_path).read_text(encoding="utf-8"))

    def write_json(self, relative_path: str, value: dict) -> None:
        (self.root / relative_path).write_text(
            json.dumps(value, indent=2) + "\n", encoding="utf-8"
        )

    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository.validate(root=self.root), [])

    def test_release_tag_matches_version(self) -> None:
        package = self.read_json("package.json")
        self.assertEqual(
            validate_repository.validate(f"v{package['version']}", root=self.root), []
        )

    def test_release_tag_mismatch_is_rejected(self) -> None:
        errors = validate_repository.validate("v9.9.9", root=self.root)
        self.assertTrue(any("must match the marketplace version" in error for error in errors))

    def test_package_and_marketplace_versions_must_match(self) -> None:
        manifest = self.read_json(".claude-plugin/marketplace.json")
        manifest["version"] = "1.2.3"
        self.write_json(".claude-plugin/marketplace.json", manifest)

        errors = validate_repository.validate(root=self.root)

        self.assertIn(
            "package version must match the Claude marketplace version", errors
        )

    def test_package_lock_versions_must_match(self) -> None:
        package_lock = self.read_json("package-lock.json")
        package_lock["version"] = "9.9.9"
        self.write_json("package-lock.json", package_lock)

        errors = validate_repository.validate(root=self.root)

        self.assertIn("package-lock versions must match the package version", errors)

    def test_expected_catalog_membership_is_explicit(self) -> None:
        self.assertEqual(
            validate_repository.EXPECTED_CLAUDE,
            {"claudelint", "mintlify-docs", "patrick-workflows"},
        )
        self.assertEqual(
            validate_repository.EXPECTED_CODEX,
            {"mintlify-docs", "patrick-workflows"},
        )


if __name__ == "__main__":
    unittest.main()
