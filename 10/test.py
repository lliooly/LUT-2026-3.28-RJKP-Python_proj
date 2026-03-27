from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask10(unittest.TestCase):
    def test_series_sum(self):
        result = run_task(10)
        assert_success(self, result)
        self.assertIn("1×2×3+3×4×5+...+49×50×51的值为：844350", result.stdout)


if __name__ == "__main__":
    unittest.main()
