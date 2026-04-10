from pathlib import Path
from urllib.parse import urljoin
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

CATALOG_URL = "https://b.guidaye.com/xiandai/4244/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
    )
}


def fetch_text(url):
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    return response.text


def parse_catalog(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    chapters = []
    seen = set()

    for link in soup.find_all("a", href=True):
        title = " ".join(link.get_text(" ", strip=True).split())
        if not title or len(title) < 2:
            continue

        href = urljoin(base_url, link["href"])
        if href in seen or href == base_url:
            continue
        if "/xiandai/4244/" not in href:
            continue

        chapters.append({"title": title, "url": href})
        seen.add(href)

    return chapters


def parse_chapter_content(html):
    soup = BeautifulSoup(html, "html.parser")
    selectors = [
        "#content",
        ".content",
        ".articleContent",
        ".chapter_content",
        "article",
    ]

    for selector in selectors:
        container = soup.select_one(selector)
        if container is not None:
            pieces = [
                " ".join(node.get_text(" ", strip=True).split())
                for node in container.find_all(["p", "div"])
            ]
            text = "\n".join(part for part in pieces if part)
            if text:
                return text

    paragraphs = [" ".join(node.get_text(" ", strip=True).split()) for node in soup.find_all("p")]
    return "\n".join(part for part in paragraphs if part)


def demo_chapters():
    return [
        {
            "title": "第一章",
            "content": "蝌蚪声、鼓点声和乡村夜色交织在一起，故事从这里开始。",
        },
        {
            "title": "第二章",
            "content": "人物关系逐渐展开，记忆与现实在叙述里不断交错。",
        },
        {
            "title": "第三章",
            "content": "叙述继续推进，情节张力增强，形成完整的演示文本样例。",
        },
    ]


task_dir = Path(__file__).resolve().parent
output_path = task_dir / "wa.txt"

try:
    catalog_html = fetch_text(CATALOG_URL)
    chapters = parse_catalog(catalog_html, CATALOG_URL)
    if not chapters:
        raise requests.RequestException("未解析到章节目录")

    downloaded = []
    for chapter in chapters:
        chapter_html = fetch_text(chapter["url"])
        content = parse_chapter_content(chapter_html)
        downloaded.append({"title": chapter["title"], "content": content or "正文为空。"})
except requests.RequestException:
    print("网络不可用，使用内置示例章节数据。")
    downloaded = demo_chapters()

with output_path.open("w", encoding="utf-8") as file:
    for chapter in downloaded:
        file.write(chapter["title"] + "\n")
        file.write(chapter["content"] + "\n\n")

print(f"共写入 {len(downloaded)} 个章节。")
print(f"文本已保存到：{output_path.name}")
