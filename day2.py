#!/usr/bin/python

import fileinput

def sides(*dims):
    s = []
    for i, d in enumerate(dims):
        for dd in dims[i+1:]:
            s += [d * dd]
    return s

def box(sides):
    return 2 * sum(sides)

def slack(sides):
    return min(sides)

def package(*dims):
    s = sides(*dims)
    return box(s) + slack(s)

def part1(s):
    fl = [package(*c) for c in s]
    return sum(fl)

def bow(*dims):
    pr = 1
    for d in dims:
        pr *= d
    return pr

def perimeter(*dims):
    p = []
    for i, d in enumerate(dims):
        for dd in dims[i+1:]:
            p += [2 * (d+dd)]
    return p


def part2(s):
    rib = sum([min(perimeter(*c)) for c in s])
    bo = sum([bow(*c) for c in s])

    return rib + bo

def parse(line):
    return tuple([int(x) for x in line.split('x')])

if __name__ == '__main__':
    s = [parse(line) for line in fileinput.input()]
    print "Part 1: ", part1(s)
    print "Part 2: ", part2(s)
