from typing import List
from collections import defaultdict
from itertools import accumulate


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = list(accumulate(nums, initial=0))
        freq = defaultdict(int)
        cnt = 0
        # (s[i] - s[j]) % k = 0
        # s[i] % k - s[j] % k = 0
        # s[i] % k = s[j] % k
        for item in prefix_sum:
            cnt += freq[item % k]
            freq[item % k] += 1
        return cnt
