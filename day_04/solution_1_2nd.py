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

    count = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            search_right = search_left = search_up = search_down = False
            if rows[i][j] == "X":
                search_left = j >= 3
                search_right = j <= len(rows) - 4
                search_up = i >= 3
                search_up_left = search_left and search_up
                search_up_right = search_right and search_up
                search_down = i <= len(rows) - 4
                search_down_left = search_left and search_down
                search_down_right = search_right and search_down

                if search_left:
                    if (
                        rows[i][j - 1] == "M"
                        and rows[i][j - 2] == "A"
                        and rows[i][j - 3] == "S"
                    ):
                        # print(f"Found XMAS (U) at ({i}, {j})")
                        count += 1

                if search_right:
                    if (
                        rows[i][j + 1] == "M"
                        and rows[i][j + 2] == "A"
                        and rows[i][j + 3] == "S"
                    ):
                        # print(f"Found XMAS (U) at ({i}, {j})")
                        count += 1

                if search_up:
                    # Vertical search up.
                    if (
                        rows[i - 1][j] == "M"
                        and rows[i - 2][j] == "A"
                        and rows[i - 3][j] == "S"
                    ):
                        # print(f"Found XMAS (U) at ({i}, {j})")
                        count += 1

                if search_up_left:
                    # Left diagonal search up.
                    if (
                        rows[i - 1][j - 1] == "M"
                        and rows[i - 2][j - 2] == "A"
                        and rows[i - 3][j - 3] == "S"
                    ):
                        # print(f"Found XMAS (LU) at ({i}, {j})")
                        count += 1

                if search_up_right:
                    # Right diagonal search up.
                    if (
                        rows[i - 1][j + 1] == "M"
                        and rows[i - 2][j + 2] == "A"
                        and rows[i - 3][j + 3] == "S"
                    ):
                        # print(f"Found XMAS (RU) at ({i}, {j})")
                        count += 1

                if search_down:
                    # Vertical search down.
                    if (
                        rows[i + 1][j] == "M"
                        and rows[i + 2][j] == "A"
                        and rows[i + 3][j] == "S"
                    ):
                        # print(f"Found XMAS (D) at ({i}, {j})")
                        count += 1

                if search_down_left:
                    # Left diagonal search down.
                    if (
                        rows[i + 1][j - 1] == "M"
                        and rows[i + 2][j - 2] == "A"
                        and rows[i + 3][j - 3] == "S"
                    ):
                        # print(f"Found XMAS (LD) at ({i}, {j})")
                        count += 1

                if search_down_right:
                    # Right diagonal search down.
                    if (
                        rows[i + 1][j + 1] == "M"
                        and rows[i + 2][j + 2] == "A"
                        and rows[i + 3][j + 3] == "S"
                    ):
                        # print(f"Found XMAS (RD) at ({i}, {j})")
                        count += 1

    print(count)


if __name__ == "__main__":
    main()
