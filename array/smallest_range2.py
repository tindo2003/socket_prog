from typing import List 
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        N = len(nums)
        for i in range(1, N):
            mini = min(nums[i] - k, nums[0] + k)
            maxi = max(nums[i-1] + k, nums[-1] - k)
            res = min(res, maxi - mini)
        return res