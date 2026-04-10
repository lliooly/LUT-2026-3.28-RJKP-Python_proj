from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask26(unittest.TestCase):
    def test_sort_and_extract_colors(self):
        result = run_task(26)
        assert_success(self, result)
        self.assertIn("按照标签排序后的列表：", result.stdout)
        self.assertIn("[('green', 'color'), ('red', 'color'), ('yellow', 'color')", result.stdout)
        self.assertIn("颜色列表 lst_colors：", result.stdout)
        self.assertIn("['red', 'yellow', 'green']", result.stdout)


if __name__ == "__main__":
    unittest.main()
