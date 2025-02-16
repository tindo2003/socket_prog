from typing import List
from collections import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            tmp = x * 2 + y
            heapq.heappush(nums, tmp)
            res += 1
        return res
