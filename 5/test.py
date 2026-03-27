from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask5(unittest.TestCase):
    def test_usd_to_cny(self):
        result = run_task(5, "3.5$\n")
        assert_success(self, result)
        self.assertIn("3.5美元可以兑换人民币24.04元", result.stdout)


if __name__ == "__main__":
    unittest.main()
