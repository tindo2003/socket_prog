from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for idx in range(1, N):
            if nums[idx] <= nums[idx-1]:    
                cur_diff = nums[idx-1] - nums[idx] + 1
                nums[idx] += cur_diff 
                res += cur_diff
        return res