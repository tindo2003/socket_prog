from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # the sum of any two sides must be greater than the third side
        # IDEA: make c fixed. while l < r: move l and r accordingly to the nums[l] + nums[r]
        N = len(nums)
        nums.sort()
        cnt = 0
        for c in range(N - 1, 1, -1):
            l, r = 0, c - 1
            while l < r:
                if nums[l] + nums[r] > nums[c]:
                    cnt += r - l
                    r -= 1
                else:
                    l += 1
        return cnt
