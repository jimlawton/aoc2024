#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def print_state(state):
    for row in state:
        print("".join(row))


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"File not found: {file}")
        sys.exit(1)

    start_state = []
    with open(file, "r") as f:
        start_state = [list(x.strip()) for x in f.readlines()]

    print("Start state:")
    print_state(start_state)

    curr_state = start_state.copy()

    start_loc = ()
    for i, row in enumerate(start_state):
        for j, col in enumerate(row):
            if col == "^":
                start_loc = (i, j)
    print(f"Found guard at ({i}, {j})")

    curr_loc = start_loc
    direction = "U"
    while True:
        # print(f"Current loc: {curr_loc}")
        if (
            curr_loc[0] == 0
            or curr_loc[1] == 0
            or curr_loc[0] == len(start_state) - 1
            or curr_loc[1] == len(start_state[0]) - 1
        ):
            curr_state[curr_loc[0]][curr_loc[1]] = "X"
            print(f"Guard escaped at ({curr_loc[0]}, {curr_loc[1]})")
            break
        if direction == "U":
            next_loc = (curr_loc[0] - 1, curr_loc[1])
            if curr_state[next_loc[0]][next_loc[1]] == "#":
                direction = "R"
                next_loc = (curr_loc[0], curr_loc[1] + 1)
        elif direction == "D":
            next_loc = (curr_loc[0] + 1, curr_loc[1])
            if curr_state[next_loc[0]][next_loc[1]] == "#":
                direction = "L"
                next_loc = (curr_loc[0], curr_loc[1] - 1)
        elif direction == "L":
            next_loc = (curr_loc[0], curr_loc[1] - 1)
            if curr_state[next_loc[0]][next_loc[1]] == "#":
                direction = "U"
                next_loc = (curr_loc[0] - 1, curr_loc[1])
        elif direction == "R":
            next_loc = (curr_loc[0], curr_loc[1] + 1)
            if curr_state[next_loc[0]][next_loc[1]] == "#":
                direction = "D"
                next_loc = (curr_loc[0] + 1, curr_loc[1])
        # print(f"Next loc: {next_loc}")

        # print_state(curr_state)
        curr_state[curr_loc[0]][curr_loc[1]] = "X"
        curr_state[next_loc[0]][next_loc[1]] = "^"
        curr_loc = next_loc

    print("Final state:")
    print_state(curr_state)

    print("Total steps: ", sum([x.count("X") for x in curr_state]))


if __name__ == "__main__":
    main()
