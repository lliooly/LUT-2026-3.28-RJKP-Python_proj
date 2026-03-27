from pathlib import Path

file_path = Path(__file__).resolve().parent / "Wenjian.txt"
content = file_path.read_text(encoding="utf-8")

new_content = content.replace("World", "Python")
file_path.write_text(new_content, encoding="utf-8")

print(f"替换前的内容：{content}")
print(f"替换后的内容：{new_content}")
