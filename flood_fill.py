#!/usr/bin/env python3
"""Flood fill algorithm on ASCII art grids."""
import sys
from collections import deque

def flood_fill(grid, x, y, new_char, diagonal=False):
    rows, cols = len(grid), len(grid[0])
    old = grid[y][x]
    if old == new_char: return grid
    q = deque([(x, y)])
    visited = set()
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    if diagonal: dirs += [(1,1),(1,-1),(-1,1),(-1,-1)]
    count = 0
    while q:
        cx, cy = q.popleft()
        if (cx,cy) in visited: continue
        if not (0<=cx<cols and 0<=cy<rows): continue
        if grid[cy][cx] != old: continue
        visited.add((cx,cy))
        grid[cy][cx] = new_char
        count += 1
        for dx, dy in dirs: q.append((cx+dx, cy+dy))
    return grid, count

def parse_grid(text):
    return [list(line) for line in text.strip().split('\n')]

def show(grid):
    for row in grid: print(''.join(row))

if __name__ == '__main__':
    if '--demo' in sys.argv:
        grid = parse_grid("""
..........
.###..###.
.#....#.#.
.###..###.
......#...
.###..#...
..........
""".strip())
        print("Before:"); show(grid)
        grid, n = flood_fill(grid, 0, 0, '*')
        print(f"\nAfter fill(0,0,'*') — {n} cells:"); show(grid)
    elif len(sys.argv) >= 5:
        grid = parse_grid(sys.stdin.read())
        x, y, ch = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
        grid, n = flood_fill(grid, x, y, ch, '--diagonal' in sys.argv)
        show(grid)
        print(f"\n{n} cells filled", file=sys.stderr)
    else:
        print("Usage: flood_fill.py <x> <y> <char> [--diagonal] < grid.txt")
        print("       flood_fill.py --demo")
