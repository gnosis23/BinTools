#!/usr/bin/env python3
import os
import requests
import readline
import signal
import sys


def signal_handler(sig, frame):
    """处理Ctrl+C信号"""
    print("\n\nbye!")
    sys.exit(0)


def main():
    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)

    # 填写你的 API Key
    API_KEY = os.getenv("DEEPSEEK_API_KEY")

    if not API_KEY:
        print("DEEPSEEK_API_KEY not found")
        return

    url = "https://api.deepseek.com/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}

    # 初始化对话历史
    messages = [{"role": "system", "content": "你是一个专业的助手"}]

    print("DeepSeek chat")
    print("input 'quit' or 'exit' to exit")
    print("=" * 50)

    while True:
        try:
            # 获取用户输入 (现在支持方向键等编辑功能)
            user_input = input("\nyou: ").strip()

            # 检查退出命令
            if user_input.lower() in ["quit", "exit", "q"]:
                print("bye!")
                break

            if not user_input:
                continue

            # 添加用户消息到历史
            messages.append({"role": "user", "content": user_input})

            # 准备请求数据
            data = {
                "model": "deepseek-chat",
                "messages": messages,
                "stream": False,
            }

            # 显示等待提示
            print("\nAI: thinking...", end="", flush=True)

            # 发送请求
            response = requests.post(url, headers=headers, json=data)

            # 清除"thinking..."提示
            print("\rAI: ", end="", flush=True)

            if response.status_code == 200:
                result = response.json()
                ai_response = result["choices"][0]["message"]["content"]
                print(ai_response)

                # 添加AI回复到历史
                messages.append({"role": "assistant", "content": ai_response})

            else:
                print(f"request failed, error code: {response.status_code}")
                if response.text:
                    print(f"error info: {response.text}")

        except EOFError:
            # 处理Ctrl+D
            print("\nbye!")
            break
        except Exception as e:
            print(f"\nerror: {e}")


if __name__ == "__main__":
    main()
