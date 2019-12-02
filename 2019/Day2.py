#!/usr/bin/env python3
import os
from ngu import read_file


def part1(content):
    for i in range(0, len(content), 4):
        opcode = int(content[i])
        pos1 = int(content[i+1])
        pos2 = int(content[i+2])
        result_pos = int(content[i+3])
        val1 = int(content[pos1])
        val2 = int(content[pos2])

        if opcode == 1:
            content[result_pos] = val1 + val2
        elif opcode == 2:
            content[result_pos] = val1 * val2
        elif opcode == 99:
            return content


def part2(content):
    pass


def main():
    content = read_file(2, True)
    # Replace incorrect valeus from input
    content[1] = 12
    content[2] = 2
    p1_result = part1(content)[0]
    print("Part 1: {}".format(p1_result))


if __name__ == '__main__':
    main()
