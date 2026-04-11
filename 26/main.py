from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import os
import sys

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib"))

try:
    import jieba
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

DATA_FILE = BASE_DIR / "data" / "xiyouji_utf8.txt"
OUTPUT_DIR = BASE_DIR / "output"
TOP15_FILE = OUTPUT_DIR / "character_frequency_top15.txt"
BAR_CHART_FILE = OUTPUT_DIR / "character_frequency_top15.png"
WORDCLOUD_FILE = OUTPUT_DIR / "character_wordcloud_top15.png"

CHARACTER_ALIASES = {
    "孙悟空": {"悟空", "行者", "大圣", "齐天大圣", "美猴王", "老孙", "弼马温"},
    "唐僧": {"唐三藏", "三藏", "玄奘", "圣僧", "唐长老"},
    "猪八戒": {"八戒", "悟能", "猪刚鬣", "呆子"},
    "沙僧": {"悟净", "沙和尚"},
    "观音菩萨": {"观音", "观世音", "南海观音"},
    "如来佛祖": {"如来", "佛祖"},
    "玉皇大帝": {"玉帝"},
    "太上老君": {"老君"},
    "太白金星": set(),
    "二郎神": {"杨戬", "显圣真君"},
    "哪吒": {"哪吒太子"},
    "牛魔王": set(),
    "铁扇公主": {"罗刹女"},
    "红孩儿": {"圣婴大王"},
    "白骨精": {"白骨夫人"},
    "镇元子": {"镇元大仙"},
    "黄袍怪": set(),
    "托塔李天王": {"李天王"},
    "东海龙王": {"敖广"},
    "灵吉菩萨": set(),
    "文殊菩萨": {"文殊师利菩萨"},
    "普贤菩萨": set(),
    "嫦娥": {"姮娥"},
    "黑熊精": {"熊罴怪"},
    "黄风怪": {"黄风大王"},
}


def configure_matplotlib() -> None:
    plt.rcParams["font.sans-serif"] = ["PingFang SC", "Hiragino Sans GB", "Arial Unicode MS", "SimHei"]
    plt.rcParams["axes.unicode_minus"] = False


def find_cjk_font() -> str:
    for candidate in [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError("未找到可用于中文词云的字体文件。")


def build_alias_map() -> dict[str, str]:
    alias_map: dict[str, str] = {}
    for canonical_name, aliases in CHARACTER_ALIASES.items():
        all_aliases = {canonical_name, *aliases}
        for alias in sorted(all_aliases, key=len, reverse=True):
            jieba.add_word(alias, freq=200000)
            alias_map[alias] = canonical_name
    return alias_map


def count_characters(text: str, alias_map: dict[str, str]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for token in jieba.lcut(text):
        canonical_name = alias_map.get(token)
        if canonical_name:
            counter[canonical_name] += 1
    return counter


def save_top15_table(top15: list[tuple[str, int]]) -> None:
    with TOP15_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["排名", "人物", "出现次数"])
        for rank, (name, count) in enumerate(top15, start=1):
            writer.writerow([rank, name, count])


def plot_bar_chart(top15: list[tuple[str, int]]) -> None:
    names = [name for name, _ in top15]
    counts = [count for _, count in top15]

    figure, axis = plt.subplots(figsize=(12, 7))
    bars = axis.bar(names, counts, color="#3B82F6", edgecolor="#1D4ED8", linewidth=1.0)
    axis.set_title("《西游记》人物出现频率 Top 15")
    axis.set_xlabel("人物")
    axis.set_ylabel("出现次数")
    axis.tick_params(axis="x", rotation=30)
    axis.grid(axis="y", linestyle="--", alpha=0.3)

    for bar, count in zip(bars, counts):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(counts) * 0.01,
            str(count),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    figure.tight_layout()
    figure.savefig(BAR_CHART_FILE, dpi=150, bbox_inches="tight")
    plt.close(figure)


def generate_wordcloud(top15: list[tuple[str, int]]) -> None:
    wordcloud = WordCloud(
        font_path=find_cjk_font(),
        background_color="white",
        width=1600,
        height=900,
        colormap="tab20",
        max_words=15,
    )
    wordcloud.generate_from_frequencies(dict(top15))
    wordcloud.to_file(str(WORDCLOUD_FILE))


def main() -> int:
    if not DATA_FILE.exists():
        print(f"未找到输入文件：{DATA_FILE}")
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    configure_matplotlib()
    alias_map = build_alias_map()
    text = DATA_FILE.read_text(encoding="utf-8")
    top15 = count_characters(text, alias_map).most_common(15)

    if not top15:
        print("未统计到人物词频，请检查输入文件或别名字典。")
        return 1

    save_top15_table(top15)
    plot_bar_chart(top15)
    generate_wordcloud(top15)

    print("《西游记》人物词频 Top 15：")
    for rank, (name, count) in enumerate(top15, start=1):
        print(f"{rank:>2}. {name:<8}{count}")
    print(f"统计表已保存：{TOP15_FILE.name}")
    print(f"柱状图已保存：{BAR_CHART_FILE.name}")
    print(f"词云图已保存：{WORDCLOUD_FILE.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
