from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        n = len(nums)
        res = 0
        for i in range(n):
            ele = nums[i] - i
            res += my_dict[ele]
            my_dict[ele] += 1
        number_of_pairs = n * (n - 1) // 2
        return number_of_pairs - res
