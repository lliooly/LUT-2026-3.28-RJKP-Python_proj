from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask27(unittest.TestCase):
    def test_population_age_structure_analysis(self):
        task_dir = Path(__file__).resolve().parent
        data_file = task_dir / "data" / "population_age_structure_2011_2024.txt"
        output_files = [
            task_dir / "output" / "recent_three_years_age_ratio_pies.png",
            task_dir / "output" / "age_ratio_trend_2011_2024.png",
            task_dir / "output" / "analysis_summary.txt",
        ]

        for output_file in output_files:
            if output_file.exists():
                output_file.unlink()

        if data_file.exists():
            data_file.unlink()

        result = run_task(27)
        assert_success(self, result)

        if has_module("matplotlib"):
            self.assertIn("年龄结构文本数据已保存：population_age_structure_2011_2024.txt", result.stdout)
            self.assertTrue(data_file.exists())
            for output_file in output_files:
                self.assertTrue(output_file.exists(), msg=f"未生成文件：{output_file}")
        else:
            self.assertIn("uv sync --extra full", result.stdout)


if __name__ == "__main__":
    unittest.main()
