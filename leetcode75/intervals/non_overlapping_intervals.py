from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        stack = [intervals[0]]
        for start, end in intervals[1:]:
            if stack:
                s1, e1 = stack[-1]
                if start >= e1:
                    stack.append((start, end))
                else:
                    cnt += 1
        return cnt
