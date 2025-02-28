from typing import (
    List,
)

from heapq import heappush, heappop


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
        # Write your code here
        intervals.sort(key=lambda x: x.start)  # sort by start time
        h = []
        # we end meeting to ends as early as possible. however, if we encounter
        # a meeting that starts later than the current endtime, then we gotta
        # start a new meeting room
        for interval in intervals:
            print(h)
            start, end = interval.start, interval.end
            if not h:
                heappush(h, end)
                continue
            previous_end = h[0]
            if start >= previous_end:
                heappop(h)
                heappush(h, end)
            else:
                heappush(h, end)

        return len(h)
