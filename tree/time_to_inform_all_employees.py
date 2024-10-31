from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        adj_lst = defaultdict(list)
        for idx, val in enumerate(manager):
            if val != -1:
                adj_lst[val].append(idx)
        
        def dfs(cur_node, cur_time):
            
            nonlocal res
            res = max(res, cur_time) 
            for neighbor in adj_lst[cur_node]:
                dfs(neighbor, cur_time + informTime[cur_node])
        dfs(headID, 0)
        return res
