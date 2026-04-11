from __future__ import annotations

from datetime import datetime
from pathlib import Path
import csv
import os
import sys

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib"))

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

try:
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
    from playwright.sync_api import sync_playwright

    PLAYWRIGHT_AVAILABLE = True
except ModuleNotFoundError:
    PLAYWRIGHT_AVAILABLE = False

STATS_HOME_URL = "https://www.stats.gov.cn/"
YEAR_DATA_URL = "https://data.stats.gov.cn/dg/website/page.html#/pc/national/yearData"
CHROME_EXECUTABLES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]

DATA_FILE = BASE_DIR / "data" / "population_age_structure_2011_2024.txt"
OUTPUT_DIR = BASE_DIR / "output"
PIE_CHART_FILE = OUTPUT_DIR / "recent_three_years_age_ratio_pies.png"
TREND_CHART_FILE = OUTPUT_DIR / "age_ratio_trend_2011_2024.png"
ANALYSIS_FILE = OUTPUT_DIR / "analysis_summary.txt"

FIELDNAMES = [
    "year",
    "total_population",
    "age_0_14_count",
    "age_0_14_ratio",
    "age_15_64_count",
    "age_15_64_ratio",
    "age_65_plus_count",
    "age_65_plus_ratio",
    "total_dependency_ratio",
    "child_dependency_ratio",
    "elderly_dependency_ratio",
]

ROW_MAPPINGS = [
    ("total_population", int),
    ("age_0_14_count", int),
    ("age_15_64_count", int),
    ("age_65_plus_count", int),
    ("total_dependency_ratio", float),
    ("child_dependency_ratio", float),
    ("elderly_dependency_ratio", float),
]

FALLBACK_ROWS = [
    {"year": 2011, "total_population": 134916, "age_0_14_count": 22261, "age_0_14_ratio": 16.5, "age_15_64_count": 100378, "age_15_64_ratio": 74.4, "age_65_plus_count": 12277, "age_65_plus_ratio": 9.1, "total_dependency_ratio": 34.4, "child_dependency_ratio": 22.1, "elderly_dependency_ratio": 12.3},
    {"year": 2012, "total_population": 135922, "age_0_14_count": 22427, "age_0_14_ratio": 16.5, "age_15_64_count": 100718, "age_15_64_ratio": 74.1, "age_65_plus_count": 12777, "age_65_plus_ratio": 9.4, "total_dependency_ratio": 34.9, "child_dependency_ratio": 22.2, "elderly_dependency_ratio": 12.7},
    {"year": 2013, "total_population": 136726, "age_0_14_count": 22423, "age_0_14_ratio": 16.4, "age_15_64_count": 101041, "age_15_64_ratio": 73.9, "age_65_plus_count": 13262, "age_65_plus_ratio": 9.7, "total_dependency_ratio": 35.3, "child_dependency_ratio": 22.2, "elderly_dependency_ratio": 13.1},
    {"year": 2014, "total_population": 137646, "age_0_14_count": 22712, "age_0_14_ratio": 16.5, "age_15_64_count": 101032, "age_15_64_ratio": 73.4, "age_65_plus_count": 13902, "age_65_plus_ratio": 10.1, "total_dependency_ratio": 36.2, "child_dependency_ratio": 22.5, "elderly_dependency_ratio": 13.7},
    {"year": 2015, "total_population": 138326, "age_0_14_count": 22824, "age_0_14_ratio": 16.5, "age_15_64_count": 100978, "age_15_64_ratio": 73.0, "age_65_plus_count": 14524, "age_65_plus_ratio": 10.5, "total_dependency_ratio": 37.0, "child_dependency_ratio": 22.6, "elderly_dependency_ratio": 14.3},
    {"year": 2016, "total_population": 139232, "age_0_14_count": 23252, "age_0_14_ratio": 16.7, "age_15_64_count": 100943, "age_15_64_ratio": 72.5, "age_65_plus_count": 15037, "age_65_plus_ratio": 10.8, "total_dependency_ratio": 37.9, "child_dependency_ratio": 22.9, "elderly_dependency_ratio": 15.0},
    {"year": 2017, "total_population": 140011, "age_0_14_count": 23522, "age_0_14_ratio": 16.8, "age_15_64_count": 100528, "age_15_64_ratio": 71.8, "age_65_plus_count": 15961, "age_65_plus_ratio": 11.4, "total_dependency_ratio": 39.3, "child_dependency_ratio": 23.4, "elderly_dependency_ratio": 15.9},
    {"year": 2018, "total_population": 140541, "age_0_14_count": 23751, "age_0_14_ratio": 16.9, "age_15_64_count": 100065, "age_15_64_ratio": 71.2, "age_65_plus_count": 16724, "age_65_plus_ratio": 11.9, "total_dependency_ratio": 40.4, "child_dependency_ratio": 23.7, "elderly_dependency_ratio": 16.8},
    {"year": 2019, "total_population": 141008, "age_0_14_count": 23689, "age_0_14_ratio": 16.8, "age_15_64_count": 99552, "age_15_64_ratio": 70.6, "age_65_plus_count": 17767, "age_65_plus_ratio": 12.6, "total_dependency_ratio": 41.5, "child_dependency_ratio": 23.8, "elderly_dependency_ratio": 17.8},
    {"year": 2020, "total_population": 141212, "age_0_14_count": 25277, "age_0_14_ratio": 17.9, "age_15_64_count": 96871, "age_15_64_ratio": 68.6, "age_65_plus_count": 19064, "age_65_plus_ratio": 13.5, "total_dependency_ratio": 45.9, "child_dependency_ratio": 26.2, "elderly_dependency_ratio": 19.7},
    {"year": 2021, "total_population": 141260, "age_0_14_count": 24678, "age_0_14_ratio": 17.5, "age_15_64_count": 96526, "age_15_64_ratio": 68.3, "age_65_plus_count": 20056, "age_65_plus_ratio": 14.2, "total_dependency_ratio": 46.3, "child_dependency_ratio": 25.6, "elderly_dependency_ratio": 20.8},
    {"year": 2022, "total_population": 141175, "age_0_14_count": 23908, "age_0_14_ratio": 16.9, "age_15_64_count": 96289, "age_15_64_ratio": 68.2, "age_65_plus_count": 20978, "age_65_plus_ratio": 14.9, "total_dependency_ratio": 46.6, "child_dependency_ratio": 24.8, "elderly_dependency_ratio": 21.8},
    {"year": 2023, "total_population": 140967, "age_0_14_count": 23063, "age_0_14_ratio": 16.3, "age_15_64_count": 96228, "age_15_64_ratio": 68.3, "age_65_plus_count": 21676, "age_65_plus_ratio": 15.4, "total_dependency_ratio": 46.5, "child_dependency_ratio": 24.0, "elderly_dependency_ratio": 22.5},
    {"year": 2024, "total_population": 140828, "age_0_14_count": 22240, "age_0_14_ratio": 15.8, "age_15_64_count": 96565, "age_15_64_ratio": 68.6, "age_65_plus_count": 22023, "age_65_plus_ratio": 15.6, "total_dependency_ratio": 45.8, "child_dependency_ratio": 23.0, "elderly_dependency_ratio": 22.8},
]


