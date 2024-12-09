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
    for page, rule in page_rules.items():
        print(f"{page}: {rule}")
    print()

    # Start with the longest rule.
    # Replace each page in the rule with the page plus its page rule list.
    # When all are replaced, remove all but the last instance of any page in the list.
    # The end result is a list of pages in the order they should appear.
    correct_order = []
    for page, rule in page_rules.items():
        # print(f"Page {page}, rule {rule}")
        correct_order.extend([page] + rule)
    unique_pages = list(set(correct_order))
    for page in unique_pages:
        while correct_order.count(page) > 1:
            correct_order.remove(page)
    print("Correct order:", correct_order)
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

    middles = []
    for update in good_updates:
        middles.append(update[len(update) // 2])
    print(sum(middles))

    print("Bad updates:")
    for update in bad_updates:
        print(update)
    print()

    corrected_updates = []
    for i, update in enumerate(bad_updates):
        # print(f"Correcting update {update}")
        correct_update = [x for x in correct_order if x in update]
        print(f"Correcting update {update} -> {correct_update}")
        corrected_updates.append(correct_update)
        # print()

    # print("Corrected updates:")
    middles = []
    for update in corrected_updates:
        # print(update)
        middles.append(update[len(update) // 2])
    print()
    print("Sum (corrected):", sum(middles))
    print()


if __name__ == "__main__":
    main()
