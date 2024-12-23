from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        N, M = len(grid), len(grid[0])
        for c in range(M):
            column = []
            for r in range(N):
                column.append(grid[r][c])
            columns.append(column)

        cnt = 0
        for row in grid:
            for column in columns:
                if row == column:
                    cnt += 1
        return cnt
