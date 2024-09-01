from typing import (
    List,
)

import heapq


#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        h = []
        if not intervals: return 0
        res = 1
        sorted_intv = sorted(intervals, key=lambda x: x.start)
        heapq.heappush(h, sorted_intv[0].end)

        for item in sorted_intv[1:]:
            start2, end2 = item.start, item.end 
            end1 = h[0]
            if start2 < end1:
                res += 1
            else:
                heapq.heappop(h)
            heapq.heappush(h, end2)
        return res