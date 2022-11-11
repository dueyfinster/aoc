#!/usr/bin/env python3
import os
import math
from utils import advent, helper


advent.setup(2019, 1)

def calculate(result, num):
    return result + math.floor((int(num)/3)) - 2


def calculate_rescursive(result, payload):
    new_payload = math.floor((int(payload)/3)) - 2
    if new_payload >= 0:
        result = result + new_payload
        return calculate_rescursive(result, new_payload)
    else:
        return result


def part1(content):
    result = 0
    for num in content:
        result = calculate(result, num)

    advent.print_answer(1, result)
    return result


def part2(content):
    total_result = 0
    for num in content:
        total_result = total_result + calculate_rescursive(0, num)
    advent.print_answer(1, total_result)
    return total_result


def main():
    file = advent.read_file()
    content = helper.get_lines(file)
    part1(content)
    part2(content)


if __name__ == '__main__':
    main()
