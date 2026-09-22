import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_metrics.py"
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("render_metrics", SCRIPT)
metrics = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(metrics)


class MetricsTests(unittest.TestCase):
    def test_generated_metrics_match_repository(self):
        repo = Path(__file__).resolve().parents[1]
        expected = {"schema_version": 1, **metrics.compute_core_metrics(repo)}
        actual = json.loads((repo / "data" / "metrics.json").read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)

    def test_duplicate_curated_identity_fails(self):
        link = "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/alpha.md)"
        with self.assertRaises(ValueError):
            metrics.parse_curated_ids(f"- A {link}\n- B {link}\n")

    def test_core_query_is_source_root_scoped_and_write_free(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "README.md").write_text(
                "- [A](https://example.com/a) - A. "
                "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/alpha.md)\n"
                "- [B](https://example.com/b) - B. "
                "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/beta.md)\n",
                encoding="utf-8",
            )
            result = metrics.compute_core_metrics(repo)
            self.assertEqual(result["curated_representative_entries"], 2)
            self.assertEqual(result["curated_entry_ids"], ["alpha", "beta"])
            self.assertFalse((repo / "data" / "metrics.json").exists())


if __name__ == "__main__":
    unittest.main()
