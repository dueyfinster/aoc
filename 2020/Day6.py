#!/usr/bin/env python3
from ngu import read_file


def process_input(content):
    answers = []
    answer = ""

    for i, line in enumerate(content):
        if line != '':
            answer = answer + ' ' + line

        if line == '' or i == (len(content)-1):
            answers.append(answer.strip())
            answer = ""

    return answers


def part1(data):
    pass
    #print("Part 1: {}".format(str(result)))


def part2(data):
    pass
    #print("Part 2: {}".format(str(result)))


def main():
    content = read_file(6)
    data = process_input(content)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
