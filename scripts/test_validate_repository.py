#!/usr/bin/env python3
"""Tests for marketplace validation."""

from __future__ import annotations

import unittest

import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository.validate(), [])

    def test_release_tag_matches_version(self) -> None:
        self.assertEqual(validate_repository.validate("v1.0.0"), [])

    def test_release_tag_mismatch_is_rejected(self) -> None:
        errors = validate_repository.validate("v9.9.9")
        self.assertTrue(any("must match the marketplace version" in error for error in errors))

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
