"""
Problem: Number of Islands
Pattern: DFS / BFS (Graph Traversal)
Difficulty: Medium

Description:
Given an m × n 2D grid `grid` where each cell is either '1' (land) or '0' (water),
return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

Constraints:
- m == len(grid)
- n == len(grid[i])
- 1 ≤ m, n ≤ 300
- grid[i][j] is '0' or '1'

Return:
An integer representing the number of islands.

Examples:
Input:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3
"""
def number_of_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0]) 
    visited = set()
    islands = 0

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands
