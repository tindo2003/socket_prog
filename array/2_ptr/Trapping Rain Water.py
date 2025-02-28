from typing import List
from math import inf


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        maxi = -inf
        for l in range(len(height)):
            maxi = max(maxi, height[l])
            left_max[l] = maxi

        maxi = -inf
        for r in range(n - 1, -1, -1):
            maxi = max(maxi, height[r])
            right_max[r] = maxi

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
