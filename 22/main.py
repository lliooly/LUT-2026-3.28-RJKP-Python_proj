from pathlib import Path

base_dir = Path(__file__).resolve().parent
source_file = base_dir / "yzy.txt"
target_file = base_dir / "yzy2.txt"

lines = source_file.read_text(encoding="utf-8").splitlines()
one_line_text = "".join(lines)

print(one_line_text)
target_file.write_text(one_line_text, encoding="utf-8")
print(f"内容已写入：{target_file.name}")
