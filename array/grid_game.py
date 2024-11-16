from typing import List 
from math import inf 
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        first_forward = [0] * N
        first_forward[0] = grid[0][0]
        first_backward = [0] * N
        first_backward[N - 1] = grid[0][N - 1]
        second_forward = [0] * N
        second_forward[0] = grid[1][0]
        second_backward = [0] * N
        second_backward[N - 1] = grid[1][N - 1]
        for idx in range(1, N):
            first_forward[idx] = first_forward[idx - 1] + grid[0][idx]
            second_forward[idx] += second_forward[idx - 1] + grid[1][idx]
        for idx in range(N - 2, -1, -1):
            first_backward[idx] = first_backward[idx + 1] + grid[0][idx]
            second_backward[idx] += second_backward[idx + 1] + grid[1][idx]

        res = inf
        for idx in range(N):
            cur_max = 0
            if idx - 1 >= 0:
                cur_max = max(cur_max, second_forward[idx - 1])
            if idx + 1 < N:
                cur_max = max(cur_max, first_backward[idx + 1])
            res = min(res, cur_max)
        return res
