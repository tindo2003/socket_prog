from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            max_val = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if matrix[nr][nc] > matrix[r][c]:
                        if dp[nr][nc] != -1:
                            max_val = max(max_val, dp[nr][nc])
                        else:
                            max_val = max(max_val, dfs(nr, nc))
            dp[r][c] = 1 + max_val
            return 1 + max_val

        res = 1
        for r in range(n):
            for c in range(m):
                tmp = dfs(r, c)
                res = max(res, tmp)
                dp[r][c] = tmp

        return res
