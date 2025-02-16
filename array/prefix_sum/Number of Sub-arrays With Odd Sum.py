from typing import List
from collections import defaultdict, accumulate


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # [1, 3, 5]
        # [1], [5], [3], [1, 3, 5]
        # [1, 4, 9]
        # difference of two items with different parity results in an odd number
        # odd - even = even - odd = odd
        res = 0
        freq = defaultdict(int)
        pref_sum = list(accumulate(arr))
        for s in pref_sum:
            if s % 2 == 1:
                res += 1
            cur_mod = s % 2
            if cur_mod == 0:
                res += freq[1]
                freq[0] += 1
            else:
                res += freq[0]
                freq[1] += 1
        MOD = 10**9 + 7
        return res % MOD
