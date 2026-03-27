# Python 与 uv 安装教程

本教程用于帮助首次接触本项目的使用者安装 `Python` 和 `uv`，并完成项目初始化。

## 推荐方案

推荐先安装 `uv`，再由 `uv` 管理 Python。

原因：

- 命令更统一。
- 后续运行项目、同步依赖、切换 Python 版本都更方便。
- 更适合和本项目当前的 `uv` 工作流配合。

## 第一步：安装 uv

### macOS / Linux

在终端执行：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

如果系统没有 `curl`，也可以使用：

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

### Windows

在 PowerShell 中执行：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 验证是否安装成功

```bash
uv --version
```

如果能看到版本号，说明 `uv` 已可用。

## 第二步：安装 Python

### 方案 A：用 uv 安装 Python

这是本项目最推荐的方式。

安装最新可用 Python：

```bash
uv python install
```

如果希望同时提供 `python` 和 `python3` 这样的默认命令，可执行：

```bash
uv python install --default
```

安装完成后检查：

```bash
python --version
uv python list
```

## 方案 B：从 Python 官网下载安装

如果不想让 `uv` 管理 Python，也可以直接从 Python 官方渠道安装。

官方下载页：

- [Python 官方下载页](https://www.python.org/downloads/)

### Windows

Windows 官方文档当前推荐使用 Python Install Manager。它可以从 `python.org/downloads` 下载，也可以通过 Microsoft Store 安装。

安装完成后，通常可以直接使用：

```powershell
python
py
```

查看已安装版本：

```powershell
py list
```

### macOS

可以从 Python 官网下载适用于 macOS 的官方安装包并按提示安装。官方文档说明，当前 macOS 提供的是可同时支持 Apple Silicon 和 Intel 的安装包。

安装完成后可检查：

```bash
python3 --version
```

### Linux

Linux 上更推荐直接使用 `uv python install` 或发行版自带的包管理器安装 Python。Python 官方下载页主要提供源码包，很多 Linux 环境并不以图形安装包为主。

## 第三步：初始化本项目

进入项目根目录后执行：

```bash
uv sync
```

首次执行时会自动生成 `uv.lock`。

如果需要运行依赖第三方库的题目，再启用可选依赖：

```bash
uv sync --extra full
```

## 第四步：运行项目

交互式选择题号：

```bash
uv run main.py
```

直接运行指定题号：

```bash
uv run main.py 7
```

运行需要额外依赖的题目：

```bash
uv run --extra full main.py 24
uv run --extra full main.py 25
```

## 常见问题

### 1. 终端提示找不到 `uv`

说明 `uv` 还未加入当前终端的 `PATH`，可尝试：

- 关闭并重新打开终端。
- 重新登录系统后再试。
- 按 `uv` 官方安装文档检查 PATH 设置。

### 2. 终端提示找不到 `python`

如果你是通过 `uv` 安装 Python，先执行：

```bash
uv python install --default
```

如果是官网下载方式，请确认安装时已经把 Python 命令加入 PATH，或重新打开终端后再试。

### 3. 第 24 题和第 25 题无法运行

这两题依赖 `networkx`、`matplotlib`、`jieba`。请执行：

```bash
uv sync --extra full
```

## 官方参考资料

- [uv 安装文档](https://docs.astral.sh/uv/getting-started/installation/)
- [uv 安装和管理 Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv 项目工作流](https://docs.astral.sh/uv/guides/projects/)
- [uv 运行脚本文档](https://docs.astral.sh/uv/guides/scripts/)
- [Python 官方下载页](https://www.python.org/downloads/)
- [Python Windows 安装文档](https://docs.python.org/3/using/windows.html)
- [Python macOS 安装文档](https://docs.python.org/3.11/using/mac.html)