def configure_matplotlib() -> None:
    plt.rcParams["font.sans-serif"] = ["PingFang SC", "Hiragino Sans GB", "Arial Unicode MS", "SimHei"]
    plt.rcParams["axes.unicode_minus"] = False


def launch_browser(playwright):
    executable_path = next((path for path in CHROME_EXECUTABLES if Path(path).exists()), None)
    launch_kwargs = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
    if executable_path:
        launch_kwargs["executable_path"] = executable_path
    return playwright.chromium.launch(**launch_kwargs)


def open_year_data_page(page) -> str:
    page.goto(STATS_HOME_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2500)
    annual_data_link = page.locator('a[href*="yearData"]').first
    href = annual_data_link.get_attribute("href") or YEAR_DATA_URL

    try:
        annual_data_link.click()
        page.wait_for_function("() => window.location.href.includes('yearData')", timeout=5000)
        page.wait_for_timeout(4000)
        return "已从国家统计局首页点击“年度数据”进入国家数据页面。"
    except PlaywrightTimeoutError:
        page.goto(href, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(4000)
        return "首页点击“年度数据”超时，已回退到年度数据直链。"


def select_population_table(page) -> None:
    page.get_by_text("人口", exact=True).click(timeout=20000)
    page.wait_for_timeout(1000)
    page.get_by_text("人口年龄结构和抚养比", exact=True).click(timeout=20000)
    page.wait_for_timeout(6000)


def select_recent_15_years(page) -> None:
    page.locator("span.el-input__suffix").click(timeout=10000)
    page.wait_for_timeout(500)
    dropdown = page.locator(".el-select-dropdown.dsf-national-datepage-timer")
    dropdown.get_by_text("最近15年", exact=True).click(timeout=10000)
    dropdown.locator("a.ds-button").click(force=True)
    page.wait_for_function(
        """
        () => Array.from(document.querySelectorAll('.data-table .el-table__header-wrapper th .cell'))
            .some(el => (el.textContent || '').includes('2011'))
        """,
        timeout=30000,
    )
    page.wait_for_timeout(2000)


def extract_table_rows(page) -> list[dict[str, int | float]]:
    headers = [text.strip() for text in page.locator(".data-table .el-table__header-wrapper th .cell").all_inner_texts()]
    years = [int(text.replace("年", "")) for text in headers[1:] if text]
    row_locator = page.locator(".data-table .el-table__body-wrapper tbody tr")

    if row_locator.count() != len(ROW_MAPPINGS):
        raise ValueError(f"抓取到的指标行数异常：{row_locator.count()}")

    records_by_year = {year: {"year": year} for year in years}
    for row_index, (field_name, parser) in enumerate(ROW_MAPPINGS):
        cell_texts = [text.strip() for text in row_locator.nth(row_index).locator("td .cell").all_inner_texts()][1:]
        for year, cell_text in zip(years, cell_texts):
            if cell_text:
                records_by_year[year][field_name] = parser(cell_text)

    records: list[dict[str, int | float]] = []
    for year in sorted(years):
        if 2011 <= year <= 2024:
            row = records_by_year[year]
            required_fields = [field_name for field_name, _ in ROW_MAPPINGS]
            missing_fields = [field_name for field_name in required_fields if field_name not in row]
            if missing_fields:
                raise ValueError(f"{year} 年缺少字段：{', '.join(missing_fields)}")

            total_population = row["total_population"]
            row["age_0_14_ratio"] = round(row["age_0_14_count"] / total_population * 100, 1)
            row["age_15_64_ratio"] = round(row["age_15_64_count"] / total_population * 100, 1)
            row["age_65_plus_ratio"] = round(row["age_65_plus_count"] / total_population * 100, 1)
            records.append(row)
    return records


def scrape_population_age_structure() -> tuple[list[dict[str, int | float]], str]:
    if not PLAYWRIGHT_AVAILABLE:
        return FALLBACK_ROWS, "本地未安装 Playwright，已回退到项目内校对数据。"

    with sync_playwright() as playwright:
        browser = launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1800, "height": 1200})

        try:
            entry_status = open_year_data_page(page)
            select_population_table(page)
            select_recent_15_years(page)
            rows = extract_table_rows(page)
            return rows, f"{entry_status} 已通过 Playwright 抓取“人口年龄结构和抚养比”最近15年数据。"
        finally:
            browser.close()


