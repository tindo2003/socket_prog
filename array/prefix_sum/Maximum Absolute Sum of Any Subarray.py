from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        this is Kadane's algorithm but with extra stuffs
        """

        def kadane(arr):
            pref_sum = 0
            min_val = max_val = 0
            min_res = 0
            max_res = 0
            for num in nums:
                pref_sum += num
                max_res = max(max_res, pref_sum - min_val)
                min_res = min(min_res, pref_sum - max_val)
                min_val = min(min_val, pref_sum)
                max_val = max(max_val, pref_sum)
            return min_res, max_res

        min_subarr_sum, max_subarr_sum = kadane(nums)
        return max(abs(min_subarr_sum), abs(max_subarr_sum))
