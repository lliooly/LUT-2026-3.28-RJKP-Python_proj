from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask7(unittest.TestCase):
    def test_triangle_perimeter_and_area(self):
        result = run_task(7, "3\n4\n5\n")
        assert_success(self, result)
        self.assertIn("三角形的周长为：12.0", result.stdout)
        self.assertIn("三角形的面积为：6.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
