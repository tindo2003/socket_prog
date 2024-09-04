from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N = len(heights)
        M = len(heights[0])
        pacific_visited = [[False] * M for _ in range(N)]
        atlantic_visited = [[False] * M for _ in range(N)]
        directions = [[0,1], [1,0],[0,-1],[-1,0]]
        q = deque([])
        res = set()
        for r in range(N):
            pacific_visited[r][0] = True 
            q.append((r, 0))
        for c in range(M):
            pacific_visited[0][c] = True 
            q.append((0, c))
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not pacific_visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    pacific_visited[nx][ny] = True 
                    q.append((nx, ny))
        q = deque([])
        for r in range(N):
            atlantic_visited[r][M-1] = True
            q.append((r, M-1))
        for c in range(M):
            atlantic_visited[N-1][c] = True
            q.append((N-1, c))
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not atlantic_visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    if pacific_visited[nx][ny]:
                        res.add((nx, ny))
                    atlantic_visited[nx][ny] = True 
                    q.append((nx, ny)) 
        for r in range(N):
            if atlantic_visited[r][M-1] and pacific_visited[r][M-1]:
                res.add((r, M-1))
            if atlantic_visited[r][0] and pacific_visited[r][0]: 
                res.add((r, 0))
        for c in range(M):
            if atlantic_visited[N-1][c] and pacific_visited[N-1][c]:
                res.add((N-1, c))
            if atlantic_visited[0][c] and pacific_visited[0][c]:
                res.add((0, c))
        return [list(item) for item in res]
                


