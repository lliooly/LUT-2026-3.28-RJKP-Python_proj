from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask13(unittest.TestCase):
    def test_student_list_operations(self):
        result = run_task(13)
        assert_success(self, result)
        self.assertIn("学号为003的学生信息：['003', '张武', 18]", result.stdout)
        self.assertIn("李梅", result.stdout)
        self.assertIn("刘祥", result.stdout)
        self.assertIn("['005', '林歌', 20]", result.stdout)


if __name__ == "__main__":
    unittest.main()
