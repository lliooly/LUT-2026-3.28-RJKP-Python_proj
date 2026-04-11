from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask26(unittest.TestCase):
    def test_xiyouji_analysis(self):
        task_dir = Path(__file__).resolve().parent
        output_files = [
            task_dir / "output" / "character_frequency_top15.txt",
            task_dir / "output" / "character_frequency_top15.png",
            task_dir / "output" / "character_wordcloud_top15.png",
        ]

        for output_file in output_files:
            if output_file.exists():
                output_file.unlink()

        result = run_task(26)
        assert_success(self, result)

        if has_module("jieba") and has_module("matplotlib") and has_module("wordcloud"):
            self.assertIn("《西游记》人物词频 Top 15：", result.stdout)
            for output_file in output_files:
                self.assertTrue(output_file.exists(), msg=f"未生成文件：{output_file}")
        else:
            self.assertIn("uv sync --extra full", result.stdout)


if __name__ == "__main__":
    unittest.main()
