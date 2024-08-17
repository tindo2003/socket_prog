from typing import List 
import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the observation is the time is strictly decreasing
        # this is the end of the range
        end = max(piles)
        start = 1
        res = inf

        while start <= end:
            mid = (start + end) // 2

            time = sum(math.ceil(pile / mid) for pile in piles)

            if time <= h:
                res = min(res, time)
                end = mid - 1
            else:
                start = mid + 1
        return res