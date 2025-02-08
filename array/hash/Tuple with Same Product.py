from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        my_dict = defaultdict(int)
        for i in range(N):
            for j in range(i + 1, N):
                my_prod = nums[i] * nums[j]
                my_dict[my_prod] += 1
        res = 0
        for k, v in my_dict.items():
            if v > 1:
                # if there are 3 pairs. you can choose 2 out of 3
                # for each pair, you have 8 possible combinations
                combinations = (v * (v - 1)) // 2
                res += combinations * 8
        return res
