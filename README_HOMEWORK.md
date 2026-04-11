# 作业说明（第 26-28 题）

当前分支仅保留第 `26`、`27`、`28` 题，全部使用 `uv` 管理，并保持每题独立可运行。

## 环境准备

```bash
uv sync --extra full
```

统一入口运行：

```bash
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

## 第 26 题：《西游记》人物词频分析

- 输入文件：`[26/data/xiyouji_utf8.txt](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/26/data/xiyouji_utf8.txt)`
- 实现方式：基于 `jieba` 分词和人物别名字典统计人物出现频率。
- 输出文件：
  - `[26/output/character_frequency_top15.txt](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/26/output/character_frequency_top15.txt)`
  - `[26/output/character_frequency_top15.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/26/output/character_frequency_top15.png)`
  - `[26/output/character_wordcloud_top15.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/26/output/character_wordcloud_top15.png)`

## 第 27 题：人口年龄结构与抚养比分析

- 自动化抓取来源：国家统计局首页 -> `年度数据` -> `指标` -> `人口` -> `人口年龄结构和抚养比`
- 抓取方式：`Playwright + Chrome` 无头浏览器自动点击和读取 `.el-table` 表格 DOM
- 文本数据文件：
  - `[27/data/population_age_structure_2011_2024.txt](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/27/data/population_age_structure_2011_2024.txt)`
- 输出文件：
  - `[27/output/recent_three_years_age_ratio_pies.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/27/output/recent_three_years_age_ratio_pies.png)`
  - `[27/output/age_ratio_trend_2011_2024.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/27/output/age_ratio_trend_2011_2024.png)`
  - `[27/output/analysis_summary.txt](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/27/output/analysis_summary.txt)`

说明：

- 由于 `data.stats.gov.cn` 的接口脚本直连经常被 `403` 拦截，当前实现改为真实浏览器自动化抓取。
- 自动化脚本会先从国家统计局首页寻找“年度数据”，再点击“人口”与“人口年龄结构和抚养比”，随后切换到“最近15年”，再从表格 DOM 提取数据。
- 网站如果临时不可用或自动化失败，程序会回退到项目内校对数据，保证题目仍可运行。

## 第 28 题：神经网络模型训练与预测

- 数据集：`sklearn digits` 手写数字数据集
- 预处理：训练/测试集划分 + `MinMaxScaler` 归一化
- 模型：`MLPClassifier(hidden_layer_sizes=(64, 32))`
- 输出文件：
  - `[28/output/metrics_summary.txt](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/28/output/metrics_summary.txt)`
  - `[28/output/training_curves.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/28/output/training_curves.png)`
  - `[28/output/confusion_matrix.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/28/output/confusion_matrix.png)`
  - `[28/output/prediction_samples.png](/Users/shishishi/Desktop/LUT-2026-3.28-RJKP-Python_proj/28/output/prediction_samples.png)`

## 测试

运行单题测试：

```bash
uv run python 26/test.py
uv run python 27/test.py
uv run python 28/test.py
```
