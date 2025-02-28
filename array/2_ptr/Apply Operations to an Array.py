from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            next_num = nums[i + 1]
            cur_num = nums[i]
            if next_num == cur_num:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0

        for r in range(n):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
        for i in range(l, n):
            nums[i] = 0
        return nums
