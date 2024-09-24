from typing import List 
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        h = []
        l, r = 0, N - 1
        for _ in range(candidates):
            heapq.heappush(h, (costs[l], l, 1))
            l += 1
        
        for _ in range(candidates):
            if r < l: break 
            heapq.heappush(h, (costs[r], r, -1))
            r -= 1

        ans = 0 
        while k > 0:
            c, idx, flag = heapq.heappop(h)
            ans += c

            if l <= r:
                if flag == 1:
                    heapq.heappush(h, (costs[l], l, 1))
                    l += 1
                else:
                    heapq.heappush(h, (costs[r], r, -1))
                    r -= 1
            k -= 1
        return ans  

        