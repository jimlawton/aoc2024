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

    print("Page rules:")
    for page in sorted(page_rules.keys()):
        print(f"{page}: {page_rules[page]}")
    print()

    good_updates = []
    bad_updates = []
    for i, update in enumerate(updates):
        is_bad = False
        for j, page in enumerate(update):
            if page in page_rules:
                pre_pages = update[:j]
                for pre_page in pre_pages:
                    if pre_page in page_rules[page]:
                        is_bad = True
                        break
                post_pages = update[j + 1 :]
                for post_page in post_pages:
                    if post_page in page_rules and page in page_rules[post_page]:
                        is_bad = True
                        break
            else:
                continue
        if is_bad:
            bad_updates.append(update)
        else:
            good_updates.append(update)

    print(f"Good updates: {len(good_updates)}")
    middles = []
    for update in good_updates:
        middles.append(update[len(update) // 2])
    print(sum(middles))

    print(f"Bad updates: {len(bad_updates)}")
    for update in bad_updates:
        print(update)
    print()

    corrected_updates = []
    for i, update in enumerate(bad_updates):
        corrected_update = update[:]
        for j, page in enumerate(update):
            if page in page_rules:
                pre_pages = update[:j]
                for pre_page in pre_pages:
                    if pre_page in page_rules[page]:
                        # Swap the pages.
                        corrected_update[j] = pre_page
                        corrected_update[pre_pages.index(pre_page)] = page
                post_pages = corrected_update[j + 1 :]
                for post_page in post_pages:
                    if post_page in page_rules and page in page_rules[post_page]:
                        # Swap the pages.
                        corrected_update[j] = post_page
                        corrected_update[post_pages.index(post_page)] = page
            else:
                continue
        corrected_updates.append(corrected_update)

    print("Corrected updates:")
    middles = []
    for update in corrected_updates:
        print(update)
        middles.append(update[len(update) // 2])
    print()
    print("Sum (corrected):", sum(middles))


if __name__ == "__main__":
    main()
