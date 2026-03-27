# LUT-2026-3.28-RJKP  Python 上机练习题项目

> [!WARNING] 如果发现运行异常、结果错误或文档问题，请及时提交 Issue。

本项目按题号 `1` 到 `25` 拆分为独立目录，每个目录对应一道题。

## 目录结构

- `1/` 到 `25/`：每道题的独立目录。
- `main.py`：该题的参考实现。
- `test.py`：该题的基础测试用例。
- `test_utils.py`：根目录下的测试辅助文件。

部分题目包含配套数据文件：

- `21/zen.txt`
- `22/yzy.txt`
- `23/Wenjian.txt`

部分题目在运行后会生成输出文件：

- `21/zen1.txt`
- `22/yzy2.txt`
- `24/relationship_graph.png`

## 环境要求

- Python 3.9 或更高版本

第 `24` 题和第 `25` 题需要额外安装第三方库：

```bash
pip3 install networkx matplotlib jieba
```

如果未安装，脚本会输出依赖提示信息。

## 运行方式

进入某道题目录后直接运行：

```bash
cd 7
python3 main.py
```

也可以在项目根目录直接运行某道题：

```bash
python3 7/main.py
```

交互题会按提示从键盘读取输入，例如：

```bash
python3 1/main.py
python3 5/main.py
python3 7/main.py
```

## 测试方式

每道题都提供了一个 `unittest` 测试文件，可以单独运行：

```bash
python3 7/test.py
```

在项目根目录批量运行全部测试：

```bash
for i in {1..25}; do python3 "$i/test.py"; done
```

## 说明

- 文件读写题会在对应题目目录内读取或写入文件。
- 第 `23` 题会修改 `Wenjian.txt` 的内容。
- 第 `24` 题会在成功运行后生成人物关系图图片。
- 第 `11` 题使用随机数，因此每次运行的具体数值可能不同。
