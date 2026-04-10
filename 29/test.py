from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask29(unittest.TestCase):
    def test_numpy_operations(self):
        result = run_task(29)
        assert_success(self, result)

        if has_module("numpy"):
            self.assertIn("A + B：", result.stdout)
            self.assertIn("A 和 B 中间两行对应元素之和：", result.stdout)
            self.assertIn("A 的 rank：2", result.stdout)
            self.assertIn("A 的 shape：(4, 5)", result.stdout)
        else:
            self.assertIn("uv sync --extra full", result.stdout)


if __name__ == "__main__":
    unittest.main()
