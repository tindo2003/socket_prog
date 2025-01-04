from typing import List
from bisect import bisect
from collections import deque
from math import inf


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find the indices of the elements:
        # - res: the index of the largest element in arr that is strictly less than tgt
        # - res1: the index of the smallest element in arr that is greater than or equal to tgt
        N = len(arr)

        def binary_search(tgt):
            l, r = 0, N - 1
            res, res1 = -1, N
            while l <= r:
                m = (l + r) // 2
                if tgt <= arr[m]:
                    res1 = m
                    r = m - 1
                else:
                    res = m
                    l = m + 1
            return res, res1

        l, r = binary_search(x)
        res = deque([])
        for _ in range(k):
            l_ele = r_ele = inf
            if l >= 0:
                l_ele = arr[l]
            if r < N:
                r_ele = arr[r]
            l_d = abs(l_ele - x)
            r_d = abs(r_ele - x)
            if l_d <= r_d:
                res.appendleft(l_ele)
                l -= 1
            elif r_d < l_d:
                res.append(r_ele)
                r += 1
        return list(res)
