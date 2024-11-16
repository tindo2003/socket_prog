from typing import List 
import heapq
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        cur_sum = neededTime[0]
        time_q = [-neededTime[0]]
        for idx in range(1, len(colors)):
            cur_c = colors[idx]
            prev_c = colors[idx - 1]
            if cur_c != prev_c:
                if len(time_q) > 1:
                    res += (cur_sum - (-1 * heapq.heappop(time_q)))
                time_q = []
                cur_sum = 0
            heapq.heappush(time_q, -neededTime[idx])
            cur_sum += neededTime[idx]
        if len(time_q) > 1:
            res += (cur_sum - (-1 * heapq.heappop(time_q)))
        return res
