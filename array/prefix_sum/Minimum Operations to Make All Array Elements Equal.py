from itertools import accumulate
from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = list(accumulate(nums))
        res = []
        # sorted = [1 3 6 8]
        for q in queries:
            tmp = 0
            wanted_idx = bisect_left(nums, q)
            if wanted_idx >= len(nums):
                tmp += q * len(nums) - prefix_sum[len(nums) - 1]
            elif wanted_idx == 0:
                tmp += prefix_sum[len(nums) - 1] - q * len(nums)
            else:
                # the first half will be less than num so we need to do num*length of first half - sum of all elements in first half
                tmp += q * (wanted_idx) - prefix_sum[wanted_idx - 1]
                # the second half will be greater than num so we do sum of all elements in second half - num*length of second hald
                # imagine q = 5
                # we want 5-1 + 5-3 + 6-5 + 8-5
                # 5*2 - (1+3) + (6+8) - 5*2
                remaining = len(nums) - wanted_idx
                remaining_sum = prefix_sum[len(nums) - 1] - prefix_sum[wanted_idx - 1]
                tmp += remaining_sum - q * remaining

            res.append(tmp)
        return res
