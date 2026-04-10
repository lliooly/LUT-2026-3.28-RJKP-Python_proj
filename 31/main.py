from pathlib import Path
import sys

try:
    import matplotlib
    import numpy as np
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

task_dir = Path(__file__).resolve().parent
csv_path = task_dir / "cost_product.csv"
figure_path = task_dir / "production_analysis.png"

cost_matrix = np.array(
    [
        [0.6, 1.8, 0.9],
        [1.8, 2.4, 1.5],
        [0.6, 1.2, 0.9],
    ]
)
quantity_matrix = np.array(
    [
        [4000, 4500, 4500, 4000],
        [2000, 2600, 2400, 2200],
        [5800, 6200, 6000, 5000],
    ]
)

quarters = ["一季度", "二季度", "三季度", "四季度"]
products = ["A", "B", "C"]
cost_types = ["原料", "人工", "管理"]

unit_cost_per_product = cost_matrix.sum(axis=0)
yearly_cost_per_product = unit_cost_per_product * quantity_matrix.sum(axis=1)
total_cost = yearly_cost_per_product.sum()
first_quarter_cost = float(unit_cost_per_product @ quantity_matrix[:, 0])
quarterly_cost_by_type = cost_matrix @ quantity_matrix

print("四个季度三种产品全年成本：")
for product, value in zip(products, yearly_cost_per_product):
    print(f"{product} 产品全年总成本：{value:.2f} 万元")
print(f"工厂全年总成本：{total_cost:.2f} 万元")
print(f"第一季度生产三种产品的总成本：{first_quarter_cost:.2f} 万元")
print("各季度按成本类型汇总的二维数组：")
print(quarterly_cost_by_type)

np.savetxt(csv_path, quarterly_cost_by_type, delimiter=",", fmt="%.2f")
print(f"成本分类数据已写入：{csv_path.name}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for product, series in zip(products, quantity_matrix):
    axes[0].plot(quarters, series, marker="o", linewidth=2, label=product)
axes[0].set_title("四个季度产品产量变化")
axes[0].set_xlabel("季度")
axes[0].set_ylabel("产量")
axes[0].legend()
axes[0].grid(alpha=0.3, linestyle="--")

first_quarter_cost_types = quarterly_cost_by_type[:, 0]
axes[1].pie(
    first_quarter_cost_types,
    labels=cost_types,
    autopct="%.2f%%",
    startangle=90,
)
axes[1].set_title("第一季度成本构成")

fig.tight_layout()
fig.savefig(figure_path, dpi=150)
plt.close(fig)
print(f"图形已保存到：{figure_path.name}")
