#!/usr/bin/env python3
from ngu import read_file
import re


def manhattan_dist(pos):
    return abs(pos[0]) + abs(pos[1])


def convert_to_coords(positions, last_pos, pos_to_calculate, distance, crossings, distances):
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
        if new_pos in crossings:
            distances[new_pos] = distance

    return new_pos, distance


def calculate_positions(wire, crossings):
    positions = set()
    start_pos = (0, 0)
    distances = dict()
    distance = 0
    for pos_to_calc in wire:
        curr_pos, distance = convert_to_coords(
            positions, start_pos, pos_to_calc, distance, crossings, distances)
        start_pos = curr_pos

    return positions, distances


def part1(wire1, wire2):
    w1_positions, _ = calculate_positions(wire1, {})
    w2_positions, _ = calculate_positions(wire2, {})
    crossings = w1_positions.intersection(w2_positions)
    man_distances = [manhattan_dist(pos) for pos in crossings]
    return min(man_distances), crossings


def part2(wire1, wire2, crossings):
    lowest_cost_crossing = 0
    w1_positions, w1_distances = calculate_positions(wire1, crossings)
    w2_positions, w2_distances = calculate_positions(wire2, crossings)

    distances = [w1_distances[pos] + w2_distances[pos] for pos in crossings]
    lowest_cost_crossing = min(distances)

    return lowest_cost_crossing


def main():
    content = read_file(3)
    wire1 = content[0].split(",")
    wire2 = content[1].split(",")

    p1_result, crossings = part1(wire1, wire2)
    print("Part 1: {}".format(p1_result))
    p2_result = part2(wire1, wire2, crossings)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
