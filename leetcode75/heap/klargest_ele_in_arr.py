from heapq import heappush, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        # since k largest, use the inverse which is min heap
        for num in nums:
            heappush(h, num)
            if len(h) > k:
                heappop(h)
        return h[0]
