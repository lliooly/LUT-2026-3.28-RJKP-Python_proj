from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask15(unittest.TestCase):
    def test_product_dict(self):
        result = run_task(15)
        assert_success(self, result)
        self.assertIn("方糖……99元", result.stdout)
        self.assertIn("所有产品的平均价格为：324.00元", result.stdout)
        self.assertIn("价格最高的产品名称为：X1", result.stdout)


if __name__ == "__main__":
    unittest.main()
