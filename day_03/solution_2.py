#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

RE = re.compile(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))")


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
    mul_enabled = True
    for expr in data:
        if expr[1] == "do()":
            mul_enabled = True
        elif expr[2] == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                operands = expr[0].replace("mul(", "").replace(")", "").split(",")
                total += int(operands[0]) * int(operands[1])

    print(total)


if __name__ == "__main__":
    main()
