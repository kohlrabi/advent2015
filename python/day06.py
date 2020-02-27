#!/usr/bin/python3

import fileinput
import re

gridsize = 1000


def apply_command(line, grid, mode=1):
    m = re.match(
        r'([a-z ]+)([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', line)
    cmd, *corners = m.groups()
    corners = list(map(int, corners))

    cmd = cmd.rstrip()

    if mode == 1:
        op = {'turn on': lambda x: True, 'turn off': lambda x: False,
              'toggle': lambda x: x ^ True}[cmd]
    else:
        op = {'turn on': lambda x: x+1, 'turn off': lambda x: max(x-1, 0),
              'toggle': lambda x: x+2}[cmd]

    for i in range(corners[0], corners[2]+1):
        for j in range(corners[1], corners[3]+1):
            grid[i][j] = op(grid[i][j])


def part1(s):
    grid = [[False for _ in range(gridsize)] for __ in range(gridsize)]
    for line in s:
        apply_command(line, grid, mode=1)
    return sum(x for row in grid for x in row)


def part2(s):
    grid = [[0 for _ in range(gridsize)] for __ in range(gridsize)]
    for line in s:
        apply_command(line, grid, mode=2)
    return sum(x for row in grid for x in row)


if __name__ == '__main__':
    s = [line.rstrip() for line in fileinput.input()]
    print("Part 1:", part1(s))
    print("Part 2:", part2(s))
