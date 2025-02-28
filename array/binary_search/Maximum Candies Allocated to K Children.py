from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # the max one can give max of candies
        # 0 -> 18
        def f(target):
            if target == 0:
                return True
            cnt = 0
            for num in candies:
                cnt += num // target
            return cnt >= k

        l, r = 0, max(candies)
        res = -1
        while l <= r:
            m = (l + r) // 2
            if f(m):
                l = m + 1
                res = m
            else:
                r = m - 1
        return res
