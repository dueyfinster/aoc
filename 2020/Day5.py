#!/usr/bin/env python3
from ngu import read_file
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
    print("Part 1: {}".format(str(result)))


def part2(data):
    pass
    # print("Part 2: {}".format(str(result)))


def main():
    content = read_file(5)
    data = process_input(content)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
