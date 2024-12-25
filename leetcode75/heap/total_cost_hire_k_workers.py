from typing import List
from heapq import heappush, heappop


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # lesson: control ordering of heap by one extra element
        # use two pointers approach
        # simulation
        h = []
        total = 0
        N = len(costs)
        l, r = 0, N - 1
        for _ in range(candidates):
            heappush(h, (costs[l], 0))
            l += 1
        for _ in range(candidates):
            if r < l:
                break
            heappush(h, (costs[r], 1))
            r -= 1
        for _ in range(k):
            val, dire = heappop(h)
            # popped from left
            if dire == 0:
                if l <= r:
                    heappush(h, (costs[l], 0))
                    l += 1
            # popped from right
            else:
                if l <= r:
                    heappush(h, (costs[r], 1))
                    r -= 1
            total += val
        return total
