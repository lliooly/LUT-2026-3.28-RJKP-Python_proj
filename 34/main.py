from datetime import date
from urllib.parse import urljoin
import re
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

BASE_URL = "https://www.njtech.edu.cn/index/jjxy.htm"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
    )
}
DATE_PATTERN = re.compile(r"(20\d{2})[-/.年](\d{1,2})[-/.月](\d{1,2})")


def normalize_date(text):
    match = DATE_PATTERN.search(text)
    if not match:
        return None
    year, month, day = map(int, match.groups())
    try:
        return date(year, month, day)
    except ValueError:
        return None


def fetch_text(url):
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    return response.text


def parse_list_page(html, page_url):
    soup = BeautifulSoup(html, "html.parser")
    items = []
    seen = set()

    for node in soup.find_all(["li", "tr", "div"]):
        link = node.find("a", href=True)
        if link is None:
            continue

        title = " ".join(link.get_text(" ", strip=True).split())
        if len(title) < 4:
            continue

        href = urljoin(page_url, link["href"])
        if href in seen or href == page_url:
            continue

        text = node.get_text(" ", strip=True)
        publish_date = normalize_date(text)
        if publish_date is None and "/info/" not in href:
            continue

        items.append(
            {
                "title": title,
                "url": href,
                "date": publish_date,
            }
        )
        seen.add(href)

    return items


def parse_article_content(html):
    soup = BeautifulSoup(html, "html.parser")
    selectors = [
        "#vsb_content",
        ".v_news_content",
        ".wp_articlecontent",
        ".TRS_Editor",
        "article",
    ]

    for selector in selectors:
        container = soup.select_one(selector)
        if container is not None:
            paragraphs = [
                " ".join(node.get_text(" ", strip=True).split())
                for node in container.find_all(["p", "div"])
            ]
            text = "\n".join(part for part in paragraphs if part)
            if text:
                return text

    paragraphs = [" ".join(node.get_text(" ", strip=True).split()) for node in soup.find_all("p")]
    return "\n".join(part for part in paragraphs if part)


def build_demo_dataset():
    demo_pages = {}
    for page_no in range(1, 11):
        page_items = []
        for item_no in range(1, 16):
            if page_no <= 3:
                item_date = date(2024, page_no, item_no)
            elif page_no <= 8:
                item_date = date(2023, page_no - 2, item_no)
            else:
                item_date = date(2022, page_no - 8, item_no)

            page_items.append(
                {
                    "title": f"示例菁菁校园标题 第{page_no}页-{item_no:02d}",
                    "url": f"https://example.com/jjxy/{page_no}/{item_no}.htm",
                    "date": item_date,
                    "content": (
                        f"这是第 {page_no} 页第 {item_no} 条示例新闻的详细内容，"
                        "用于在网络不可用时演示爬虫处理流程。"
                    ),
                }
            )
        demo_pages[page_no] = page_items
    return demo_pages


def get_demo_results():
    demo_pages = build_demo_dataset()
    first_page_items = demo_pages[1]
    first_ten_titles = [item["title"] for page_no in range(1, 11) for item in demo_pages[page_no]]
    titles_2023 = sorted(
        [item for page_no in range(1, 11) for item in demo_pages[page_no] if item["date"].year == 2023],
        key=lambda item: item["date"],
    )
    return first_page_items, first_ten_titles, titles_2023


def deduplicate_items(items):
    unique_items = []
    seen = set()
    for item in items:
        key = item["url"]
        if key in seen:
            continue
        unique_items.append(item)
        seen.add(key)
    return unique_items


def collect_list_pages(max_pages=80):
    pending = [BASE_URL]
    visited = set()
    pages = []

    while pending and len(pages) < max_pages:
        url = pending.pop(0)
        if url in visited:
            continue

        html = fetch_text(url)
        visited.add(url)
        pages.append((url, html))

        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            href = urljoin(url, link["href"])
            if href in visited or href in pending:
                continue
            if "/index/jjxy" not in href or not href.endswith(".htm"):
                continue
            pending.append(href)

    return pages


def get_online_results():
    pages = collect_list_pages()
    if not pages:
        raise requests.RequestException("未抓取到列表页")

    first_page_url, first_page_html = pages[0]
    first_page_items = parse_list_page(first_page_html, first_page_url)[:15]
    detailed_items = []
    for item in first_page_items:
        try:
            content = parse_article_content(fetch_text(item["url"]))
        except requests.RequestException:
            content = "正文抓取失败。"
        detailed_items.append({**item, "content": content or "正文为空。"})

    collected_for_2023 = []
    first_ten_titles = []

    for page_url, html in pages[:10]:
        parsed_items = deduplicate_items(parse_list_page(html, page_url))
        first_ten_titles.extend(item["title"] for item in parsed_items)

    for page_url, html in pages:
        parsed_items = deduplicate_items(parse_list_page(html, page_url))
        collected_for_2023.extend(parsed_items)

    titles_2023 = [item for item in deduplicate_items(collected_for_2023) if item["date"] and item["date"].year == 2023]
    titles_2023.sort(key=lambda item: item["date"])
    return detailed_items, first_ten_titles, titles_2023


try:
    first_page_items, first_ten_titles, titles_2023 = get_online_results()
except requests.RequestException:
    print("网络不可用，使用内置示例数据。")
    first_page_items, first_ten_titles, titles_2023 = get_demo_results()

print("第一页的15条标题及内容：")
for index, item in enumerate(first_page_items[:15], start=1):
    print(f"{index}. {item['title']}")
    print(item["content"])

print("前10页标题：")
for index, title in enumerate(first_ten_titles, start=1):
    print(f"{index}. {title}")
print(f"前10页标题总数：{len(first_ten_titles)}")

print("2023 年标题（按发布时间升序）：")
for item in titles_2023:
    if item["date"] is None:
        continue
    print(f"{item['date'].isoformat()} {item['title']}")
