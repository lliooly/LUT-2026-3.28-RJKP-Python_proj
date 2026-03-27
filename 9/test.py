from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask9(unittest.TestCase):
    def test_divisible_by_3_not_5(self):
        result = run_task(9)
        assert_success(self, result)
        self.assertIn("3 6 9 12", result.stdout)
        self.assertIn("96 99", result.stdout)
        self.assertNotIn("15 ", result.stdout)


if __name__ == "__main__":
    unittest.main()
