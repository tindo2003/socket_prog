from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        tmp = [-1] * (N + 1)
        for idx, val in enumerate(nums):
            tmp[val] += 1
        res = []
        for i in range(1, N + 1):
            if tmp[i] == -1:
                res.append(i)
        return res
