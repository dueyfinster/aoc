#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import re
from itertools import cycle

def part1(data):
    result = None
    regex = re.compile('(?!bag|bags|contain)(?<![a-zA-Z])[0-9a-zA-Z]+')

    li = list(map(lambda s: regex.findall(s), data))

    main_keys = ['adj', 'col']
    sub_keys = ['no', 'adj', 'col']
    nli = []

    for values in iter(li):
       d = dict(zip(main_keys, values[0:2]))
       d['con'] = tuple(zip(cycle(sub_keys), values[2:]))
       nli.append(d)

    advent.print_answer(1, result)
    return result


def part2(data):
    result = None
    advent.print_answer(2, result)
    return result


def main():
    advent.setup(2020,7)
    file = advent.read_file()
    lines = helper.get_lines(file)
    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
