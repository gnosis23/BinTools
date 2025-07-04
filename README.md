# BinTools

This is a collection of simple command-line tools.

## sh-copilot.py

自动将自然语言描述翻译为shell命令的工具，使用DeepSeek V3 API。

### 功能特性

- 将自然语言描述转换为对应的shell命令
- 使用DeepSeek V3的HTTP API接口
- 支持安全执行确认
- 完善的错误处理机制

### 前置要求

1. 安装Python依赖：
   ```bash
   pip3 install requests
   ```

2. 设置DeepSeek API密钥环境变量：
   ```bash
   export DEEPSEEK_API_KEY=your_api_key_here
   ```

### 使用方法

```bash
python3 sh-copilot.py "<自然语言描述>"
```

### 示例

```bash
# 列出文件
python3 sh-copilot.py "列出当前目录下的所有文件"

# 查找进程
python3 sh-copilot.py "查找包含python的进程"

# 创建目录
python3 sh-copilot.py "创建一个名为test的目录"

# 查看系统信息
python3 sh-copilot.py "显示系统内存使用情况"
```

程序会显示建议的shell命令，并询问是否执行。

## cidr.py

Converts a range of IP addresses to a list of CIDR blocks.

### Usage

```bash
./cidr.py <start_ip> <end_ip>
```

### Example

```bash
./cidr.py 192.168.0.0 192.168.0.255
```

### Prerequisites

This script requires the `netaddr` Python library. You can install it with pip:

```bash
pip install netaddr
```

## sp.py

Splits a line of text from standard input into words, printing each word on a new line.

### Usage

```bash
echo "this is a test" | ./sp.py
```

This will output:

```
this
is
a
test
```
