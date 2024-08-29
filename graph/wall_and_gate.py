from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        N = len(rooms)
        M = len(rooms[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        best = {}
        q = deque([])
        for r in range(N):
            for c in range(M):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    best[(r, c)] = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 
                    if (nx, ny) in best: continue 
                    if 0 <= nx < N and 0 <= ny < M and rooms[nx][ny] != 1:
                        best[(nx, ny)] = best[(x, y)] + 1
                        q.append((nx, ny))
        
        for (x, y), dist in best.items():
            rooms[x][y] = dist 

        