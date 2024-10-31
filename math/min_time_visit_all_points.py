from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            x2, y2 = points[i]
            x1, y1 = points[i - 1]
            if x1 == x2: 
                res += abs(y2 - y1)
                continue
            if y1 == y2: 
                res += abs(x2 - x1)
                continue
            s = 0
            
            # there are two choices. one = u could match the x. second = you could match the y
            nx1 = x1 + (x2 - x1)
            ny1 = y1 + (x2 - x1)
            ny3 = y1 - (x2 - x1)
            
            s1 = abs(y2 - ny1) + abs(x2 - x1)
            s3 = abs(y2 - ny3) + abs(x2 - x1)

            ny1 = y1 + (y2 - y1)
            nx1 = x1 + (y2 - y1)
            nx2 = x1 - (y2 - y1)
            
            s2 = abs(x2 - nx1) + abs(y2 - y1)
            s4 = abs(x2 - nx2) + abs(y2 - y1)
            res += min(s1, s2, s3, s4)
            
        return res
