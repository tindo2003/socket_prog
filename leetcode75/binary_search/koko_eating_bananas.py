from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = -1
        while l <= r:
            rate = (r + l) // 2
            total_hours = sum([math.ceil(p / rate) for p in piles])
            if total_hours <= h:
                res = rate
                # want to experiment even lower rate
                r = rate - 1
            else:
                l = rate + 1
        return res
