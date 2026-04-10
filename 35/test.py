from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask35(unittest.TestCase):
    def test_novel_scraping(self):
        output_path = Path(__file__).resolve().parent / "wa.txt"
        if output_path.exists():
            output_path.unlink()

        try:
            result = run_task(35)
            assert_success(self, result)

            if has_module("requests") and has_module("bs4"):
                self.assertIn("文本已保存到：wa.txt", result.stdout)
                self.assertTrue(output_path.exists())
            else:
                self.assertIn("uv sync --extra full", result.stdout)
        finally:
            if output_path.exists():
                output_path.unlink()


if __name__ == "__main__":
    unittest.main()
