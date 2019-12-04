#!/usr/bin/env python3
from ngu import read_file


def part1():
    pass


def part2():
    pass


def main():
    content = read_file(4)[0].split('-')

    p1_result = part1(content)
    print("Part 1: {}".format(p1_result))
    p2_result = part2(content)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
