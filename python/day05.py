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
    re_double = re.findall(r'(.)\1{1,}', s)
    if re_double:
        return True
    return False


def part1(s):
    ni = [l for l in s if nice(l)]
    return len(ni)


if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()]
    print("Part 1:", part1(s))
