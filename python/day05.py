#!/usr/bin/python3

import fileinput
import re


def nice(s):

    re_bad = re.compile(r'ab|cd|pq|xy').findall
    re_vowels = re.compile(r'(.*[aeiou].*){3,}').findall
    re_double = re.compile(r'(.)\1{1,}').findall

    if not re_bad(s) and re_vowels(s) and re_double(s):
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
