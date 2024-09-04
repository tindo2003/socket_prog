from typing import List 
from collections import defaultdict
class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def max_killed_enemies(self, grid: List[List[str]]) -> int:
        # write your code here
        if not grid: return 0
        N = len(grid)
        M = len(grid[0])
        res = 0
        col_hits = [0] * M 
        row_hits = 0
        for r in range(N):
            for c in range(M):
                if c == 0 or grid[r][c-1] == "W":
                    row_hits = 0
                    for k in range(c, M):
                        if grid[r][k] == "W":
                            break 
                        elif grid[r][k] == "E":
                            row_hits += 1
                if r == 0 or grid[r-1][c] == "W":
                    col_hits[c] = 0 
                    for k in range(r, N):
                        if grid[k][c] == "W":
                            break 
                        elif grid[k][c] == "E":
                            col_hits[c] += 1
                if grid[r][c] == '0':
                    res = max(res, row_hits + col_hits[c])
        return res
                
