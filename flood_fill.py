#!/usr/bin/env python3
"""Flood Fill - Fill connected regions in 2D grids (BFS and DFS variants)."""
import sys
from collections import deque

def flood_fill_bfs(grid, r, c, new_color):
    rows, cols = len(grid), len(grid[0]); old = grid[r][c]
    if old == new_color: return grid
    queue = deque([(r, c)]); grid[r][c] = new_color
    while queue:
        cr, cc = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==old:
                grid[nr][nc] = new_color; queue.append((nr, nc))
    return grid

def count_regions(grid):
    rows, cols = len(grid), len(grid[0]); visited = set(); regions = {}
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in visited:
                color = grid[r][c]; count = 0
                queue = deque([(r,c)]); visited.add((r,c))
                while queue:
                    cr, cc = queue.popleft(); count += 1
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = cr+dr, cc+dc
                        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]==color:
                            visited.add((nr,nc)); queue.append((nr,nc))
                regions.setdefault(color, []).append(count)
    return regions

def display(grid):
    for row in grid: print("  " + " ".join(str(c) for c in row))

def main():
    grid = [[1,1,1,0,0],[1,1,0,0,2],[1,0,0,2,2],[0,0,3,3,3],[0,3,3,3,0]]
    print("=== Flood Fill ===\n\nOriginal:"); display(grid)
    regions = count_regions([row[:] for row in grid])
    print(f"\nRegions: {sum(len(v) for v in regions.values())}")
    for color, sizes in sorted(regions.items()):
        print(f"  Color {color}: {len(sizes)} region(s), sizes={sizes}")
    grid = flood_fill_bfs(grid, 0, 0, 9)
    print("\nAfter fill(0,0) with 9:"); display(grid)

if __name__ == "__main__":
    main()
