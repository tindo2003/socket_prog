from typing import List
from math import inf
from itertools import combinations
from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # This approach is somewhat brute force.
        # For each horizontal line y, we collect all corresponding x-coordinates.
        # Then, for every pair of horizontal lines (y1, y2), we find all x-coordinate pairs in the intersection of x-coordinates for y1 and y2.
        y_points = defaultdict(set)
        res = inf
        for x, y in points:
            y_points[y].add(x)
        for y1, y2 in combinations(y_points.keys(), r=2):
            x1_lst = y_points[y1]
            x2_lst = y_points[y2]
            for x1, x2 in combinations(x1_lst.intersection(x2_lst), r=2):
                res = min(res, (abs(y2 - y1) * abs(x2 - x1)))
        if res == inf:
            return 0
        return res
