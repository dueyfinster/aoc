#!/usr/bin/env python3
import os
import math
from ngu import read_file
from itertools import combinations


def part1(content):
    combos = list(combinations(content, 2))
    x, y = list(filter(lambda val: sum(val) == 2020, combos))[0]
    result = x * y

    print("Part 1: {}".format(str(result)))


def part2(content):
    combos = list(combinations(content, 3))
    x, y, z = list(filter(lambda val: sum(val) == 2020, combos))[0]
    result = x * y * z

    print("Part 2: {}".format(str(result)))


def main():
    content = read_file(1)
    nums = list(map(int, content))
    part1(nums)
    part2(nums)


if __name__ == '__main__':
    main()
