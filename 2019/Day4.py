#!/usr/bin/env python3
from ngu import read_file
from collections import Counter


def all_digits_increasing(nums):
    if nums != sorted(nums):
        return False

    return True


def repeated_nums_adjacent(nums):
    last_num = nums[0]
    for num in nums[1:]:
        if last_num == num:
            return True
        last_num = num
    return False


def part1(start, end):
    candidates = []
    start_nums = [int(i) for i in str(start)]
    for number in range(start, end+1):
        nums = [int(i) for i in str(number)]
        if all_digits_increasing(nums):
            if repeated_nums_adjacent(nums):
                candidates.append(number)

    return len(candidates)


def part2(start, end):
    pass


def main():
    content = read_file(4)[0].split('-')
    start, end = int(content[0]), int(content[1])
    p1_result = part1(start, end)
    print("Part 1: {}".format(p1_result))
    p2_result = part2(start, end)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
