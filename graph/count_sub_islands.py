from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        N = len(grid1)
        M = len(grid1[0])
        visited = [[False for _ in range(M)] for _ in range(N)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        good = False
        res = 0 

        def dfs(r, c):
            if grid2[r][c] == 1 and grid1[r][c] == 0:
                nonlocal good 
                good = False 
            for dr, dc in direction:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < N and 0 <= nc < M and grid2[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True 
                    dfs(nr, nc)

        # the gist is to go through the island in grid2. if while iterating, u encountering a cell in grid2 that is not land in grid1, then not a subisland
        for r in range(N):
            for c in range(M):
                if not visited[r][c] and grid2[r][c] == 1:
                    good = True 
                    visited[r][c] = True
                    dfs(r, c)
                    if good:
                        res += 1

        
        return res 