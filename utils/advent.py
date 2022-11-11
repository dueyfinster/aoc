import os
from os.path import dirname, realpath
import csv
import sys

def log(s, *a):
	sys.stderr.write('[advent] ' + s.format(*a))
	sys.stderr.flush()

def setup(year, day):
	global YEAR
	global DAY
	global SESSION

	if not (year >= 2015 and 1 <= day <= 25):
		log('ERROR: wrong year and/or day set!\n')
		sys.exit(1)

	YEAR = year
	DAY  = day

def read_file():
    filepath = realpath(__file__)

    dir_of_file = dirname(filepath)
    parent_dir_of_file = dirname(dir_of_file)

    filename = "{}/input/day{}.txt".format(YEAR, DAY)
    full_path = os.path.join(parent_dir_of_file, filename)
    with open(full_path) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content

def print_answer(part, answer):
	print('{} Day {} Part {}:'.format(YEAR, DAY, part), answer)