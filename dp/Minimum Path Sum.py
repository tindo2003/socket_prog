from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-1] * m for _ in range(n)]
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if r == n - 1 and c == m - 1:
                    dp[r][c] = grid[r][c]
                    continue
                c_right = c + 1
                r_down = r + 1

                if c_right < m:
                    dp[r][c] = grid[r][c] + dp[r][c_right]
                if r_down < n:
                    if dp[r][c] == -1:
                        dp[r][c] = grid[r][c] + dp[r_down][c]
                    else:
                        dp[r][c] = min(grid[r][c] + dp[r_down][c], dp[r][c])

        return dp[0][0]
