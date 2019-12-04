#!/usr/bin/env python3
from ngu import read_file
from collections import Counter


def all_digits_increasing(nums):
    return nums == sorted(nums)


def repeated_nums_adjacent(nums):
    last_num = nums[0]
    for num in nums[1:]:
        if last_num == num:
            return True
        last_num = num
    return False


def more_than_two_adjacent(candidate):
    nums = [int(i) for i in str(candidate)]
    li = Counter(nums)

    # TODO: not working yet
    if 2 < max(li.values()) and 2 not in li.values():
        last_num = nums[0]
        streak = 0
        for i in range(1, len(nums)):
            if last_num == nums[i]:
                streak = streak + 1
            else:
                streak = 0
            last_num = nums[i]

            if streak >= 2:
                return True

    return False


def part1(start, end):
    candidates = []
    start_nums = [int(i) for i in str(start)]
    for number in range(start, end+1):
        nums = [int(i) for i in str(number)]
        if all_digits_increasing(nums):
            if repeated_nums_adjacent(nums):
                candidates.append(number)

    return len(candidates), candidates


def part2(candidates):
    new_cand = []
    for cand in candidates:
        if not more_than_two_adjacent(cand):
            new_cand.append(cand)

    return len(new_cand)


def main():
    content = read_file(4)[0].split('-')
    start, end = int(content[0]), int(content[1])
    p1_result, candidates = part1(start, end)
    print("Part 1: {}".format(p1_result))
    p2_result = part2(candidates)
    print("Part 2: {}".format(p2_result))


if __name__ == '__main__':
    main()
