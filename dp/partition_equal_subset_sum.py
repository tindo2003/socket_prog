from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        memo = [[-1] * (s + 1) for _ in range(len(nums))]

        def dfs(idx, cur_sum):
            if idx == len(nums):
                if cur_sum == target:
                    return True
                return False
            if cur_sum >= target:
                return False
            if memo[idx][cur_sum] != -1:
                return memo[idx][cur_sum]
            picked = dfs(idx + 1, cur_sum + nums[idx])
            non_picked = dfs(idx + 1, cur_sum)
            tmp = picked or non_picked
            memo[idx][cur_sum] = tmp
            return tmp

        return dfs(0, 0)
