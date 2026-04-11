from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask28(unittest.TestCase):
    def test_neural_network_digits(self):
        task_dir = Path(__file__).resolve().parent
        output_files = [
            task_dir / "output" / "metrics_summary.txt",
            task_dir / "output" / "training_curves.png",
            task_dir / "output" / "confusion_matrix.png",
            task_dir / "output" / "prediction_samples.png",
        ]

        for output_file in output_files:
            if output_file.exists():
                output_file.unlink()

        result = run_task(28)
        assert_success(self, result)

        if has_module("sklearn") and has_module("matplotlib"):
            self.assertIn("测试集准确率：", result.stdout)
            for output_file in output_files:
                self.assertTrue(output_file.exists(), msg=f"未生成文件：{output_file}")
        else:
            self.assertIn("uv sync --extra full", result.stdout)


if __name__ == "__main__":
    unittest.main()
