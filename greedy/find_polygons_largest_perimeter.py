from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        N = len(nums)
        p_sum = [0] * N
        cur_sum = 0
        nums.sort(reverse=True)
        for idx, num in enumerate(nums):
            cur_sum += num
            p_sum[idx] = cur_sum
        for i in range(len(nums)):
            longest_candidate = nums[i]
            later_sums = p_sum[-1] - p_sum[i]
            if later_sums > longest_candidate:
                return later_sums + longest_candidate
        return -1
        
