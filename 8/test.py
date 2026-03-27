from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask8(unittest.TestCase):
    def test_grade_conversion(self):
        result = run_task(8, "85\n")
        assert_success(self, result)
        self.assertIn("对应的等级为：良", result.stdout)


if __name__ == "__main__":
    unittest.main()
