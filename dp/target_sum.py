from typing import List
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dfs(idx, cur_sum):
            if idx == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            if (idx, cur_sum) in memo:
                return memo[(idx, cur_sum)]
            picked = dfs(idx + 1, cur_sum + nums[idx])
            nonpicked = dfs(idx + 1, cur_sum - nums[idx])
            memo[(idx, cur_sum)] = picked + nonpicked
            return picked + nonpicked

        return dfs(0, 0)
