import tempfile
import unittest
from pathlib import Path

from scripts.validate_index_consistency import INDEX_BLOB_BASE, validate


class IndexConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.index_dir = Path(self.tempdir.name)
        (self.index_dir / "assessments").mkdir()
        (self.index_dir / "assessments" / "alpha.md").write_text(
            """---
harness_id: alpha
project_name: Alpha
repository: https://github.com/example/alpha
status: included
---
# Alpha
""",
            encoding="utf-8",
        )
        (self.index_dir / "TLDR.md").write_text(
            '<a id="alpha"></a>[Alpha](https://github.com/example/alpha)\n',
            encoding="utf-8",
        )
        (self.index_dir / "RANKINGS.md").write_text(
            '<a id="alpha"></a>[Alpha](https://github.com/example/alpha)\n',
            encoding="utf-8",
        )
        self.valid_entry = (
            "- [Alpha](https://github.com/example/alpha) - Organizational summary. "
            f"[Assessment]({INDEX_BLOB_BASE}/assessments/alpha.md) · "
            f"[TL;DR]({INDEX_BLOB_BASE}/TLDR.md#alpha) · "
            f"[Ranking]({INDEX_BLOB_BASE}/RANKINGS.md#alpha)."
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def assert_error_contains(self, readme, fragment):
        errors, _ = validate(readme, self.index_dir)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_entry_passes(self):
        errors, entries = validate(self.valid_entry, self.index_dir)
        self.assertEqual([], errors)
        self.assertEqual(1, entries)

    def test_missing_assessment_fails(self):
        readme = self.valid_entry.replace("alpha.md", "missing.md")
        self.assert_error_contains(readme, "canonical assessment does not exist")

    def test_repository_mismatch_fails(self):
        readme = self.valid_entry.replace(
            "https://github.com/example/alpha",
            "https://github.com/example/not-alpha",
            1,
        )
        self.assert_error_contains(readme, "does not match Index repository")

    def test_wrong_anchor_link_fails(self):
        readme = self.valid_entry.replace("TLDR.md#alpha", "TLDR.md#wrong")
        self.assert_error_contains(readme, "missing canonical TL;DR link")

    def test_missing_canonical_anchor_fails(self):
        (self.index_dir / "RANKINGS.md").write_text("# Rankings\n", encoding="utf-8")
        self.assert_error_contains(self.valid_entry, "RANKINGS.md has no explicit anchor")

    def test_state_vector_duplication_fails(self):
        readme = self.valid_entry.replace(
            "Organizational summary.",
            "Organizational summary: `A C C — — P`.",
        )
        self.assert_error_contains(
            readme, "duplicates a canonical six-state VSM vector"
        )

    def test_per_system_state_assignment_fails(self):
        readme = self.valid_entry.replace(
            "Organizational summary.",
            "Organizational summary; S3: C.",
        )
        self.assert_error_contains(
            readme, "duplicates a canonical per-system VSM state assignment"
        )

    def test_numeric_ranking_duplication_fails(self):
        readme = self.valid_entry.replace(
            "Organizational summary.",
            "Organizational summary; rank 2.",
        )
        self.assert_error_contains(readme, "duplicates a canonical numeric ranking")


if __name__ == "__main__":
    unittest.main()
