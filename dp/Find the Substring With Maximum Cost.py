from collections import defaultdict
from typing import List
from math import inf


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # kadane algo
        my_dict = defaultdict(int)
        for i in range(len(chars)):
            my_dict[chars[i]] = vals[i]
        my_lst = []
        for c in s:
            if c in my_dict:
                my_lst.append(my_dict[c])
            else:
                my_lst.append(ord(c) - ord("a") + 1)
        min_val = 0
        s = 0
        res = -inf

        for num in my_lst:
            s += num
            res = max(res, s - min_val)
            min_val = min(min_val, s)
        return max(res, 0)
