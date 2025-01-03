from typing import List
from math import inf


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        left = [inf] * N  # initially, we don't know where number 1 is
        right = [inf] * N
        for i in range(0, N):
            if i == 0:
                if seats[i] == 1:
                    left[i] = 0
                continue
            if seats[i] == 1:
                left[i] = 0
            else:
                left[i] = left[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if i == N - 1:
                if seats[i] == 1:
                    right[i] = 0
                continue
            if seats[i] == 1:
                right[i] = 0
            else:
                right[i] = right[i + 1] + 1
                
        res = 0
        for i in range(N):
            ldist = left[i]
            rdist = right[i]
            tmp = min(ldist, rdist)
            res = max(tmp, res)
        return res
