# LUT-2026-3.28-RJKP  Python 上机练习题项目

> [!WARNING] 如果发现运行异常、结果错误或文档问题，请及时提交 Issue。

本项目按题号 `1` 到 `25` 拆分为独立目录，每个目录对应一道题。

安装 Python 和 `uv` 的详细教程见：

- [Python 与 uv 安装教程](docs/INSTALL_PYTHON_UV.md)

## 目录结构

- `1/` 到 `25/`：每道题的独立目录。
- `main.py`：根目录统一启动入口，推荐通过 `uv run main.py` 启动。
- `各题目录中的 main.py`：该题的参考实现。
- `test.py`：该题的基础测试用例。
- `launcher.py`：启动逻辑实现文件。
- `test_utils.py`：根目录下的测试辅助文件。
- `pyproject.toml`：`uv` 项目配置文件。
- `docs/INSTALL_PYTHON_UV.md`：Python 与 `uv` 安装教程。

部分题目包含配套数据文件：

- `21/zen.txt`
- `22/yzy.txt`
- `23/Wenjian.txt`

部分题目在运行后会生成输出文件：

- `21/zen1.txt`
- `22/yzy2.txt`
- `24/relationship_graph.png`

## 环境要求

- 安装 `uv`
- Python 3.9 或更高版本

## 初始化

基础环境同步：

```bash
uv sync
```

首次执行时会自动生成 `uv.lock`。

如果需要运行第 `24` 题和第 `25` 题，使用项目里已经声明好的可选依赖：

```bash
uv sync --extra full
```

也可以在单次运行时直接启用：

```bash
uv run --extra full main.py 24
uv run --extra full main.py 25
```

如果未启用这些依赖，脚本会输出缺库提示信息。

## 依赖维护

如果后续需要把新依赖正式写入项目，请使用 `uv add`，不要直接用 `uv pip install` 往环境里临时塞包。

例如，把可选依赖加到 `full` extra：

```bash
uv add --optional full networkx matplotlib jieba
```

这会把依赖声明写入 `pyproject.toml`，再通过 `uv sync --extra full` 或 `uv run --extra full ...` 使用。

## 运行方式

推荐通过统一启动器运行：

```bash
uv run main.py
```

启动后根据提示输入题号即可。

也可以直接指定题号运行某一题：

```bash
uv run main.py 7
```

如需启用可选依赖运行第 `24` / `25` 题：

```bash
uv run --extra full main.py 24
```

如果仍想直接运行某道题，也可以使用：

```bash
uv run python 7/main.py
```

## 测试方式

每道题都提供了一个 `unittest` 测试文件，可以单独运行：

```bash
uv run python 7/test.py
```

在项目根目录批量运行全部测试：

```bash
for i in {1..25}; do uv run python "$i/test.py"; done
```

## 说明

- 文件读写题会在对应题目目录内读取或写入文件。
- 第 `23` 题会修改 `Wenjian.txt` 的内容。
- 第 `24` 题会在成功运行后生成人物关系图图片。
- 第 `11` 题使用随机数，因此每次运行的具体数值可能不同。
- 根目录 `main.py` 支持交互选择题号，也支持通过命令行参数直接指定题号。
