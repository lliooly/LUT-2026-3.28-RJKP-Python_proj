from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, has_module, run_task


class TestTask24(unittest.TestCase):
    def test_relationship_graph(self):
        task_dir = Path(__file__).resolve().parent
        output_file = task_dir / "relationship_graph.png"
        if output_file.exists():
            output_file.unlink()

        try:
            result = run_task(24)
            assert_success(self, result)

            if has_module("networkx") and has_module("matplotlib"):
                self.assertIn("人物共现关系列表：", result.stdout)
                self.assertIn("关系图已保存到：relationship_graph.png", result.stdout)
                self.assertTrue(output_file.exists())
            else:
                self.assertIn("请先安装networkx和matplotlib库", result.stdout)
        finally:
            if output_file.exists():
                output_file.unlink()


if __name__ == "__main__":
    unittest.main()
