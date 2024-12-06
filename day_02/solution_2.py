#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def is_safe(row):
    if sorted(row) != row and sorted(row, reverse=True) != row:
        return False
    distances = [abs(j - i) for i, j in zip(row, row[1:])]
    min_distance = min(distances)
    max_distance = max(distances)
    return min_distance > 0 and max_distance <= 3


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
        if is_safe(row):
            safe.append(row)
        else:
            unsafe.append(row)

    # Use the Problem Dampener.
    new_safe = safe.copy()
    new_unsafe = []
    for row in unsafe:
        safe_row = False
        for i, elem in enumerate(row):
            mod_row = row.copy()
            del mod_row[i]
            if is_safe(mod_row):
                new_safe.append(row)
                safe_row = True
                break
        if safe_row:
            new_unsafe.append(row)

    print(len(new_safe))


if __name__ == "__main__":
    main()
