# Python 作业项目

当前分支只保留三个作业模块：`26`、`27`、`28`。项目使用 `uv` 管理，支持统一入口运行和单题测试。

## 快速开始

```bash
uv sync --extra full
uv run main.py --list
uv run main.py 26
uv run main.py 27
uv run main.py 28
```

也可以直接运行单题脚本：

```bash
uv run python 26/main.py
uv run python 27/main.py
uv run python 28/main.py
```

## 项目结构

- `main.py`：根目录启动入口。
- `launcher.py`：题目发现和运行逻辑。
- `26/`：`西游记` 人物词频统计、柱状图、词云。
- `27/`：使用 `Playwright` 自动抓取人口年龄结构与抚养比数据，并生成饼图、折线图和分析结论。
- `28/`：神经网络数据预处理、模型训练、结果分析、预测展示。
- `test_utils.py`：测试辅助函数。
- `pyproject.toml`：`uv` 项目配置。
- `README_HOMEWORK.md`：三道作业的详细说明。

## 测试

```bash
uv run python 26/test.py
uv run python 27/test.py
uv run python 28/test.py
```

## 说明

- 运行三道题前都建议先执行 `uv sync --extra full`。
- 第 `27` 题会优先用 `Playwright` 从国家统计局首页点击进入“年度数据”页面并抓取表格；如果自动化失败，会回退到项目内校对数据。
- 第 `26-28` 题的详细说明见 [README_HOMEWORK.md](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/README_HOMEWORK.md)。
