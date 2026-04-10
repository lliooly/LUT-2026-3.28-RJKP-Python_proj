from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask33(unittest.TestCase):
    def test_student_score_analysis(self):
        task_dir = Path(__file__).resolve().parent
        excel_path = task_dir / "studentscore.xlsx"
        csv_path = task_dir / "studentscore.csv"
        figure_path = task_dir / "studentscore_boxplot.png"
        excel_existed = excel_path.exists()

        for path in (csv_path, figure_path):
            if path.exists():
                path.unlink()

        try:
            result = run_task(33)
            assert_success(self, result)

            if has_module("pandas") and has_module("matplotlib") and has_module("openpyxl"):
                self.assertIn("五门课程平均分超过 90 分的学生：", result.stdout)
                self.assertIn("黄药师", result.stdout)
                self.assertIn("按总分降序排列的成绩单：", result.stdout)
                self.assertTrue(excel_path.exists())
                self.assertTrue(csv_path.exists())
                self.assertTrue(figure_path.exists())
            else:
                self.assertIn("uv sync --extra full", result.stdout)
        finally:
            for path in (csv_path, figure_path):
                if path.exists():
                    path.unlink()
            if excel_path.exists() and not excel_existed:
                excel_path.unlink()


if __name__ == "__main__":
    unittest.main()
