from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        indices_lst = []
        n = len(s)
        for idx, c in enumerate(s):
            if c == "|":
                indices_lst.append(idx)
        pref_sum = [0] * n
        if s[0] == "*":
            pref_sum[0] = 1
        for i in range(1, n):
            c = s[i]
            pref_sum[i] = pref_sum[i - 1]
            if c == "*":
                pref_sum[i] += 1

        res = []

        for left, right in queries:
            # find one index less than or equal to left
            tmp_left = bisect_left(indices_lst, left)
            if tmp_left == len(indices_lst):
                res.append(0)
                continue
            left_index = indices_lst[tmp_left]
            # find one index less than or equal to right
            tmp_right = bisect_right(indices_lst, right) - 1
            if tmp_right < 0:
                res.append(0)
                continue
            right_index = indices_lst[tmp_right]
            if right_index <= left_index:
                res.append(0)
            else:
                res.append(pref_sum[right_index] - pref_sum[left_index])
        return res
