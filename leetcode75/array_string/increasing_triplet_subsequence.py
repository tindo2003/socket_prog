from math import inf
from typing import List


class Solution:
    """
    guaranteed to work method
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        min_left = [0] * N
        max_right = [0] * N
        mini = inf
        maxi = -inf
        for i in range(N):
            mini = min(mini, nums[i])
            min_left[i] = mini

        for i in range(N - 1, -1, -1):
            maxi = max(maxi, nums[i])
            max_right[i] = maxi

        for i in range(N):
            cur = nums[i]
            if min_left[i] < cur < max_right[i]:
                return True
        return False

    """
    smart way 
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = inf
        for num in nums:
            # less than or equal so we won't reach the third case which is to return True
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
