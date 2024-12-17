from collections import heapq
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        h = []
        s = set()
        res = 0
        for idx, num in enumerate(nums):
            heapq.heappush(h, (num, idx))
        while h:
            cur, idx = heapq.heappop(h)
            if idx not in s:
                res += cur
                s.add(idx)
                if idx - 1 >= 0:
                    s.add(idx - 1)
                if idx + 1 < len(nums):
                    s.add(idx + 1)
        return res
