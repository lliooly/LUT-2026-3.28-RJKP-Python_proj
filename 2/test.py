from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask2(unittest.TestCase):
    def test_reverse_number(self):
        result = run_task(2, "123\n")
        assert_success(self, result)
        self.assertIn("这个三位数的反序数为：321", result.stdout)


if __name__ == "__main__":
    unittest.main()
