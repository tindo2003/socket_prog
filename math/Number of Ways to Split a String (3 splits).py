from math import comb
from itertools import accumulate


class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        s_lst = list(map(int, list(s)))
        s = sum(s_lst)
        if s == 0:
            # N-1 gaps. pick 2 vertical lines to divide
            num_ways = comb(len(s_lst) - 1, 2)
            return num_ways % MOD
        
        result, remainder = divmod(s, 3)
        if remainder != 0:
            return 0

        prefix_sum = list(accumulate(s_lst, initial=0))[1:]
        first_stop = result
        second_stop = result * 2
        cnt1 = cnt2 = 0
        for idx, val in enumerate(prefix_sum):
            if val == first_stop:
                cnt1 += 1
            elif val == second_stop:
                cnt2 += 1
        return (cnt1 * cnt2) % MOD
