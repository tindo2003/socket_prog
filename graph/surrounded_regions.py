from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n
                    and 0 <= nc < m
                    and board[nr][nc] == "O"
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = True
                    dfs(nr, nc)

        # start from the boundary. if the cell is not visited, it means that it can't be reached from the boundary. as a result, it can be safely turned into "X"
        for r in range(n):
            c = 0
            if not visited[r][c] and board[r][c] == "O":
                visited[r][c] = True
                dfs(r, c)
            c = m - 1
            if not visited[r][c] and board[r][c] == "O":
                visited[r][c] = True
                dfs(r, c)

        for c in range(m):
            r = 0
            if not visited[r][c] and board[r][c] == "O":
                visited[r][c] = True
                dfs(r, c)
            r = n - 1
            if not visited[r][c] and board[r][c] == "O":
                visited[r][c] = True
                dfs(r, c)

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"
