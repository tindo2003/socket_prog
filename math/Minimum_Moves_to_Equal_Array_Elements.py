from math import inf
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s = 0
        N = len(nums)
        mini = inf
        for num in nums:
            mini = min(mini, num)
            s += num
        # s - mini to exclude the minimum itself.
        return (s - mini) - (mini * (N - 1))
