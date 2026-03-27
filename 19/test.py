from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask19(unittest.TestCase):
    def test_password_level(self):
        result = run_task(19, "Abc12345\n")
        assert_success(self, result)
        self.assertIn("Abc12345的密码强度为4级", result.stdout)


if __name__ == "__main__":
    unittest.main()
