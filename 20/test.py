from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask20(unittest.TestCase):
    def test_recursive_series(self):
        result = run_task(20, "3\n")
        assert_success(self, result)
        self.assertIn("m(3) = 1.161905", result.stdout)


if __name__ == "__main__":
    unittest.main()
