from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_lst = defaultdict(list)
        for x, y in edges:
            adj_lst[x].append(y)
            adj_lst[y].append(x)
        visited = set([0])
        
        def dfs(cur):
            counter = 0
            for neighbor in adj_lst[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res = dfs(neighbor)
                    if res != -1:
                        counter += 2
                        counter += res
            if hasApple[cur] or counter != 0:
                return counter
            else:
                return -1
        res = dfs(0)
        if res == -1:
            return 0
        else:
            return res

            

