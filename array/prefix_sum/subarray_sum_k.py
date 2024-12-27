from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = defaultdict(int)
        # in case the array contains 0. for the case like [-1, 1, 0]. the last 0 will contribute 2 to the result because 0 itself and the (-1, 1, 0)
        my_dict[0] = 1
        s = 0
        res = 0
        for num in nums:
            # prefix sum
            s += num
            if s - k in my_dict:
                res += my_dict[s - k]
            # count the frequency of the prefix sum
            my_dict[s] += 1
        return res
