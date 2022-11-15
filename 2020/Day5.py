#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import math


def process_input(content):
    data = []
    for line in content:
        data.append([char for char in line])
    return data


def seat_range(idx, letter, rang):
    lower, upper = rang
    bound = upper-lower
    complete = False

    if letter == 'L':
        mid = math.floor((bound/2))
        new_rang = (lower, mid+lower)
    elif letter == 'R':
        mid = round((bound/2))
        new_rang = (lower+mid, upper)

    if idx == 2 and letter == 'L':
        new_rang = (lower, lower)
        complete = True
    elif idx == 2 and letter == 'R':
        new_rang = (upper, upper)
        complete = True

    return complete, new_rang


def row_range(idx, letter, rang):
    lower, upper = rang
    bound = upper-lower
    complete = False

    if letter == 'F':
        mid = math.floor((bound/2))
        new_rang = (lower, mid+lower)
    elif letter == 'B':
        mid = round((bound/2))
        new_rang = (lower+mid, upper)

    if idx == 6 and letter == 'F':
        new_rang = (lower, lower)
        complete = True
    elif idx == 6 and letter == 'B':
        new_rang = (upper, upper)
        complete = True

    return complete, new_rang


def part1(data):
    seats = []

    for i, line in enumerate(data):
        r_range = (0, 127)
        for y, char in enumerate(line):
            finished, r_range = row_range(y, char, r_range)
            if finished:
                break
        s_range = (0, 7)
        for x, char in enumerate(line[-3:]):
            complete, s_range = seat_range(x, char, s_range)
            if complete:
                seat_id = (r_range[0] * 8) + s_range[0]
                seats.append(
                    {'line': i, 'row': r_range[0], 'seat': s_range[0], 'seat_id': seat_id})
                break
    seat_ids = [seat['seat_id'] for seat in seats]
    result = max(seat_ids)

    advent.print_answer(1, result)
    return seat_ids


def part2(seat_ids):
    full_seat_li = set(range(min(seat_ids), max(seat_ids)))
    seat_ids = set(seat_ids)

    diff = full_seat_li.symmetric_difference(seat_ids)

    result = 0
    for num in diff:
        if num-1 in seat_ids and num+1 in seat_ids:
            result = num

    advent.print_answer(2, result)
    return result


def main():
    advent.setup(2020,5)
    file = advent.read_file()
    content = helper.get_lines(file)
    data = process_input(content)
    seat_ids = part1(data)
    part2(seat_ids)


if __name__ == '__main__':
    main()
