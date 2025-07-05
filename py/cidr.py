#!/usr/bin/env python3
from netaddr import *
import sys

# print(sys.argv)
if len(sys.argv) < 3:
    print("## need 2 ip address")
    exit()

cidrs = iprange_to_cidrs(IPAddress(sys.argv[1]), IPAddress(sys.argv[2]))
print(cidrs)
