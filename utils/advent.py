import os
from os.path import dirname, realpath
import csv
import sys


def log(s, *a):
    sys.stderr.write('[advent] ' + s.format(*a))
    sys.stderr.flush()


def setup(year: int, day: int):
    global YEAR
    global DAY

    if not (year >= 2015 and 1 <= day <= 25):
        log('ERROR: wrong year and/or day set!\n')
        sys.exit(1)

    YEAR = year
    DAY = day


def read_file(fname=None, mode='r'):

    if fname is not None:
        return open(fname, mode)

    filepath = realpath(__file__)

    dir_of_file = dirname(filepath)
    parent_dir_of_file = dirname(dir_of_file)

    filename = "{}/input/day{}.txt".format(YEAR, DAY)
    full_path = os.path.join(parent_dir_of_file, filename)
    file = open(full_path, mode)
    
    return file


def print_answer(part: int, answer):
    if part < 1 or part > 2:
        raise ValueError("Not a valid part")
    print('{}-D{}-P{}:'.format(YEAR, DAY, part), answer)

