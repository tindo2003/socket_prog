from typing import List 
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        N, M = len(board), len(board[0])
        visited = [[False] * M for _ in range(N)]
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        def dfs(x, y):
            # check surrounding
            bomb_count = 0
            my_lst = []
            visited[x][y] = True 
            for dx, dy in directions:
                nx, ny = x + dx, dy + y 
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if board[nx][ny] == "M":
                        bomb_count += 1
                    else:
                        my_lst.append((nx, ny))
            if bomb_count > 0:
                board[x][y] = str(bomb_count)
                return 
            board[x][y] = "B"
            for nx, ny in my_lst:
                dfs(nx, ny)
            

        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board 
        if board[x][y] == "E":
            dfs(x, y)

        return board 
