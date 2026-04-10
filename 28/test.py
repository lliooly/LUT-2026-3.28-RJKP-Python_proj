from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask28(unittest.TestCase):
    def test_ranking(self):
        result = run_task(28)
        assert_success(self, result)
        self.assertIn("第1名：E", result.stdout)
        self.assertIn("第2名：C", result.stdout)
        self.assertIn("第3名：B", result.stdout)
        self.assertIn("A：第4名", result.stdout)
        self.assertIn("D：第5名", result.stdout)


if __name__ == "__main__":
    unittest.main()
