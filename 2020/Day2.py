#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import re

def process_input(content):
    data = []
    for line in content:
        m = re.match("([0-9]+)-([0-9]+)\s([a-z])[:]\s([A-Za-z0-9]+)", line)
        first_digit = int(m.group(1))
        second_digit = int(m.group(2))
        letter = m.group(3)
        passw = m.group(4)
        data.append((first_digit, second_digit, letter, passw))
    return data

def is_valid_pass(lower_limit, upper_limit, letter, passw):
    count = passw.count(letter)
    if count >= lower_limit and count <= upper_limit:
        return True
    return False


def is_valid_pass2(idx_one, idx_two, letter, passw):
    fi = passw[idx_one-1]
    se = passw[idx_two-1]
    if (letter == fi and letter != se) or (letter != fi and letter == se):
        return True
    return False


def part1(data):
    result = 0
    for item in data:
        lower_limit = item[0]
        upper_limit = item[1]
        letter = item[2]
        passw = item[3]
        if is_valid_pass(lower_limit, upper_limit, letter, passw):
            result = result + 1

    advent.print_answer(1, result)

    return result


def part2(data):
    result = 0
    for item in data:
        idx_one = item[0]
        idx_two = item[1]
        letter = item[2]
        passw = item[3]
        if is_valid_pass2(idx_one, idx_two, letter, passw):
            result = result + 1

    advent.print_answer(1, result)

    return result


def main():
    advent.setup(2020,2)
    file = advent.read_file()
    data = process_input(helper.get_lines(file))
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
