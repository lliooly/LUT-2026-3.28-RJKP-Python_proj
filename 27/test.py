from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask27(unittest.TestCase):
    def test_set_operations(self):
        result = run_task(27)
        assert_success(self, result)
        self.assertIn("参加比赛的所有学生名单：", result.stdout)
        self.assertIn("两项比赛都参加的学生名单：", result.stdout)
        self.assertIn("仅参加一项比赛的学生名单：", result.stdout)
        self.assertIn("['刘小雨', '唐英', '宁成', '张锁', '李晓亮', '李朋']", result.stdout)


if __name__ == "__main__":
    unittest.main()
