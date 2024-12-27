from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left_ele = values[0] + 0
        N = len(values)
        res = 0
        for r in range(1, N):
            right_ele = values[r] - r
            res = max(res, left_ele + right_ele)
            left_ele = max(left_ele, values[r] + r)
        return res
