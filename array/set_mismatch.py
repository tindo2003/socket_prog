from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        freq = Counter(nums)

        for num in range(1, len(nums) + 1):
            v = freq[num]
            if v == 0:
                res[1] = num
            elif v == 2:
                res[0] = num
        return res
