from typing import List 
from bisect import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # 0 1 4 4 5 7
        nums.sort()
        res = 0
        for num in nums:
            """
            lower <= num + y <= upper
            lower - num <= y <= upper - num
            """
            idx_gte = bisect.bisect_left(nums, lower - num)
            # all elements *before* index idx_lte satisfy the condition <= upper - num.
            idx_lte = bisect.bisect_right(nums, upper - num)
            res += idx_lte - idx_gte
            if (
                lower - num <= num <= upper - num
            ):  # don't want to count the number twice as a pair. (num, num)
                res -= 1
        return res // 2
