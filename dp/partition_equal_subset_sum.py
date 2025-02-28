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


# version 2 using purely dfs
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        my_sum = sum(nums)
        if my_sum % 2 != 0:
            return False
        target_sum = my_sum // 2
        my_lst = []

        def dfs(cur_idx, cur_lst, cur_sum):
            if cur_idx == len(nums):
                if cur_sum == target_sum:
                    my_lst.append(cur_lst.copy())
                return
            # pick
            cur_lst.append(nums[cur_idx])
            dfs(cur_idx + 1, cur_lst, cur_sum + nums[cur_idx])
            cur_lst.pop()
            # unpick
            dfs(cur_idx + 1, cur_lst, cur_sum)

        dfs(0, [], 0)

        if my_lst:
            return True

        return False
