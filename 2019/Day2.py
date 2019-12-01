#!/usr/bin/env python3
import os

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    #content = [int(x.strip()) for x in content]
    return content


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "input/day2.txt")
    content = read_file(filename)


if __name__ == '__main__':
    main()