def get_population_rows() -> tuple[list[dict[str, int | float]], str]:
    try:
        return scrape_population_age_structure()
    except Exception as exc:
        return FALLBACK_ROWS, f"Playwright 抓取失败（{type(exc).__name__}: {exc}），已回退到项目内校对数据。"


def write_text_dataset(rows: list[dict[str, int | float]], source_status: str) -> None:
    with DATA_FILE.open("w", encoding="utf-8", newline="") as file:
        file.write("# 数据来源：国家数据网“年度数据”页面 -> 指标 -> 人口 -> 人口年龄结构和抚养比\n")
        file.write("# 入口首页：https://www.stats.gov.cn/\n")
        file.write(f"# 页面地址：{YEAR_DATA_URL}\n")
        file.write(f"# 抓取时间：{datetime.now().isoformat(timespec='seconds')}\n")
        file.write(f"# 抓取状态：{source_status}\n")
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def load_rows() -> list[dict[str, int | float]]:
    rows: list[dict[str, int | float]] = []
    with DATA_FILE.open("r", encoding="utf-8", newline="") as file:
        data_lines = [line for line in file.readlines() if not line.startswith("#")]
        reader = csv.DictReader(data_lines, delimiter="\t")
        for row in reader:
            parsed_row = {}
            for field in FIELDNAMES:
                if field == "year":
                    parsed_row[field] = int(row[field])
                elif field.endswith("_ratio"):
                    parsed_row[field] = float(row[field])
                else:
                    parsed_row[field] = int(row[field])
            rows.append(parsed_row)
    return rows


def plot_recent_three_year_pies(rows: list[dict[str, int | float]]) -> None:
    latest_rows = rows[-3:]
    labels = ["0-14岁", "15-64岁", "65岁及以上"]
    colors = ["#60A5FA", "#34D399", "#F59E0B"]

    figure, axes = plt.subplots(1, 3, figsize=(15, 5))
    figure.suptitle("最近三年各年龄段人口比例")

    for axis, row in zip(axes, latest_rows):
        sizes = [row["age_0_14_ratio"], row["age_15_64_ratio"], row["age_65_plus_ratio"]]
        axis.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            textprops={"fontsize": 10},
        )
        axis.set_title(f"{row['year']}年")

    figure.tight_layout()
    figure.savefig(PIE_CHART_FILE, dpi=150, bbox_inches="tight")
    plt.close(figure)


