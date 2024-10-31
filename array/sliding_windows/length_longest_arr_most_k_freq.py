from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        my_freq = defaultdict(int)
        l = 0 
        N = len(nums)
        res = -inf
        for r in range(N):
            cur_num = nums[r]
            my_freq[cur_num] += 1
            while my_freq[cur_num] > k:
                my_freq[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
