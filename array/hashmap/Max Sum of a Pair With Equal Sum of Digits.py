from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        my_dict = defaultdict(list)

        def find_sum_of_digits(num):
            res = 0
            while num != 0:
                div, mod = divmod(num, 10)
                res += mod
                num = num // 10
            return res

        for num in nums:
            s = find_sum_of_digits(num)
            my_dict[s].append(num)

        res = -1
        for k, cur_lst in my_dict.items():
            if len(cur_lst) >= 2:
                cur_lst.sort()
                res = max(res, cur_lst[-1] + cur_lst[-2])
        return res
