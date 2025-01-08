from itertools import accumulate
from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums, initial=0))

        def binary_search(tgt):
            """
            objective: find the greatest index less than or equal to target
            """
            res = -1
            l, r = 0, len(prefix_sum) - 1
            while l <= r:
                m = (l + r) // 2
                if tgt < prefix_sum[m]:
                    r = m - 1
                else:
                    res = m
                    l = m + 1
            return res

        mini = inf
        for i, item in enumerate(prefix_sum):
            if item >= target:
                needed = item - target
                idx = binary_search(needed)
                mini = min(mini, i - idx)
        if mini == inf:
            return 0
        return mini
