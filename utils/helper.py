import re
from typing import TextIO

def get_lines(file : TextIO, rstrip=True, lstrip=True, as_tuple=False):
    '''Read file into a list (or tuple) of lines.'''
    kind = tuple if as_tuple else list
    lines = map(lambda l: l.rstrip('\n'), file)

    if rstrip and lstrip:
        return kind(map(str.strip, lines))
    if rstrip:
        return kind(map(str.rstrip, lines))
    if lstrip:
        return kind(map(str.lstrip, lines))
    return kind(lines)


def get_ints(file, use_regex=False, regex=r'-?\d+', as_tuple=False):
    '''Takes a file and return a list (or optionally tuple) of integers'''
    kind = tuple if as_tuple else list

    if use_regex:
        exp = re.compile(regex)
        return kind(map(int, exp.findall(file.read())))
    return kind(map(int, file.read().split()))
