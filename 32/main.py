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
figure_path = task_dir / "polynomial_plot.png"

poly = np.poly1d([1, 0, 2, 0, 0, 1])
first_derivative = np.polyder(poly, 1)
second_derivative = np.polyder(poly, 2)

print("f(x)=x^5+2x^3+1")
print(f"f(2) = {poly(2)}")
print(f"f(5) = {poly(5)}")
print("一阶导数：")
print(first_derivative)
print("二阶导数：")
print(second_derivative)

plot_poly = np.poly1d([1, 2, 3, 4])
plot_first = np.polyder(plot_poly, 1)
plot_second = np.polyder(plot_poly, 2)
x = np.linspace(-10, 10, 400)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, plot_poly(x), label="f(x)=x^3+2x^2+3x+4", linewidth=2)
ax.plot(x, plot_first(x), label="f'(x)", linewidth=2)
ax.plot(x, plot_second(x), label="f''(x)", linewidth=2)
ax.set_title("函数及其导数图像")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(alpha=0.3, linestyle="--")
ax.legend()

fig.tight_layout()
fig.savefig(figure_path, dpi=150)
plt.close(fig)
print(f"图像已保存到：{figure_path.name}")
