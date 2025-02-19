from typing import List
import math


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, math.ceil(n / 2)
        # the maximum number of pairs is ceil(n/2).
        # we splitting the array into 2 halves. one containing potential smaller numbers and the other containing potential larger numbers—and then greedily pair them to maximize the number of valid pairs.
        res = 0
        while r < n:
            l_ele = nums[l]
            r_ele = nums[r]
            if 2 * l_ele <= r_ele:
                res += 2
                l += 1
            r += 1
        return res
