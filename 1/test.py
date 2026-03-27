from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask1(unittest.TestCase):
    def test_sum_and_average(self):
        result = run_task(1, "90\n80\n70\n")
        assert_success(self, result)
        self.assertIn("总分为：240.0", result.stdout)
        self.assertIn("平均分为：80.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
