#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
from itertools import combinations

def part1(content):
    combos = list(combinations(content, 2))
    x, y = list(filter(lambda val: sum(val) == 2020, combos))[0]
    result = x * y
    advent.print_answer(2, result)
    return result


def part2(content):
    combos = list(combinations(content, 3))
    x, y, z = list(filter(lambda val: sum(val) == 2020, combos))[0]
    result = x * y * z
    advent.print_answer(2, result)
    return result


def main():
    advent.setup(2020,1)
    file = advent.read_file()
    nums = helper.get_ints(file)
    part1(nums)
    part2(nums)


if __name__ == '__main__':
    main()
