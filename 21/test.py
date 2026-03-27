from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask21(unittest.TestCase):
    def test_word_statistics(self):
        task_dir = Path(__file__).resolve().parent
        target_file = task_dir / "zen1.txt"
        if target_file.exists():
            target_file.unlink()

        result = run_task(21)
        assert_success(self, result)

        self.assertIn("行数：4", result.stdout)
        self.assertIn("单词总数：20", result.stdout)
        self.assertTrue(target_file.exists())
        self.assertIn("better: 4", target_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
