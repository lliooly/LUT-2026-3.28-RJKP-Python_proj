from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask4(unittest.TestCase):
    def test_string_operations(self):
        result = run_task(4)
        assert_success(self, result)
        self.assertIn("第一个字符：w", result.stdout)
        self.assertIn("字符串总长度：14", result.stdout)
        self.assertIn("删除标点符号并拆分后的四个字符串：['www', 'moe', 'gov', 'cn']", result.stdout)
        self.assertIn("原字符串没有变化，因为字符串是不可变类型。", result.stdout)


if __name__ == "__main__":
    unittest.main()
