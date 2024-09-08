from typing import List
import math 
from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        N = len(bombs)
        for i, item1 in enumerate(bombs):
            for j in range(i + 1, N):
                x1, y1, r1 = item1[0], item1[1], item1[2]  
                x2, y2, r2 = bombs[j][0], bombs[j][1], bombs[j][2] 
                dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                if dist <= r2:
                    adj_list[j].append(i)
                if dist <= r1:
                    adj_list[i].append(j)
        res = float("-inf")
        
        def dfs(i):
            for new_idx in adj_list[i]:
                if new_idx not in self.visited:
                    self.visited.add(new_idx)
                    dfs(new_idx)
            
        for i in range(N):
            self.visited = set() 
            self.visited.add(i)
            dfs(i)
            
            res = max(res, len(self.visited))  
        return res