def plot_ratio_trend(rows: list[dict[str, int | float]]) -> None:
    years = [row["year"] for row in rows]
    zero_to_fourteen = [row["age_0_14_ratio"] for row in rows]
    fifteen_to_sixty_four = [row["age_15_64_ratio"] for row in rows]
    sixty_five_plus = [row["age_65_plus_ratio"] for row in rows]

    figure, axis = plt.subplots(figsize=(12, 6))
    axis.plot(years, zero_to_fourteen, marker="o", linewidth=2, color="#3B82F6", label="0-14岁")
    axis.plot(years, fifteen_to_sixty_four, marker="o", linewidth=2, color="#10B981", label="15-64岁")
    axis.plot(years, sixty_five_plus, marker="o", linewidth=2, color="#F59E0B", label="65岁及以上")
    axis.axvline(2016, linestyle="--", linewidth=1.2, color="#9CA3AF", label="全面二孩施行（2016-01-01）")

    axis.set_title("2011-2024年各年龄段人口比例走势图")
    axis.set_xlabel("年份")
    axis.set_ylabel("人口比例（%）")
    axis.set_xticks(years)
    axis.tick_params(axis="x", rotation=45)
    axis.grid(linestyle="--", alpha=0.3)
    axis.legend()

    figure.tight_layout()
    figure.savefig(TREND_CHART_FILE, dpi=150, bbox_inches="tight")
    plt.close(figure)


def build_analysis(rows: list[dict[str, int | float]]) -> list[str]:
    first_year = rows[0]
    latest_year = rows[-1]
    policy_year = next(row for row in rows if row["year"] == 2015)
    child_peak = max((row for row in rows if row["year"] >= 2015), key=lambda item: item["age_0_14_ratio"])

    aging_ratio_delta = latest_year["age_65_plus_ratio"] - first_year["age_65_plus_ratio"]
    elderly_dependency_delta = latest_year["elderly_dependency_ratio"] - first_year["elderly_dependency_ratio"]
    child_ratio_delta = child_peak["age_0_14_ratio"] - policy_year["age_0_14_ratio"]

    return [
        (
            f"2011-2024年，65岁及以上人口占比由 {first_year['age_65_plus_ratio']:.1f}% "
            f"升至 {latest_year['age_65_plus_ratio']:.1f}% ，增加 {aging_ratio_delta:.1f} 个百分点；"
            f"同期老年抚养比由 {first_year['elderly_dependency_ratio']:.1f}% 升至 "
            f"{latest_year['elderly_dependency_ratio']:.1f}% ，增加 {elderly_dependency_delta:.1f} 个百分点，"
            "老龄化趋势持续加深。"
        ),
        (
            "2015年10月提出全面二孩政策，2016年1月1日起施行。"
            f"从数据看，0-14岁人口占比从 2015 年的 {policy_year['age_0_14_ratio']:.1f}% "
            f"阶段性上升到 {child_peak['year']} 年的 {child_peak['age_0_14_ratio']:.1f}% ，"
            f"增加 {child_ratio_delta:.1f} 个百分点，说明少儿人口比例在政策开放后出现短期回升。"
        ),
        (
            f"但 2020 年以后，0-14岁人口占比又从 {child_peak['age_0_14_ratio']:.1f}% "
            f"回落到 2024 年的 {latest_year['age_0_14_ratio']:.1f}% ，"
            "说明少儿人口比例的改善并未长期延续。"
        ),
    ]


def write_analysis(lines: list[str]) -> None:
    ANALYSIS_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    configure_matplotlib()

    rows, source_status = get_population_rows()
    rows = sorted(rows, key=lambda item: item["year"])
    write_text_dataset(rows, source_status)
    rows = load_rows()
    plot_recent_three_year_pies(rows)
    plot_ratio_trend(rows)
    analysis_lines = build_analysis(rows)
    write_analysis(analysis_lines)

    print(source_status)
    print(f"年龄结构文本数据已保存：{DATA_FILE.name}")
    print(f"近三年饼图已保存：{PIE_CHART_FILE.name}")
    print(f"比例趋势图已保存：{TREND_CHART_FILE.name}")
    print(f"分析结论已保存：{ANALYSIS_FILE.name}")
    print("分析摘要：")
    for line in analysis_lines:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
