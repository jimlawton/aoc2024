#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Horizontal:
#
# ....Xxmas. 1
# .samxMS... 1
# ...S..A...
# ..A.A.MS.X
# xmasamx.MM 2
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.xmasX 1  5

# Vertical:
#
#       1  2
# ....XXMAS.
# .SAMXMs...
# ...S..a...
# ..A.A.mS.x
# XMASAMx.Mm
# X.....XA.a
# S.S.S.S.Ss
# .A.A.A.A.a
# ..M.M.M.Mm
# .X.X.XMASx    3

# Diagonals:
#
# ....xXMAS.
# .SAMXmS...
# ...s..a...
# ..a.a.Ms.x
# XmASAmX.mM
# x.....xa.A
# s.s.s.s.sS
# .a.a.a.a.A
# ..m.m.m.mM
# .x.x.xMASx 10

# Diagonal, shift right:
#
# ....XXMAS.
#  .SAMXMS...
#   ...s..A...
#    ..a.A.MS.x
#     XmASAMX.mM
#      x.....Xa.A
#       S.S.s.s.sS
#        .A.a.a.a.A
#         ..m.m.m.MM
#          .x.x.xMASX  5

# Diagonal, shift left:
#
#          ....xXMAS.
#         .SAMXmS...
#        ...s..a...
#       ..A.a.Ms.X
#      XMASAmX.MM
#     X.....xA.A
#    s.s.S.s.SS
#   .a.a.A.a.A
#  ..m.m.M.mM
# .X.x.xMASx  5


def print_rows(rows):
    for row in rows:
        print(row)


def transpose(rows):
    xp_rows = ["".join(x) for x in list(zip(*rows))]
    return xp_rows


def count_horixontal(rows):
    count = 0
    for row in rows:
        if "XMAS" in row:
            count += 1
        if "SAMX" in row:
            count += 1
    return count


def count_vertical(rows):
    rows = transpose(rows)
    count = count_horixontal(rows)
    return count


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

    # Find horizontal.
    h_count = count_horixontal(rows)
    print(f"Horizontal: {h_count}")

    # Find vertical.
    v_count = count_vertical(rows)
    print(f"Vertical: {v_count}")

    max_pad = len(rows) - 1

    # Find diagonals, right.
    padded_rows_right = []
    for i in range(len(rows)):
        padded_rows_right.append("." * i + rows[i] + "." * (max_pad - i))
    dr_count = count_vertical(padded_rows_right)
    print(f"Diagonal, right: {dr_count}")

    # Find diagonals, left.
    padded_rows_left = []
    for i in range(len(rows)):
        padded_rows_left.append("." * (max_pad - i) + rows[i] + "." * i)
    dl_count = count_vertical(padded_rows_left)
    print(f"Diagonal, left: {dl_count}")

    print(h_count + v_count + dr_count + dl_count)


if __name__ == "__main__":
    main()
