from typing import List


# 2D DP
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        my_dict = {k: v for v, k in enumerate(arr)}
        res = 0
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for r in range(n - 1, -1, -1):
            for c in range(r - 1, -1, -1):
                l_ele = arr[r]
                r_ele = arr[c]
                next_ele = l_ele + r_ele

                if next_ele in my_dict:
                    idx = my_dict[next_ele]
                    dp[r][c] = max(dp[r][c], dp[idx][r] + 1)
                    res = max(res, dp[r][c])
                else:
                    dp[r][c] = 2
        return res
