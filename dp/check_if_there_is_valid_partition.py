from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        my_dict = {}
        def dfs(idx):
            if idx == N: return True
            if idx + 1 >= N: return False
            if idx in my_dict: return my_dict[idx]
            first, second = False, False
            if nums[idx] == nums[idx + 1]:
                first = dfs(idx + 2)
            third_idx = idx + 2
            if third_idx < N:
                third_num = nums[third_idx]
                if (third_num == nums[idx] == nums[idx + 1]) or (nums[idx] == nums[idx + 1] - 1 and nums[idx + 1] == third_num - 1):
                    second = dfs(idx + 3)
            my_dict[idx] = first or second
            return my_dict[idx]
        return dfs(0)
            