from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # INVARIANCE: in a given window, we can never have > K zeros
        num_0 = 0
        N = len(nums)
        l = 0
        ans = 0 
        for r in range(N):
            if nums[r] == 0:
                num_0 += 1
            while num_0 > k:
                if nums[l] == 0: num_0 -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans 