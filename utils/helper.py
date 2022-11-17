__all__ = ['log']

import re
import sys
from typing import TextIO


def log(s, *a):
    '''Log to standard error after formatting it with any additionally provided argument.'''
    sys.stderr.write(s.format(*a))
    sys.stderr.flush()


def eprint(*a, **kwa):
    '''Wrapper for print() that prints on standard error.'''
    print(*a, **kwa, file=sys.stderr)


def dump_iterable(iterable, fmt='{:d}: {!r}'):
	'''Dump index and values of an iterable using the specified format string to
	standard error.
	'''
	for i, item in enumerate(iterable):
		log(fmt + '\n', i, item)


def dump_dict(dct, fmt='{}: {!r}'):
	'''Dump keys and values of a dictionary using the specified format string to
	standard error.
	'''
	for k, v in dct.items():
		log(fmt + '\n', k, v)


def get_sections(file: TextIO, sep='\n\n', replace=False, rep_regexp=r'\n', rep_sub='', as_tuple=False):
    '''Get sections of a file split by separator. Default separator is '\n\n'''
    kind = tuple if as_tuple else list

    if replace:
        exp = re.compile(rep_regexp)
        sections = file.read().split(sep)
        return kind(map(lambda s : re.sub(exp, rep_sub, s), sections))
    return file.read().split(sep)

def get_lines(file: TextIO, rstrip=True, lstrip=True, as_tuple=False):
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


def get_char_matrix(file: TextIO, rstrip=True, lstrip=True, as_tuples=False):
    '''Read file into a matrix of characters.
    Strips lines on both ends by default unless rstrip=False or lstrip=False.
    Returns a list of list by default, or a tuple of tuple if as_tuples=True.
    '''
    kind = tuple if as_tuples else list
    lines = map(lambda l: l.rstrip('\n'), file)

    if rstrip and lstrip:
        return kind(kind(l.strip()) for l in lines)
    if rstrip:
        return kind(kind(l.rstrip()) for l in lines)
    if lstrip:
        return kind(kind(l.lstrip()) for l in lines)
    return kind(map(kind, lines))


def get_ints(file: TextIO, use_regex=False, regex=r'-?\d+', as_tuple=False):
    '''Takes a file and return a list (or optionally tuple) of integers'''
    kind = tuple if as_tuple else list

    if use_regex:
        exp = re.compile(regex)
        return kind(map(int, exp.findall(file.read())))
    return kind(map(int, file.read().split()))


def get_int_matrix(file: TextIO, use_regexp=False, regexp=r'-?\d+', as_tuples=False):
    '''Parse file containing lines of whitespace delimited decimal integers into
    a matrix of integers, one line = one row.
    If use_regexp=True, uses regexp to parse each line to extract integers.
    Returns a list of list by default, or a tuple of tuple if as_tuples=True.
    '''
    kind = tuple if as_tuples else list

    if use_regexp:
        exp = re.compile(regexp)
        return kind(kind(map(int, exp.findall(l))) for l in file)
    return kind(kind(map(int, l.split())) for l in file)


def get_dict_values(file: TextIO, regexp=r'([\w]+)[\W]([#\w]+)', as_tuple: bool = False):
    '''Parse file containing lines of key/value pairs in to a dictionary.
    Key is regexp match group 1 and Value is regexp match group 2.
    Returns a list of dict by default, or a tuple of dict if as_tuple=True.
    '''
    kind = tuple if as_tuple else list

    exp = re.compile(regexp)
    return kind(dict(map(tuple, exp.findall(l))) for l in file)

