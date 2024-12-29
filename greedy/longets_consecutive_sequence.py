from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 1
        N = len(nums)
        cnt = 1
        for i in range(1, N):
            if nums[i] != nums[i - 1] + 1:
                cnt = 1
            else:
                cnt += 1
            res = max(res, cnt)
        return res
