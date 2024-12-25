class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0] * n for _ in range(m)]
        grid[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                right = c + 1
                right_box = 0
                if 0 <= right < n:

                    right_box = grid[r][right]
                down = r + 1
                down_box = 0
                if 0 <= down < m:
                    down_box = grid[down][c]

                grid[r][c] = right_box + down_box

        return grid[0][0]
