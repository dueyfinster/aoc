#!/usr/bin/env python3
from ngu import read_file
import re


def manhattan_dist(pos):
    return abs(pos[0]) + abs(pos[1])


def convert_to_coords(positions, last_pos, pos_to_calculate, distance):
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
        distance = distance + 1

    return new_pos, distance


def calculate_positions(wire, distances):
    positions = set()
    start_pos = (0, 0)
    distance = 0
    for pos_to_calc in wire:
        curr_pos, distance = convert_to_coords(
            positions, start_pos, pos_to_calc, distance)
        start_pos = curr_pos
        distances[curr_pos] = distance

    return positions


def part1(wire1, wire2):
    w1_positions = calculate_positions(wire1, {})
    w2_positions = calculate_positions(wire2, {})
    crossings = w1_positions.intersection(w2_positions)
    man_distances = [manhattan_dist(pos) for pos in crossings]
    return min(man_distances)


def part2(wire1, wire2):
    lowest_cost_crossing = 0
    w1_distances = {}
    w1_positions = calculate_positions(wire1, w1_distances)
    w2_distances = {}
    w2_positions = calculate_positions(wire2, w2_distances)
    crossings = w1_positions.intersection(w2_positions)

    crossed_dist = {}

    for crossing in crossings:
        # TODO
        print(w1_distances[crossing])

    return lowest_cost_crossing


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
