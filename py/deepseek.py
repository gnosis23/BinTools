#!/usr/bin/env python3
import os
import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: deepseek.py <message>")
        return

    message = sys.argv[1]

    # 填写你的 API Key
    API_KEY = os.getenv("DEEPSEEK_API_KEY")

    url = "https://api.deepseek.com/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个专业的助手"},
            {"role": "user", "content": message},
        ],
        "stream": False,  # 关闭流式传输
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(result["choices"][0]["message"]["content"])
    else:
        print("请求失败，错误码：", response.status_code)


if __name__ == "__main__":
    main()
