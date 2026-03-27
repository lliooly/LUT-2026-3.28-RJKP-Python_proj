from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask16(unittest.TestCase):
    def test_city_statistics(self):
        result = run_task(16)
        assert_success(self, result)
        self.assertIn("张三风去过2个城市", result.stdout)
        self.assertIn("李茉绸去过3个城市", result.stdout)
        self.assertIn("慕容福去过4个城市", result.stdout)
        self.assertIn("去过上海的有2人，他们是李茉绸、慕容福", result.stdout)


if __name__ == "__main__":
    unittest.main()
