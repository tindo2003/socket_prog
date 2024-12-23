from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # size of arr containing at most one 0
        cnt_0 = 0
        l = 0
        N = len(nums)
        res = 0
        for r in range(N):
            if nums[r] == 0:
                cnt_0 += 1
            while cnt_0 > 1:
                if nums[l] == 0:
                    cnt_0 -= 1
                l += 1
            # delete one element
            res = max(res, r - l)
        return res
