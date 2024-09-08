from typing import List 
import math 
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: 
            return 0
        l = 0 
        N = len(nums)
        res = 0
        prod = 1
        for r in range(N):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            res += (r - l + 1)
        return res  

