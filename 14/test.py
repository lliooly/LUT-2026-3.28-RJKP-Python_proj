from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask14(unittest.TestCase):
    def test_final_score(self):
        result = run_task(14)
        assert_success(self, result)
        self.assertIn("该参赛选手的最终得分为：8.25", result.stdout)


if __name__ == "__main__":
    unittest.main()
