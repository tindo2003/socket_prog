from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        [4,3,2,6] -> [6, 4, 3, 2] -> [2, 6, 4, 3] -> [3, 2, 6, 4]
        """
        N = len(nums)
        dp = [0] * N
        first = sum(i * nums[i] for i in range(N))
        s = sum(nums)
        res = first
        dp[0] = first
        ptr = 1
        for i in range(N - 1, 0, -1):
            nxt = dp[ptr - 1] + s - N * nums[i]
            dp[ptr] = nxt
            res = max(res, nxt)
            ptr += 1
        return res
