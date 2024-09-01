from typing import List 

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        sorted_arr = sorted(intervals, key=lambda x: x.start)
        for idx in range(1, len(sorted_arr)):
            start1, end1 = sorted_arr[idx - 1].start, sorted_arr[idx - 1].end
            start2, end2 = sorted_arr[idx].start, sorted_arr[idx].end
            if start2 < end1:
                return False 
        return True