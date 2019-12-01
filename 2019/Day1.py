#!/usr/bin/env python3
import os
import math

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content


def calculate(result, num):
    return result + math.floor((int(num)/3)) -2

def calculate_rescursive(result, payload):
    new_payload = math.floor((int(payload)/3)) -2
    if new_payload >= 0:
        result = result + new_payload
        return calculate_rescursive(result, new_payload)
    else:
        return result


def part1(content):
    result = 0
    for num in content:
        result = calculate(result, num)

    print(result)



def part2(content):
    total_result = 0
    for num in content:
        total_result = total_result + calculate_rescursive(0, num)
    print(total_result)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "input/day1.txt")
    content = read_file(filename)
    part1(content)
    part2(content)


if __name__ == '__main__':
    main()
