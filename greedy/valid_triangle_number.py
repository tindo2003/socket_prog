from typing import List 
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
      nums.sort()
      res = 0 
      N = len(nums)
      
      for third_idx in range(N - 1, -1, -1):
        first_idx = 0 
        second_idx = third_idx - 1
        while first_idx <= second_idx:
          if nums[first_idx] + nums[second_idx] > nums[third_idx]:
            res += (second_idx - first_idx)
            second_idx -= 1
          else:
            first_idx += 1
      return res