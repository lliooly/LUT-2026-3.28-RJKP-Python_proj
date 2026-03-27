from collections import Counter
from itertools import combinations
from pathlib import Path
import os
import sys

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent / ".matplotlib"))

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import networkx as nx
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

s = (
    "张老师单独给小梅讲了10道习题。"
    "小明问了张老师一个问题。"
    "小红上课开小差被张老师批评了。"
    "小明跟小红下课一起玩了。"
    "小梅、小红还有小明放学后一起打扫卫生了。"
)

names = ["张老师", "小梅", "小明", "小红"]
sentences = [sentence for sentence in s.split("。") if sentence]
edge_counter = Counter()

for sentence in sentences:
    appeared_names = [name for name in names if name in sentence]
    unique_names = sorted(set(appeared_names))
    for pair in combinations(unique_names, 2):
        edge_counter[pair] += 1

edge_list = [(a, b, weight) for (a, b), weight in edge_counter.items()]
print("人物共现关系列表：")
print(edge_list)

graph = nx.Graph()
graph.add_nodes_from(names)
for a, b, weight in edge_list:
    graph.add_edge(a, b, weight=weight)

plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "PingFang SC", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

pos = nx.spring_layout(graph, seed=42)
edge_widths = [graph[u][v]["weight"] for u, v in graph.edges()]

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color="#9ecae1")
nx.draw_networkx_labels(graph, pos, font_size=12)
nx.draw_networkx_edges(graph, pos, width=edge_widths, edge_color="#3182bd")
nx.draw_networkx_edge_labels(
    graph,
    pos,
    edge_labels={(u, v): graph[u][v]["weight"] for u, v in graph.edges()},
)
plt.title("人物关系图")
plt.axis("off")

output_path = Path(__file__).resolve().parent / "relationship_graph.png"
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()

print(f"关系图已保存到：{output_path.name}")
