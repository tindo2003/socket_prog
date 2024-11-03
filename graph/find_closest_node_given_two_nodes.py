from typing import List
from collections import deque
from math import inf
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def find_dst(start: int) -> dict[int, int]:
            q = []
            best = {start: 0}
            q = deque([start])
            while q:
                cur = q.popleft()
                neighbor = edges[cur]
                if neighbor != -1 and neighbor not in best:
                    q.append(neighbor)
                    best[neighbor] = best[cur] + 1
            return best 

        dst1 = find_dst(node1)
        dst2 = find_dst(node2)
        tmp = []
        for k, v1 in dst1.items():
            if k in dst2:
                v2 = dst2[k]
                val = max(v1, v2)
                tmp.append((val, k))
        if not tmp: return -1
        sorted_data = sorted(tmp, key=lambda x: (x[0], x[1])) 
        return sorted_data[0][1]