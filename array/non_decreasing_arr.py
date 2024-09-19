from typing import List 
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        cache = {}
        def lis(cur_idx):
            best = 1
            if cur_idx in cache: return cache[cur_idx]
            for new_idx in range(cur_idx + 1, N):
               if nums[new_idx] >= nums[cur_idx]:
                   best = max(best, 1 + lis(new_idx))
            cache[cur_idx] = best
            return best
        best1 = lis(0)
        best2 = lis(1)
        
        if best1 == N or best1 + 1 == N or best2 == N or best2 + 1 == N:
            return True
        return False

'''
Best solution
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        pass