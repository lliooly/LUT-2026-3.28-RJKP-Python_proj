from pathlib import Path
import math
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask11(unittest.TestCase):
    def test_gcd_and_lcm(self):
        result = run_task(11)
        assert_success(self, result)

        values = [int(line.split("：")[-1]) for line in result.stdout.splitlines() if "：" in line]
        rnd1, rnd2, max_gcd, min_lcm = values

        self.assertEqual(max_gcd, math.gcd(rnd1, rnd2))
        expected_lcm = 0 if max_gcd == 0 else abs(rnd1 * rnd2) // max_gcd
        self.assertEqual(min_lcm, expected_lcm)


if __name__ == "__main__":
    unittest.main()
