from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                s1_idx, s2_idx = i - 1, j - 1
                if nums1[s1_idx] == nums2[s2_idx]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]