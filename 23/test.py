from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import assert_success, run_task


class TestTask23(unittest.TestCase):
    def test_replace_world_with_python(self):
        task_dir = Path(__file__).resolve().parent
        file_path = task_dir / "Wenjian.txt"
        original_content = "Hello World\n"
        file_path.write_text(original_content, encoding="utf-8")

        try:
            result = run_task(23)
            assert_success(self, result)
            self.assertIn("替换后的内容：Hello Python", result.stdout)
            self.assertEqual(file_path.read_text(encoding="utf-8").strip(), "Hello Python")
        finally:
            file_path.write_text(original_content, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
