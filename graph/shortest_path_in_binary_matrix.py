from typing import List 
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0: return -1
        directions = [[0, 1], [1, 0], [0,-1], [-1, 0], [1, 1], [-1,-1], [1, -1], [-1,1]]
        N = len(grid)
        M = len(grid[0])
        #visited = [[False] * M for _ in range(N)]
        best = {(0,0): 1}
        q = deque([(0,0)])
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in best and grid[nx][ny] != 1:
                    best[(nx, ny)] = best[(x, y)] + 1
                    q.append((nx, ny))
        print(best)
        if (N-1, M-1) not in best:
            return -1
        else:
            return best[(N-1, M-1)]

        