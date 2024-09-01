from typing import List 
from collections import deque 

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        q = deque([key for key in rooms[0]])
        while q:
            cur = q.popleft()
            visited.add(cur)
            for key in rooms[cur]:
                if key not in visited:
                    q.append(key)

        return len(visited) == len(rooms)