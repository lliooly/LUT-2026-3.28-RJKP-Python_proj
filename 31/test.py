from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask31(unittest.TestCase):
    def test_factory_analysis(self):
        task_dir = Path(__file__).resolve().parent
        csv_path = task_dir / "cost_product.csv"
        figure_path = task_dir / "production_analysis.png"

        for path in (csv_path, figure_path):
            if path.exists():
                path.unlink()

        try:
            result = run_task(31)
            assert_success(self, result)

            if has_module("numpy") and has_module("matplotlib"):
                self.assertIn("工厂全年总成本：176580.00 万元", result.stdout)
                self.assertIn("第一季度生产三种产品的总成本：41940.00 万元", result.stdout)
                self.assertTrue(csv_path.exists())
                self.assertTrue(figure_path.exists())
            else:
                self.assertIn("uv sync --extra full", result.stdout)
        finally:
            for path in (csv_path, figure_path):
                if path.exists():
                    path.unlink()


if __name__ == "__main__":
    unittest.main()
