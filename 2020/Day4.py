#!/usr/bin/env python3
from ngu import read_file
import re
MANDATORY_FIELDS = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", "cid"}


def valid_birth_year(passport):
    if re.match("\d{4}", passport['byr']):
        if 1920 <= int(passport['byr']) <= 2002:
            return True
    return False


def valid_issue_year(passport):
    if re.match("\d{4}", passport['iyr']):
        if 2010 <= int(passport['iyr']) <= 2020:
            return True
    return False


def valid_expr_year(passport):
    if re.match("\d{4}", passport['eyr']):
        if 2020 <= int(passport['eyr']) <= 2030:
            return True
    return False


def valid_height(passport):
    if re.match("(\d{2,3})([ci][mn])", passport['hgt']):
        m = re.match("(\d{2,3})([ci][mn])", passport['hgt'])
        num = int(m.group(1))
        unit = m.group(2)

        if unit == 'cm' and 150 <= num <= 193:
            return True
        elif unit == 'in' and 59 <= num <= 76:
            return True

    return False


def valid_hair_color(passport):
    if re.match("[#]{1}[0-9a-f]{6}", passport['hcl']):
        return True
    return False


def valid_eye_color(passport):
    valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    if passport['ecl'] in valid_colors:
        return True

    return False


def valid_pass_no(passport):
    if re.match("^\d{9}$", passport['pid']):
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


def valid_passport2(passport):
    return all([valid_birth_year(passport),
                valid_issue_year(passport),
                valid_expr_year(passport),
                valid_height(passport),
                valid_hair_color(passport),
                valid_eye_color(passport),
                valid_pass_no(passport)])


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
    valid_passports = []
    for passport in data:
        if valid_passport1(passport):
            valid_passports.append(passport)
            result += 1
    print("Part 1: {}".format(str(result)))
    return valid_passports


def part2(passports):
    result = 0
    for passport in passports:
        if valid_passport2(passport):
            result += 1
    print("Part 2: {}".format(str(result)))


def main():
    content = read_file(4)
    data = process_input(content)
    valid_passports = part1(data)
    part2(valid_passports)


if __name__ == '__main__':
    main()
