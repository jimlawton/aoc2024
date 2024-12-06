#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

RE = re.compile(r"(mul\([0-9]+,[0-9]+\))")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"File not found: {file}")
        sys.exit(1)

    data = ""
    with open(file, "r") as f:
        data = f.read()

    data = RE.findall(data)

    total = 0
    for expr in data:
        operands = expr.replace("mul(", "").replace(")", "").split(",")
        total += int(operands[0]) * int(operands[1])

    print(total)


if __name__ == "__main__":
    main()
