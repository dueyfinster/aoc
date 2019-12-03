#!/usr/bin/env python3
from ngu import read_file
import re


def manhattan_dist(pos):
    return abs(pos[0]) + abs(pos[1])


def convert_to_coords(positions, last_pos, pos_to_calculate):
    movement = int(re.sub("R|L|U|D", "", pos_to_calculate))
    x, y = last_pos
    for _ in range(0, abs(movement)):
        if 'R' in pos_to_calculate:
            # Calculate positively along X axis
            x = x + 1
        elif 'L' in pos_to_calculate:
            # Calculate negatively along X axis
            x = x - 1
        elif 'U' in pos_to_calculate:
            # Calculate positively along Y axis
            y = y + 1
        elif 'D' in pos_to_calculate:
            # Calculate negatively along Y axis
            y = y - 1
        new_pos = (x, y)
        positions.add(new_pos)

    return new_pos


def part1(wire1, wire2):
    w1_positions = set()
    w1_start_pos = (0, 0)
    for pos_to_calc in wire1:
        curr_pos = convert_to_coords(w1_positions, w1_start_pos, pos_to_calc)
        w1_start_pos = curr_pos

    w2_positions = set()
    w2_start_pos = (0, 0)
    for pos_to_calc in wire2:
        curr_pos = convert_to_coords(w2_positions, w2_start_pos, pos_to_calc)
        w2_positions.add(curr_pos)
        w2_start_pos = curr_pos

    crossings = w1_positions.intersection(w2_positions)
    man_distances = [manhattan_dist(pos) for pos in crossings]
    print(man_distances)
    return min(man_distances)


def part2(wire1, wire2):
    pass


def main():
    content = read_file(3)
    wire1 = content[0].split(",")
    wire2 = content[1].split(",")

    p1_result = part1(wire1, wire2)
    print("Part 1: {}".format(p1_result))
    p2_result = part2(wire1, wire2)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
