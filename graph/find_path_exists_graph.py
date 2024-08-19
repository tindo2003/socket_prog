from typing import List 
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_lst = defaultdict(list) # string to arr 
        if source == destination:
            return True
        for x, y in edges:  
            adj_lst[x].append(y)
            adj_lst[y].append(x)
        queue = deque()
        queue.append(source)
        visited = set()

        while queue:
            now = queue.popleft()
            for neighbor in adj_lst[now]:
                if neighbor == destination:
                    return True 
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False