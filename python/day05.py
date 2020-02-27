#!/usr/bin/python3

import fileinput

def nice(s):
    vowels = 'aeiou'
    bad = {'ab', 'cd', 'pq', 'xy'}

    for b in bad:
        if b in s:
            return False

    vows = 0
    for v in vowels:
        vows += s.count(v)
    if vows < 3:
        return False

    for i in range(97,123,1):
        if chr(i)*2 in s:
            return True
            
    return False

def part1(s):
    ni = [l for l in s if nice(l)]
    return len(ni)

if __name__ == '__main__':
    s = [line.strip() for line in fileinput.input()]
    print("Part 1:", part1(s))
    #print "Part 2: ", part2(s)
