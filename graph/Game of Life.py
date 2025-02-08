class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #
        # 2 = dead prev dead
        # 3 = dead prev alive
        # 4 = alive prev dead
        # 5 = alive prev alive
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]
        n, m = len(board), len(board[0])
        for r in range(n):
            for c in range(m):
                cur_cell = board[r][c]

                num_alive_neighbors = 0
                num_dead_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        if board[nr][nc] in [0, 4, 2]:
                            num_dead_neighbors += 1
                        if board[nr][nc] in [1, 5, 3]:
                            num_alive_neighbors += 1

                if cur_cell in [1, 4, 5]:
                    if 2 <= num_alive_neighbors <= 3:
                        board[r][c] = 5
                    else:
                        board[r][c] = 3
                else:
                    if num_alive_neighbors == 3:
                        print("i am here")
                        board[r][c] = 4
                    else:
                        board[r][c] = 2

        for r in range(n):
            for c in range(m):
                if board[r][c] in [2, 3]:
                    board[r][c] = 0
                else:
                    board[r][c] = 1
