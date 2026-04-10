from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask34(unittest.TestCase):
    def test_web_scraping(self):
        result = run_task(34)
        assert_success(self, result)

        if has_module("requests") and has_module("bs4"):
            self.assertIn("第一页的15条标题及内容：", result.stdout)
            self.assertIn("前10页标题：", result.stdout)
            self.assertIn("前10页标题总数：", result.stdout)
            self.assertIn("2023 年标题（按发布时间升序）：", result.stdout)
        else:
            self.assertIn("uv sync --extra full", result.stdout)


if __name__ == "__main__":
    unittest.main()
