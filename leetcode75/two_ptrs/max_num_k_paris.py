from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, N - 1
        cnt = 0
        nums.sort()
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                l += 1
                r -= 1
                cnt += 1
            elif s < k:
                l += 1
            else:
                r -= 1
        return cnt
