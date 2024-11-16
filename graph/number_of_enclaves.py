from typing import List 
from collections import defaultdict, deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        q = deque([])
        visited = defaultdict(bool)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        N, M = len(grid), len(grid[0])
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    if r == 0 or r == N - 1 or c == 0 or c == M - 1:
                        q.append((r, c))
                    else:
                        visited[(r, c)] = False

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, dy + y
                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and grid[nx][ny] == 1
                    and not visited[(nx, ny)]
                ):

                    q.append((nx, ny))
                    visited[(nx, ny)] = True

        res = 0
        for node, visited in visited.items():
            if not visited:
                res += 1
        return res
