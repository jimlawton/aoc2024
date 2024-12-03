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

    rows = []
    with open(file, "r") as f:
        for line in f:
            rows.append([int(x) for x in line.strip().split()])

    safe = []
    unsafe = []

    for row in rows:
        if sorted(row) != row and sorted(row, reverse=True) != row:
            unsafe.append(row)
            continue
        distances = [abs(j - i) for i, j in zip(row, row[1:])]
        min_distance = min(distances)
        max_distance = max(distances)
        if min_distance > 0 and max_distance <= 3:
            safe.append(row)
        else:
            unsafe.append(row)

    print(len(safe))


if __name__ == "__main__":
    main()
