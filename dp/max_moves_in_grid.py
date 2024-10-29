from collections import defaultdict
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        directions = [[-1, 1], [0, 1], [1, 1]]
        my_dict = defaultdict(int)

        def recur(x, y):
            if (x, y) in my_dict:
                return my_dict[(x, y)]
            total = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    nx >= 0
                    and nx < N
                    and ny >= 0
                    and ny < M
                    and grid[nx][ny] > grid[x][y]
                ):
                    total = max(total, 1 + recur(nx, ny))
            my_dict[(x, y)] = total
            return total

        res = -inf
        for r in range(N):
            res = max(res, recur(r, 0) - 1)
        return res
