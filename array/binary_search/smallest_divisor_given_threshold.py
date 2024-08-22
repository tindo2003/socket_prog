from typing import List 
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        res = inf
        while l <= r:
            mid = (r + l) // 2
            my_sum = sum(math.ceil(item / mid) for item in nums)
            # divisor too small
            if my_sum > threshold:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res