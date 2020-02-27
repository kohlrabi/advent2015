#!/usr/bin/python3

import fileinput
import re

gridsize = 1000


def apply_command(line, grid):
    m = re.match(
        r'([a-z ]+)([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', line)
    cmd, *corners = m.groups()
    corners = list(map(int, corners))

    cmd = cmd.rstrip()

    op = {'turn on': lambda x: True, 'turn off': lambda x: False,
          'toggle': lambda x: x ^ True}[cmd]

    for i in range(corners[0], corners[2]+1):
        for j in range(corners[1], corners[3]+1):
            grid[i][j] = op(grid[i][j])


def part1(s):
    grid = [[False for _ in range(gridsize)] for __ in range(gridsize)]
    for line in s:
        apply_command(line, grid)
    return sum(x for row in grid for x in row)


if __name__ == '__main__':
    s = [line.rstrip() for line in fileinput.input()]
    print("Part 1:", part1(s))
    #print("Part 2:", part2(s))
