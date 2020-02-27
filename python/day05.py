#!/usr/bin/python3

import fileinput
import re


def nice(s):

    re_bad = re.compile(r'ab|cd|pq|xy')
    re_vowels = re.compile(r'[aeiou]')
    re_double = re.compile(r'(.)\1{1,}')

    if re_bad.findall(s):
        return False
    nvowels = len(re_vowels.findall(s))
    if nvowels < 3:
        return False
    if re_double.findall(s):
        return True

    return False


def part1(s):
    ni = [l for l in s if nice(l)]
    return len(ni)


if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()]
    print("Part 1:", part1(s))
    # print "Part 2: ", part2(s)
    # print "Part 2: ", part2(s)
