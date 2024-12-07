#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def print_rows(rows):
    for row in rows:
        print(row)


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
        rows = [x.strip() for x in f.readlines()]
    if "" in rows:
        rows.remove("")

    # print_rows(rows)

    count = 0
    # If we search for 'A' cells, then we can find any intersecting 'MAS' sequences.
    # The only 'A' cells that can form X-MAS are the ones that are not on the edge of the grid.
    for i in range(1, len(rows) - 1):
        # print(f"Row {i}")
        for j in range(1, len(rows[i]) - 1):
            # print(f"Col: {j}")
            if rows[i][j] == "A":
                # print(f"Found A at {i}, {j}")
                mas_count = 0

                # Looks like the solution doesn't want to count anything other than the diagonals!

                # # L-R
                # if (rows[i][j - 1] == "M" and rows[i][j + 1] == "S") or (
                #     rows[i][j - 1] == "S" and rows[i][j + 1] == "M"
                # ):
                #     print(f"Found MAS (LR) at {i}, {j}")
                #     mas_count += 1
                # # U-D
                # if (rows[i - 1][j] == "M" and rows[i + 1][j] == "S") or (
                #     rows[i - 1][j] == "S" and rows[i + 1][j] == "M"
                # ):
                #     print(f"Found MAS (UD) at {i}, {j}")
                #     mas_count += 1

                # U-L-D-R
                if (rows[i - 1][j - 1] == "M" and rows[i + 1][j + 1] == "S") or (
                    rows[i - 1][j - 1] == "S" and rows[i + 1][j + 1] == "M"
                ):
                    # print(f"Found MAS (ULDR) at {i}, {j}")
                    mas_count += 1

                # U-R-D-L
                if (rows[i + 1][j - 1] == "M" and rows[i - 1][j + 1] == "S") or (
                    rows[i + 1][j - 1] == "S" and rows[i - 1][j + 1] == "M"
                ):
                    # print(f"Found MAS (URDL) at {i}, {j}")
                    mas_count += 1
                # print(f"MAS count {i}, {j}: {mas_count}")

                if mas_count >= 2:
                    # print(f"Found MAS at {i}, {j}")
                    count += 1

    print(count)


if __name__ == "__main__":
    main()
