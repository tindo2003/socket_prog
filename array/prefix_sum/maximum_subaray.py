from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        prefSum = 0
        min_val = 0

        for num in nums:
            prefSum += num
            res = max(res, prefSum - min_val)
            min_val = min(min_val, prefSum)

        return res
