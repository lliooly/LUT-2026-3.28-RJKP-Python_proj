from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask12(unittest.TestCase):
    def test_month_query_loop(self):
        result = run_task(12, "2\n0\n")
        assert_success(self, result)
        self.assertIn("2月有28天。", result.stdout)
        self.assertIn("程序结束。", result.stdout)


if __name__ == "__main__":
    unittest.main()
