from typing import List 
from collections import defaultdict
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        adj_lst = defaultdict(list)

        for r in range(N):
            prev_seen = None
            for c in range(M):
                if grid[r][c] == 1:
                    if prev_seen:
                        adj_lst[(r, c)].append(prev_seen)
                        adj_lst[prev_seen].append((r, c))
                    prev_seen = (r, c) 
        
        for c in range(M):
            prev_seen = None
            for r in range(N):
                if grid[r][c] == 1:
                    if prev_seen:
                        adj_lst[(r, c)].append(prev_seen)
                        adj_lst[prev_seen].append((r, c))
                    prev_seen = (r, c) 
        

        def dfs(x, y, lst):
            for nx, ny in adj_lst[(x, y)]:
                if (nx, ny) not in self.visited:
                    self.visited.add((nx, ny))
                    lst.append((nx, ny))
                    dfs(nx, ny, lst)
        
        res = 0
        self.visited = set()

        for x, y in adj_lst.keys():
            
            if (x, y) not in self.visited:
                self.visited.add((x, y))
                lst = [(x, y)]
                dfs(x, y, lst)
                if len(lst) > 1: res += len(lst)
            
        return res
