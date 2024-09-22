from typing import List 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[0:k])
        ans = cur_sum / k
        N = len(nums)
        for idx in range(k, N):
            cur_sum -= nums[idx - k] 
            cur_sum += nums[idx]
            ans = max(ans, cur_sum / k)
        return ans