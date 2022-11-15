#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
from pprint import pprint


def process_input(content):
    data = []
    for line in content:
        data.append([char for char in line])
    return data


def nav_slopes(right, down, data):
    x = 0
    result = 0
    width = len(data[0])

    for i, row in enumerate(data):
        if i % down != 0:
            continue
        if row[x] == '#':
            result = result + 1
        x = (x + right) % width
    return result


def part1(data):
    result = nav_slopes(3, 1, data)
    advent.print_answer(1, result)
    return result


def part2(data):
    r1 = nav_slopes(1, 1, data)
    r2 = nav_slopes(3, 1, data)
    r3 = nav_slopes(5, 1, data)
    r4 = nav_slopes(7, 1, data)
    r5 = nav_slopes(1, 2, data)

    result = r1 * r2 * r3 * r4 * r5
    advent.print_answer(2, result)
    return result


def main():
    advent.setup(2020, 3)
    file = advent.read_file()
    data = helper.get_lines(file)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
