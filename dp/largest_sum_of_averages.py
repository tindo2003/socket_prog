from typing import List
from math import inf


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        N = len(nums)
        cache = {}

        def helper(cur_idx, k):
            if cur_idx == N:
                if k >= 0:
                    return 0
                else:
                    return -inf
            if k == 0:
                return -inf
            if (cur_idx, k) in cache:
                return cache[(cur_idx, k)]
            cur_sum = 0
            count = 0
            best_val = 0
            for new_idx in range(cur_idx, N):
                cur_sum += nums[new_idx]
                count += 1
                avg = cur_sum / count
                avg += helper(new_idx + 1, k - 1)
                best_val = max(best_val, avg)
            cache[(cur_idx, k)] = best_val
            return cache[(cur_idx, k)]

        return helper(0, k)
