from typing import List 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lst = []
        for start, end in intervals:
            lst.append((start, 1))
            # + 1 for edge case
            lst.append((end+1, -1))
        lst.sort()

        cur = 0
        start = None
        res = []
        for x, t in lst:
            cur += t
            # cur transitions from 0 to 1
            if cur == 1 and t == 1:
                start = x 
            # cur transitions from z to 0
            elif cur == 0:
                end = x - 1
                res.append([start, end])
        return res