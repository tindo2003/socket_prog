from collections import heapq 
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # basically n log k
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x**2 + y**2), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return list([x, y] for d, x, y in heap)