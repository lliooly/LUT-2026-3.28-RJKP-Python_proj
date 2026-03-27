from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask3(unittest.TestCase):
    def test_practice_and_decline(self):
        result = run_task(3)
        assert_success(self, result)
        self.assertIn("一年后每天练功的武力值为：37.78", result.stdout)
        self.assertIn("一年后每天不练功的武力值为：0.03", result.stdout)


if __name__ == "__main__":
    unittest.main()
