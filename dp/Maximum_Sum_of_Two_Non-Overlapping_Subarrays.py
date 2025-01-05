from typing import List
from math import inf
from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ans = -inf
        i = firstLen
        max_first_subarr = -inf
        s = 0
        # default behavior is sum
        prefix_sums = list(accumulate(nums, initial=0))
        N = len(prefix_sums)

        while i + secondLen < N:
            max_first_subarr = max(
                max_first_subarr, prefix_sums[i] - prefix_sums[i - firstLen]
            )
            ans = max(
                ans, max_first_subarr + (prefix_sums[i + secondLen] - prefix_sums[i])
            )
            i += 1

        max_second_subarr = -inf
        i = secondLen
        while i + firstLen < N:
            max_second_subarr = max(
                max_second_subarr, prefix_sums[i] - prefix_sums[i - secondLen]
            )
            ans = max(
                ans, max_second_subarr + (prefix_sums[i + firstLen] - prefix_sums[i])
            )
            i += 1
        
        return ans
