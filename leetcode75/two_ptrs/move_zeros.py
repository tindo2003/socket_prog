from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Similar to Quicksort partition
        The only thing that would keep right_ptr and left_ptr apart is when there is a row of zeros 
        """
        l = 0
        N = len(nums)
        for r in range(N):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
