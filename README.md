# Python 上机练习题项目

按题号 `1` 到 `35` 组织的 Python 练习题集合，内置统一启动入口、单题测试和 `uv` 工作流。

> [!WARNING]
> 如果发现运行异常、结果错误或文档问题，请及时提交 Issue。

## Quick Start

```bash
uv sync
uv run main.py
```

直接运行指定题目：

```bash
uv run main.py 7
```

运行依赖第三方库的题目：

```bash
uv sync --extra full
uv run --extra full main.py 24
uv run --extra full main.py 25
uv run --extra full main.py 35
```

## Installation

- 环境要求：`uv`、Python `>=3.9`
- 安装教程：[Python 与 uv 安装教程](docs/INSTALL_PYTHON_UV.md)
- 首次执行 `uv sync` 时会自动生成 `uv.lock`

## Project Layout

- `main.py`：根目录统一启动入口，支持交互选题和命令行指定题号。
- `launcher.py`：启动逻辑实现文件。
- `1/` 到 `35/`：每道题的独立目录。
- `各题目录中的 main.py`：该题的参考实现。
- `各题目录中的 test.py`：该题的基础测试用例。
- `test_utils.py`：测试辅助文件。
- `pyproject.toml`：`uv` 项目配置。
- `docs/INSTALL_PYTHON_UV.md`：安装教程。

配套输入文件：

- `21/zen.txt`
- `22/yzy.txt`
- `23/Wenjian.txt`

运行后可能生成的输出文件：

- `21/zen1.txt`
- `22/yzy2.txt`
- `24/relationship_graph.png`
- `31/cost_product.csv`
- `31/production_analysis.png`
- `32/polynomial_plot.png`
- `33/studentscore.xlsx`
- `33/studentscore.csv`
- `33/studentscore_boxplot.png`
- `35/wa.txt`

## Usage

交互式选择题号：

```bash
uv run main.py
```

直接执行某一题：

```bash
uv run main.py 7
```

仍然可以直接运行题目脚本：

```bash
uv run python 7/main.py
```

## Testing

运行单题测试：

```bash
uv run python 7/test.py
```

批量运行全部测试：

```bash
for i in {1..35}; do uv run python "$i/test.py"; done
```

## Dependency Management

需要运行第 `24` / `25` / `29` / `31` / `32` / `33` / `34` / `35` 题时，启用项目中声明好的 `full` 可选依赖：

```bash
uv sync --extra full
```

如果需要把新依赖正式写入项目，请使用 `uv add`，不要直接用 `uv pip install` 往环境里临时塞包。

例如，把依赖加入 `full` extra：

```bash
uv add --optional full networkx matplotlib jieba numpy pandas openpyxl requests beautifulsoup4
```

## Notes

- 文件读写题会在对应题目目录内读取或写入文件。
- 第 `23` 题会修改 `Wenjian.txt` 的内容。
- 第 `24` 题会在成功运行后生成人物关系图图片。
- 第 `11` 题使用随机数，因此每次运行的具体数值可能不同。
