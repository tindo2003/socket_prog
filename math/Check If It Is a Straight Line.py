from math import inf
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        N = len(coordinates)
        prev_m = prev_b = 0
        for i in range(1, N):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]
            denom = x2 - x1
            if denom == 0:
                m = inf
            else:
                m = (y2 - y1) / (x2 - x1)
            if m == inf:
                b = 0
            else:
                b = y2 - m * x2
            if i != 1:
                if m != prev_m or b != prev_b:
                    return False
            prev_m = m
            prev_b = b
        return True
