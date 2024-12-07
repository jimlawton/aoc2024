#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Ordering rules have this form:
# 47|53 --> 47 comes before 53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
#
# Updates have this form:
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
#
# page_rules = {
#  29: [13],
#  47: [53, 13, 61, 29],
#  53: [29, 13],
#  61: [13, 53, 29],
#  75: [29, 53, 47, 61, 13],
#  97: [13, 61, 47, 29, 53, 75]
# }
#
# updates = [
#  [75, 47, 61, 53, 29],
#  [97, 61, 53, 29, 13],
#  [75, 29, 13],
#  [75, 97, 47, 61, 53],
#  [61, 13, 29],
#  [97, 13, 75, 29, 47]
# ]


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

    ordering_rules = []
    updates = []
    for row in rows:
        if "|" in row:
            ordering_rules.append([int(x) for x in row.split("|")])
        if "," in row:
            updates.append([int(x) for x in row.split(",")])

    page_rules = {}
    for rule in ordering_rules:
        if rule[0] not in page_rules:
            page_rules[rule[0]] = [rule[1]]
        else:
            page_rules[rule[0]].append(rule[1])

    num_violations = 0
    good_updates = []
    bad_updates = []
    for i, update in enumerate(updates):
        # print(f"Checking update {update}")
        is_bad = False
        for j, page in enumerate(update):
            # print(f"Checking page {page}")
            if page in page_rules:
                # print(f"Page rule for {page}: {page_rules[page]}")
                pre_pages = update[:j]
                for pre_page in pre_pages:
                    if pre_page in page_rules[page]:
                        # print(f"Violation: found {pre_page} before {page}")
                        num_violations += 1
                        is_bad = True
                        break
                post_pages = update[j + 1 :]
                for post_page in post_pages:
                    if post_page in page_rules and page in page_rules[post_page]:
                        # print(f"Violation: found {page} before {post_page}")
                        num_violations += 1
                        is_bad = True
                        break
            else:
                # print(f"No page rule for {page}, ignoring...")
                continue
        if is_bad:
            # print(f"{update} bad")
            bad_updates.append(update)
        else:
            # print(f"{update} good")
            good_updates.append(update)

    # print(f"Total violations: {num_violations}")
    # print("Bad updates:")
    # for update in bad_updates:
    #     print(update)
    # print("Good updates:")
    # for update in good_updates:
    #     print(update)
    middles = []
    for update in good_updates:
        middles.append(update[len(update) // 2])
    print(sum(middles))


if __name__ == "__main__":
    main()
