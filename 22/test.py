from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask22(unittest.TestCase):
    def test_merge_lines_and_write(self):
        task_dir = Path(__file__).resolve().parent
        target_file = task_dir / "yzy2.txt"
        if target_file.exists():
            target_file.unlink()

        result = run_task(22)
        assert_success(self, result)

        expected = "慈母手中线，游子身上衣。临行密密缝，意恐迟迟归。谁言寸草心，报得三春晖。"
        self.assertIn(expected, result.stdout)
        self.assertTrue(target_file.exists())
        self.assertEqual(target_file.read_text(encoding="utf-8"), expected)


if __name__ == "__main__":
    unittest.main()
