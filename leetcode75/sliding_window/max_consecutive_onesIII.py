from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # substring contain k 0's
        k_cnt = 0
        l = 0
        res = 0
        N = len(nums)
        for r in range(N):
            num = nums[r]
            if num == 0:
                k_cnt += 1
            while k_cnt > k:
                if nums[l] == 0:
                    k_cnt -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
