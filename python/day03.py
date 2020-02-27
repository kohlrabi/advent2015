#!/usr/bin/python3

import fileinput

def move(c):
    d = {'^': 0+1j, '>': 1+0j, '<': -1+0j, 'v': 0-1j}
    return d[c]

def houses(s):
    last = 0 + 0j
    u = {0 + 0j}
    for ss in s:
        last += move(ss)
        u.add(last)
    return u

def part1(s):
    u = houses(s)
    return len(u)

def part2(s):
    u = houses(s[0::2])
    u2 = houses(s[1::2])
    un = u.union(u2)
    return len(un)

if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()][0]
    print("Part 1:", part1(s))
    print("Part 2:", part2(s))
