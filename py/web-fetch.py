#!/usr/bin/env python3

import requests
import sys


def fetch_web(url):
    response = requests.get(url)
    # 检测并设置正确的编码
    response.encoding = response.apparent_encoding or "utf-8"
    return response.text


if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].startswith("http"):
        print("Usage: python web-fetch.py <url>")
        sys.exit(1)
    url = sys.argv[1]

    content = fetch_web(url)
    print(content)
