#!/usr/bin/env python3
import os
import re
from ngu import read_file
from pprint import pprint

def process_input(content):
    data = []
    for line in content:
        data.append([char for char in line])
    return data


def part1(data):
    pass
    # print("Part 1: {}".format(str(result)))


def part2(data):
    pass
    #print("Part 2: {}".format(str(result)))


def main():
    content = read_file(3)
    data = process_input(content)
    pprint(data)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
