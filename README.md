# BinTools

This is a collection of simple command-line tools.

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
