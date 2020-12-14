#!/usr/bin/env python3
from ngu import read_file
MANDATORY_FIELDS = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", "cid"}


def valid_birth_year(passport):
    if 1920 >= passport['byr'] <= 2002:
        return True
    return False


def valid_issue_year(passport):
    if 2010 >= passport['iyr'] <= 2020:
        return True
    return False


def valid_expr_year(passport):
    if 2020 >= passport['eyr'] <= 2030:
        return True
    return False


def valid_passport1(passport):
    fields_missing = set(
        passport.keys()).symmetric_difference(MANDATORY_FIELDS)

    if "cid" in fields_missing and len(fields_missing) == 1:
        return True

    if len(fields_missing) == 0:
        return True

    return False


def process_input(content):
    passports = []
    prev = 0
    passport = ""

    for i, line in enumerate(content):
        if line != '':
            passport = passport + ' ' + line

        if line == '' or i == (len(content)-1):
            d = dict(item.split(":") for item in passport.strip().split(" "))
            passports.append(d)
            passport = ""

    return passports


def part1(data):
    result = 0
    for passport in data:
        if valid_passport1(passport):
            result = result + 1
    print("Part 1: {}".format(str(result)))


def part2(data):
    pass
    # print("Part 2: {}".format(str(result)))


def main():
    content = read_file(4)
    data = process_input(content)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
