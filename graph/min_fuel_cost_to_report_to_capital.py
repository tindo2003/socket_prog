from typing import List 
from collections import defaultdict
import math 

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # roads represents a tree
        adj_lst = defaultdict(list)
        for edge in roads:
            x, y = edge 
            adj_lst[x].append(y)
            adj_lst[y].append(x)
        res = 0
        visited = [False] * (len(adj_lst) + 1)
        def dfs(cur):
            nonlocal res
            counter = 1
            visited[cur] = True
            for child in adj_lst[cur]:
                if not visited[child]:
                    counter += dfs(child)
            if cur != 0:
                res += math.ceil(counter / seats)
            return counter
        dfs(0)
        return res
