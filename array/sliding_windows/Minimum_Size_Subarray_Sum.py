from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        N = len(nums)
        s = 0
        res = inf
        for r in range(N):
            s += nums[r]
            while l <= r and s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
        if res == inf:
            return 0
        return res
