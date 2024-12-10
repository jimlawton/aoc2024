#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def print_state(state):
    for row in state:
        print(row)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"File not found: {file}")
        sys.exit(1)

    with open(file, "r") as f:
        equations = [x.strip() for x in f.readlines()]

    print("Equations:")
    print_state(equations)

    max_len = 0
    for equation in equations:
        lhs = int(equation.split(":")[0].strip())
        rhs_list = [int(x) for x in equation.split(":")[1].strip().split()]
        print(f"lhs: {lhs}, rhs_list: {rhs_list}")
        max_len = max(max_len, len(rhs_list))

    print(max_len)


if __name__ == "__main__":
    main()
