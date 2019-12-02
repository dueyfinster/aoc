import os
import csv


def read_file(day_num, is_csv=False):
    dirname = os.path.dirname(__file__)
    filename = "input/day{}.txt".format(day_num)
    full_path = os.path.join(dirname, filename)
    with open(full_path) as f:
        if is_csv:
            content = list(csv.reader(f, delimiter=','))[0]
        else:
            content = f.readlines()
            content = [x.strip() for x in content]
    return content
