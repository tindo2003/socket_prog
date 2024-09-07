from typing import List 
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        cur_sum = 0
        N = len(nums)
        res = -inf
        for i in range(k):
            cur_sum += nums[i]
            counter[nums[i]] += 1
        if len(counter) == k:
            res = cur_sum 
        for idx in range(k, N):
            cur_sum -= nums[idx - k]
            cur_sum += nums[idx]
            counter[nums[idx - k]] -= 1
            if counter[nums[idx - k]] == 0:
                del counter[nums[idx - k]]
            counter[nums[idx]] += 1 
            if len(counter) == k:
                res = max(res, cur_sum)
        return res