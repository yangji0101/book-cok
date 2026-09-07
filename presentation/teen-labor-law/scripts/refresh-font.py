#!/usr/bin/env python3
"""덱에 실제로 쓰인 글자만 담은 Noto Sans KR 서브셋을 다시 받는다.

문구를 크게 고쳤다면 한 번 돌린다:  npm run font
(고친 글자가 서브셋에 없으면 그 글자만 시스템 기본 글꼴로 보인다.)
"""

import os
import re
import urllib.parse
import urllib.request

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")
FONT_DIR = os.path.join(ROOT, "assets", "fonts")


def fetch(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60
    ).read()


def main():
    html = open(HTML, encoding="utf-8").read()
    body = html.split("<body>", 1)[1]
    # 태그를 걷어내고 화면 텍스트 + 발표자 노트에서 글자 집합을 만든다
    text = re.sub(r"<[^>]+>", " ", body)
    subset = "".join(sorted({c for c in text if not c.isspace()}))

    css = fetch(
        "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&text="
        + urllib.parse.quote(subset)
    ).decode()

    os.makedirs(FONT_DIR, exist_ok=True)
    for i, url in enumerate(sorted(set(re.findall(r"url\((https://fonts\.gstatic\.com[^)]+)\)", css)))):
        name = "noto-sans-kr-%d.woff2" % i
        data = fetch(url)
        open(os.path.join(FONT_DIR, name), "wb").write(data)
        css = css.replace(url, "assets/fonts/" + name)
        print("%s  %.1f KB" % (name, len(data) / 1024))

    open(os.path.join(FONT_DIR, "noto-sans-kr.css"), "w", encoding="utf-8").write(css)

    # index.html 의 FONT:START ~ FONT:END 구간을 새 @font-face 로 갈아 끼운다
    indented = "\n".join(("      " + l) if l.strip() else l for l in css.rstrip().splitlines())
    head, rest = html.split("/* FONT:START", 1)
    _, tail = rest.split("/* FONT:END */", 1)
    html = (
        head
        + "/* FONT:START — `npm run font` 이 이 구간을 다시 써넣는다. 손으로 고치지 말 것 */\n"
        + indented
        + "\n      /* FONT:END */"
        + tail
    )
    open(HTML, "w", encoding="utf-8").write(html)

    print("\n글자 %d자 · index.html 의 @font-face 구간까지 갱신했습니다." % len(subset))


if __name__ == "__main__":
    main()
