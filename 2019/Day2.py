#!/usr/bin/env python3
from utils import advent
advent.setup(2019, 2)

def part1(content, noun=12, verb=2):
    content[1] = noun
    content[2] = verb

    for i in range(0, len(content), 4):
        opcode = content[i]
        pos1 = content[i+1]
        pos2 = content[i+2]
        result_pos = content[i+3]
        val1 = content[pos1]
        val2 = content[pos2]

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
            result = part1(content, i, x)[0]

            if result == answer_sought:
                print("Part 2 verb: {} noun: {}".format(i, x))
                return 100 * i + x


def main():
    content = advent.read_file()[0].split(",")
    p1_content = [int(x) for x in content]
    p2_content = p1_content.copy()

    p1_result = part1(p1_content)[0]
    advent.print_answer(1, p1_result)
    p2_result = part2(p2_content)
    advent.print_answer(2, p2_result)


if __name__ == '__main__':
    main()
