from typing import List 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        cache = {}
        def helper(cur_idx):
            if cur_idx in cache:
                return cache[cur_idx]
            best_val = 1
            for new_idx in range(cur_idx + 1, N):
                if nums[new_idx] > nums[cur_idx]:
                    best_val = max(best_val, 1 + helper(new_idx))
            cache[cur_idx] = best_val
            return cache[cur_idx]
        return max(helper(i) for i in range(N))