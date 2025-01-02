from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        idx = 0
        N, M = len(matrix), len(matrix[0])
        while idx < k and idx < N:
            heappush(h, (matrix[idx][0], idx, 0))
            idx += 1

        while k > 1:
            _, i, j = heappop(h)
            if j + 1 < M:
                heappush(h, (matrix[i][j + 1], i, j + 1))
            k -= 1

        return h[0][0]


"""
Another solution
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        N, M = len(matrix), len(matrix[0])
        for r in range(N):
            for c in range(M):
                heappush(h, -matrix[r][c])
                if len(h) > k:
                    heappop(h)
        return -h[0]
