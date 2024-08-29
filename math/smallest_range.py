from typing import List
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # we want to bridge the gap by making the greatest number smaller
        # and smallest number greater. 
        # g - k. s + k 
        # g - k - s - k = g - s - 2k 
        max_num = max(nums)
        min_num = min(nums)
        return max(0, max_num - min_num - 2 * k)