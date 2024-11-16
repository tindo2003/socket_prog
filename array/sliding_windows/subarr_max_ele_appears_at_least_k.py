from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        counter = 0
        l = 0
        N = len(nums)
        res = 0 
        for r in range(N):
            num = nums[r]
            if num == maxi: counter += 1
            while counter >= k:
                res += N - r
                if nums[l] == maxi:
                    counter -= 1
                l += 1
        return res