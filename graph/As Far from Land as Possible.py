from typing import List
from collections import deque, defaultdict


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque([])
        best = defaultdict(int)
        N, M = len(grid), len(grid[0])
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    q.append((r, c))
                    best[(r, c)] = 0
        if len(q) == 0:
            return -1
        if len(q) == N * M:
            return -1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < M
                    and (nr, nc) not in best
                    and grid[nr][nc] == 0
                ):
                    best[(nr, nc)] = best[(r, c)] + 1
                    res = max(res, best[(nr, nc)])
                    q.append((nr, nc))
        return res
