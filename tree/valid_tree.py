from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected and acyclic
        # 0 = unvisited
        # 1 = visited but not finished
        # 2 = done visited
        colored = [0] * n
        adj_lst = defaultdict(list)
        for x, y in edges:
            # detect self-loop
            if x == y: return False
            adj_lst[x].append(y)
            adj_lst[y].append(x)
        # detect cycles
        def dfs(cur, parent):
            for neighbor in adj_lst[cur]:
                if neighbor != parent:
                    if colored[neighbor] == 0:
                        colored[neighbor] = 1
                        if not dfs(neighbor, cur): 
                            return False
                    elif colored[neighbor] == 1:
                        return False 
            colored[cur] = 2
            return True

        if not dfs(0, -1): 
            return False
        
        # detect connected or not
        for item in colored: 
            if item != 2: return False
        return True