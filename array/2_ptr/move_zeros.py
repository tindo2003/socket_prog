from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        prev_non_zero = 0
        for r in nums:
            cur_ele = nums[r]
            if cur_ele != 0:
                nums[prev_non_zero] = cur_ele
                prev_non_zero += 1
        for i in range(prev_non_zero, N):
            nums[i] = 0
        return nums
        