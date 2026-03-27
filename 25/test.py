from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask25(unittest.TestCase):
    def test_sentiment_analysis(self):
        result = run_task(25)
        assert_success(self, result)

        if has_module("jieba"):
            self.assertIn("形容词、副词和连词提取结果：", result.stdout)
            self.assertIn("该评论为消极情感。", result.stdout)
        else:
            self.assertIn("请先安装jieba库", result.stdout)


if __name__ == "__main__":
    unittest.main()
