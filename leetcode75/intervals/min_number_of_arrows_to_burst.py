from typing import List
from math import inf


class Solution:
    # the objective is to shrink the interval when you merge two intervals
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        cnt = 0
        last_end = -inf
        stack = [tuple(points[0])]
        for start, end in points[1:]:
            if stack:
                s1, e1 = stack[-1]
                if start <= e1:
                    stack.pop()
                    stack.append((max(start, s1), min(end, e1)))
                else:
                    stack.append((start, end))
        return len(stack)
