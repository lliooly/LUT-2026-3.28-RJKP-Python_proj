from collections import Counter
from pathlib import Path
import re

base_dir = Path(__file__).resolve().parent
source_file = base_dir / "zen.txt"
target_file = base_dir / "zen1.txt"

text = source_file.read_text(encoding="utf-8")
lines = text.splitlines()
words = re.findall(r"[A-Za-z]+", text)
word_counter = Counter(words)

result_lines = [
    f"行数：{len(lines)}",
    f"单词总数：{len(words)}",
    "词频统计：",
]

for word, count in word_counter.items():
    result_lines.append(f"{word}: {count}")

result = "\n".join(result_lines)
target_file.write_text(result, encoding="utf-8")

print(result)
print(f"统计结果已保存到：{target_file.name}")
