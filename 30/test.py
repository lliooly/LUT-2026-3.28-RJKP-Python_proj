from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask30(unittest.TestCase):
    def test_crow_and_tree_count(self):
        result = run_task(30)
        assert_success(self, result)
        self.assertIn("树的数量：5", result.stdout)
        self.assertIn("鸦的数量：20", result.stdout)


if __name__ == "__main__":
    unittest.main()
