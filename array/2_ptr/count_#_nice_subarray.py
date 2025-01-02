from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # LITERALLY JUST https://leetcode.com/problems/subarray-sum-equals-k/
        nums = [0 if n % 2 == 0 else 1 for n in nums]
        my_dict = defaultdict(int)
        cur_sum = 0
        my_dict[cur_sum] = 1
        res = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in my_dict:
                res += my_dict[cur_sum - k]
            my_dict[cur_sum] += 1
        return res
