#!/usr/bin/env python3
from ngu import read_file


def part1(wire1, wire2):
    pass


def part2(wire1, wire2):
    pass


def main():
    content = read_file(3)
    wire1 = content[0].split(",")
    wire2 = content[1].split(",")

    p1_result = part1(wire1, wire2)
    print("Part 1: {}".format(p1_result))
    p2_result = part2(wire1, wire2)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
