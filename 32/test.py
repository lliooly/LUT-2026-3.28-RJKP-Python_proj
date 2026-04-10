from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask32(unittest.TestCase):
    def test_polynomial(self):
        figure_path = Path(__file__).resolve().parent / "polynomial_plot.png"
        if figure_path.exists():
            figure_path.unlink()

        try:
            result = run_task(32)
            assert_success(self, result)

            if has_module("numpy") and has_module("matplotlib"):
                self.assertIn("f(2) = 49", result.stdout)
                self.assertIn("f(5) = 3376", result.stdout)
                self.assertIn("一阶导数：", result.stdout)
                self.assertTrue(figure_path.exists())
            else:
                self.assertIn("uv sync --extra full", result.stdout)
        finally:
            if figure_path.exists():
                figure_path.unlink()


if __name__ == "__main__":
    unittest.main()
