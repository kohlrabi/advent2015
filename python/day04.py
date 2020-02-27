#!/usr/bin/python

import fileinput
import md5
import math

def salt(s, n):
    return s + str(n)
    
def coin(s, n=5):
    for i in xrange(10000000000000):
        sa = md5.md5(salt(s, i)).hexdigest()
        if sa[0:n] == '0'*n:
            return i

def part1(s):
    return coin(s, 5)

def part2(s):
    return coin(s, 6)

if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()][0]
    print "Part 1: ", part1(s)
    print "Part 2: ", part2(s)
