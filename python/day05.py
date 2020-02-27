#!/usr/bin/python3

import fileinput
import re


def nice(s):

    re_bad = re.findall(r'ab|cd|pq|xy', s)
    if re_bad:
        return False
    re_vowels = re.findall(r'(.*[aeiou].*){3,}', s)
    if not re_vowels:
        return False
    re_double = re.findall(r'(.)\1', s)
    if re_double:
        return True
    return False


def nice2(s):
    re_twice = re.findall(r'(..).*\1', s)
    re_repeats = re.findall(r'(.).\1', s)

    if re_twice and re_repeats:
        return True
    return False


def part1(s):
    ni = [True for l in s if nice(l)]
    return len(ni)


def part2(s):
    ni = [True for l in s if nice2(l)]
    return len(ni)


if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()]
    print("Part 1:", part1(s))
    print("Part 2:", part2(s))
