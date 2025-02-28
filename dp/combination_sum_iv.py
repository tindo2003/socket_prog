from typing import List


# 377. Combination Sum IV
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [-1] * (target + 1)

        def dfs(tgt):
            if tgt == 0:
                return 1
            if dp[tgt] != -1:
                return dp[tgt]
            tmp = 0
            for num in nums:
                # if num is greater than tgt, it can't add anything positive number to make up target
                if num <= tgt:
                    tmp += dfs(tgt - num)
            dp[tgt] = tmp
            return tmp

        return dfs(target)
