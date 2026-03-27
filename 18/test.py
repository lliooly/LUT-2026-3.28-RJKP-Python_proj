from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask18(unittest.TestCase):
    def test_perfect_number(self):
        result = run_task(18, "28\n")
        assert_success(self, result)
        self.assertIn("28是完数。", result.stdout)


if __name__ == "__main__":
    unittest.main()
