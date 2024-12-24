from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [key for key in rooms[0]]
        visited = set([0])
        while q:
            cur = q.pop(0)
            visited.add(cur)
            new_keys = rooms[cur]
            for key in new_keys:
                if key not in visited:
                    q.append(key)
        return len(visited) == len(rooms)
