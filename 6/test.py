from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask6(unittest.TestCase):
    def test_leap_year(self):
        result = run_task(6, "2024\n")
        assert_success(self, result)
        self.assertIn("2024年是闰年。", result.stdout)


if __name__ == "__main__":
    unittest.main()
