from typing import List
from collections import defaultdict


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        q = []
        best = defaultdict(int)
        total_oranges = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] in [1, 2]:
                    if grid[r][c] == 2:
                        q.append((r, c))
                        best[(r, c)] = 0
                    total_oranges += 1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0
        while q:
            r, c = q.pop(0)
            res = max(res, best[(r, c)])
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < M
                    and grid[nr][nc] == 1
                    and (nr, nc) not in best
                ):
                    q.append((nr, nc))
                    best[(nr, nc)] = best[(r, c)] + 1
        if total_oranges != len(best):
            return -1
        return res
