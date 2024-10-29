from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        my_dict = defaultdict(int)
        res = 0

        def recur(idx, my_dict):
            if idx == len(nums):
                nonlocal res
                res += 1
                return
            cur_num = nums[idx]
            if cur_num + k not in my_dict and cur_num - k not in my_dict:
                my_dict[cur_num] += 1
                recur(idx + 1, my_dict)
                my_dict[cur_num] -= 1
                if my_dict[cur_num] == 0:
                    del my_dict[cur_num]
            recur(idx + 1, my_dict)

        recur(0, my_dict)
        return res - 1  # subtracting 1 because this counts empty arr too
