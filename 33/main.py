from pathlib import Path
import sys

try:
    import matplotlib
    import openpyxl  # noqa: F401
    import pandas as pd
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

task_dir = Path(__file__).resolve().parent
excel_path = task_dir / "studentscore.xlsx"
csv_path = task_dir / "studentscore.csv"
figure_path = task_dir / "studentscore_boxplot.png"

sample_rows = [
    [1, "郭靖", 85, 80, 71, 75, 95],
    [2, "黄蓉", 90, 95, 80, 85, 90],
    [3, "杨过", 88, 87, 75, 90, 93],
    [4, "小龙女", 92, 83, 78, 88, 91],
    [5, "乔峰", 86, 80, 78, 89, 90],
    [6, "张无忌", 91, 92, 78, 89, 90],
    [7, "韦小宝", 98, 95, 70, 70, 85],
    [8, "洪七公", 83, 85, 78, 81, 96],
    [9, "黄药师", 94, 95, 80, 96, 98],
    [10, "周伯通", 80, 81, 70, 75, 94],
]
columns = ["学号", "姓名", "语文", "数学", "英语", "美术", "体育"]
subjects = ["语文", "数学", "英语", "美术", "体育"]


def ensure_workbook(path):
    if path.exists():
        return

    df = pd.DataFrame(sample_rows, columns=columns)
    df.to_excel(path, index=False)


ensure_workbook(excel_path)

df = pd.read_excel(excel_path)
df["总分"] = df[subjects].sum(axis=1)
df["均分"] = df[subjects].mean(axis=1)
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

avg_over_90 = df.loc[df["均分"] > 90, ["学号", "姓名"]]
math_avg = df["数学"].mean()
math_over_avg = df.loc[df["数学"] > math_avg, ["学号", "姓名"]]
sorted_df = df.sort_values(by="总分", ascending=False)

print("读取到的成绩数据：")
print(df)
print("五门课程平均分超过 90 分的学生：")
print(avg_over_90.to_string(index=False))
print(f"数学平均分：{math_avg:.1f}")
print("数学成绩超过班级平均分的学生：")
print(math_over_avg.to_string(index=False))
print("按总分降序排列的成绩单：")
print(sorted_df.to_string(index=False))
print(f"更新后的数据已写入：{csv_path.name}")

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([df[subject] for subject in subjects], labels=subjects, patch_artist=True)
ax.set_title("五门课程成绩箱形图")
ax.set_xlabel("课程")
ax.set_ylabel("分数")
ax.set_ylim(60, 100)
ax.grid(axis="y", alpha=0.3, linestyle="--")

fig.tight_layout()
fig.savefig(figure_path, dpi=150)
plt.close(fig)
print(f"箱形图已保存到：{figure_path.name}")
