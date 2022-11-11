#!/usr/bin/env python3
import os
import re
from ngu import read_file
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
    print("Part 1: {}".format(str(result)))


def part2(data):
    r1 = nav_slopes(1, 1, data)
    r2 = nav_slopes(3, 1, data)
    r3 = nav_slopes(5, 1, data)
    r4 = nav_slopes(7, 1, data)
    r5 = nav_slopes(1, 2, data)

    result = r1 * r2 * r3 * r4 * r5
    print("Part 2: {}".format(str(result)))


def main():
    content = read_file(3)
    data = process_input(content)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
