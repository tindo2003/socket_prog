from typing import List 
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_arr = sorted(intervals, key=lambda x: x[0])
        res = 0
        l = 0 
        for r in range(1,len(sorted_arr)):
            start1, end1 = sorted_arr[l]
            start2, end2 = sorted_arr[r]
            # case 1: the current interval is entirely inside prev interval
            if start2 >= start1 and end1 >= end2:
                l = r # remove prev
                res += 1
                continue 
            # case 2: current interval is overlapping with previous element.
            if start2 < end1 and end2 > end1:   
                res += 1
                continue  # remove current 
            # if nothing gets removed, left moves on
            l=r
        return res