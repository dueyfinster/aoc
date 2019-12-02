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


def part2(orig_content):
    answer_sought = 19690720
    for i in range(12, 99):
        for x in range(2, 99):
            content = orig_content.copy()
            content[1] = i
            content[2] = x
            result = part1(content)[0]

            if result == answer_sought:
                print("Part 2 verb: {} noun: {}".format(i, x))
                return 100 * i + x


def main():
    p1_content = read_file(2, True)
    p2_content = p1_content.copy()

    p1_content[1] = 12
    p1_content[2] = 2

    # Replace incorrect valeus from input
    p1_result = part1(p1_content)[0]
    print("Part 1: {}".format(p1_result))
    p2_result = part2(p2_content)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
