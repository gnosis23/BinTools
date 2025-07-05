#!/usr/bin/env python3

import os
import sys
import json
import requests
from typing import Optional


def get_api_key() -> Optional[str]:
    """Get DeepSeek API key from environment variable"""
    return os.getenv("DEEPSEEK_API_KEY")


def translate_to_shell(text: str, api_key: str) -> Optional[str]:
    """Use DeepSeek V3 API to translate text to shell command"""
    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    prompt = f"""You are a professional system administrator. Please convert the 
    following description into the corresponding shell command.
    Only return the command itself, without any explanation or formatting.

Description: {text}

Example:
"""

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.1,
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()

        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"].strip()
        else:
            print(f"Error: Abnormal API response format: {result}", file=sys.stderr)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed: {e}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: Unknown error: {e}", file=sys.stderr)
        return None


def main():
    """Main function"""
    # Check API key
    api_key = get_api_key()
    if not api_key:
        print(
            "Error: Please set environment variable DEEPSEEK_API_KEY", file=sys.stderr
        )
        print("Usage: export DEEPSEEK_API_KEY=your_api_key", file=sys.stderr)
        sys.exit(1)

    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 sh-copilot.py <description>", file=sys.stderr)
        print(
            "Example: python3 sh-copilot.py 'list all files in current directory'",
            file=sys.stderr,
        )
        print(
            "Example: python3 sh-copilot.py 'find processes containing python'",
            file=sys.stderr,
        )
        sys.exit(1)

    # Join all arguments into one description
    description = " ".join(sys.argv[1:])

    print(f"Translating: {description}")

    # Call API to translate
    shell_command = translate_to_shell(description, api_key)

    if shell_command:
        print(f"Suggested shell command: {shell_command}")
    else:
        print(
            "Translation failed, please check network connection and API key",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
