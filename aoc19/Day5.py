#!/usr/bin/env python3
from ngu import read_file


def part1(content):
    for i in range(0, len(content), 4):
        opcode = content[i]
        pos1 = content[i+1]
        pos2 = content[i+2]
        result_pos = content[i+3]
        val1 = content[pos1]
        val2 = content[pos2]

        # TODO
        if opcode == 1:
            content[result_pos] = val1 + val2
        elif opcode == 2:
            content[result_pos] = val1 * val2
        elif opcode == 3:
            pass
        elif opcode == 4:
            pass
        elif opcode == 99:
            return content

    return 0


def part2(content):
    return 0


def main():
    content = read_file(5)[0].split(",")

    p1_content = [int(x) for x in content]
    p1_result = part1(p1_content)
    p2_content = p1_content.copy()

    print("Part 1: {}".format(p1_result))
    p2_result = part2(content)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
