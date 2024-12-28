from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        N, M = len(board), len(board[0])
        visited = [[0] * M for _ in range(N)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < N
                    and 0 <= nc < M
                    and not visited[nr][nc]
                    and board[nr][nc] == "X"
                ):
                    visited[nr][nc] = True
                    dfs(nr, nc)

        res = 0
        for r in range(N):
            for c in range(M):
                if not visited[r][c] and board[r][c] == "X":
                    visited[r][c] = True
                    dfs(r, c)
                    res += 1

        return res
