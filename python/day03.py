#!/usr/bin/python3

import fileinput

def move(c):
    d = {'^': 0+1j, '>': 1+0j, '<': -1+0j, 'v': 0-1j}
    return d[c]

def houses(s):
    h = [0 + 0j]
    u = {0 + 0j}
    for ss in s:
        new = h[-1] + move(ss)
        h.append(new)
        u.add(new)
    return h, u

def part1(s):
    h, u = houses(s)
    return len(u)

def part2(s):
    h, u = houses(s[0::2])
    h2, u2 = houses(s[1::2])
    for uu in u2:
        if not uu in u:
            u.add(uu)
    return len(u)

if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()][0]
    print("Part 1:", part1(s))
    print("Part 2:", part2(s))
