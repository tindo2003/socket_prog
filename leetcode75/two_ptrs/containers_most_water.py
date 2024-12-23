from math import inf 
from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        l, r = 0, N - 1
        res = -inf
        while l <= r:
            tmp = min(height[l], height[r]) * (r - l)
            res = max(tmp, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
