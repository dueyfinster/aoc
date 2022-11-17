#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper

def part1(lines):
    result = 0

    for l in lines:
        s = l.replace('\n', '')
        result += len(set(s))

    advent.print_answer(1, result)
    return result


def part2(lines):

    result = 0

    lines = list(map(lambda l : l.split('\n'), lines))

    for l in lines:
        alls = set.intersection(*list(map(set, l)))
        result += len(alls)
    

    advent.print_answer(2, result)
    return result


def main():
    advent.setup(2020, 6)
    file = advent.read_file()
    lines = helper.get_sections(file)

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
