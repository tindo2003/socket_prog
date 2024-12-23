from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = sum(nums[:k])
        l = 0
        N = len(nums)
        res = k_sum / k
        for r in range(k, N):
            k_sum -= nums[l]
            k_sum += nums[r]
            l += 1
            res = max(res, k_sum / k)
        return res
