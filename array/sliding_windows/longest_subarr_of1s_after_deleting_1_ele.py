from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        nums_0 = 0
        N = len(nums)
        ans = 0
        for r in range(N):
            if nums[r] == 0: nums_0 += 1
            while nums_0 > 1:
                if nums[l] == 0: nums_0 -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans - 1
        