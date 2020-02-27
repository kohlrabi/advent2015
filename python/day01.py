#!/usr/bin/python3

import fileinput

def up_or_down(c):
    if c is '(':
        return 1
    elif c is ')': 
        return -1
    else:
        return 0

def part1(s):
    fl = [up_or_down(c) for c in s]
    return sum(fl)

def part2(s):
    fl = 0
    for i, c in enumerate(s):
        if fl == -1:
            return i
        fl += up_or_down(c)

if __name__ == '__main__':
    s = [line for line in fileinput.input()][0]
    print("Part 1:", part1(s))
    print("Part 2:", part2(s))
