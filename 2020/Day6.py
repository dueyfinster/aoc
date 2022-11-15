#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper


def part1(data):
    result = None
    advent.print_answer(1, result)
    return result


def part2(data):
    result = None
    advent.print_answer(1, result)
    return result


def main():
    advent.setup(2020,6)
    file = advent.read_file()
    nums = helper.get_ints(file)
    part1(nums)
    part2(nums)


if __name__ == '__main__':
    main()
