from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for item in intervals:
            if not stack:
                stack.append(item)
            else:
                if item[0] > stack[-1][1] or item[1] > stack[-1][1]:
                    stack.append(item)
        return len(stack)
