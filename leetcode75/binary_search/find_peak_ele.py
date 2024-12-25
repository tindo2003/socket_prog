from typing import List
from math import inf


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            middle = (l + r) // 2
            middle_ele = nums[middle]
            left_ele = right_ele = -inf
            if middle - 1 >= 0:
                left_ele = nums[middle - 1]
            if middle + 1 < N:
                right_ele = nums[middle + 1]
            if left_ele < middle_ele > right_ele:
                return middle
            else:
                # go to the right because there is a potential it may go down
                if left_ele <= middle_ele <= right_ele:
                    l = middle + 1
                else:
                    r = middle - 1
