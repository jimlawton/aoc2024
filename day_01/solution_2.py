#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"File not found: {file}")
        sys.exit(1)

    pairs = []
    with open(file, "r") as f:
        for line in f:
            pairs.append([int(x) for x in line.strip().split()])

    left = [x[0] for x in pairs]
    right = [x[1] for x in pairs]

    similarity = 0
    for i in range(len(left)):
        source = left[i]
        right_count = right.count(source)
        similarity += right_count * source

    print(similarity)


if __name__ == "__main__":
    main()
