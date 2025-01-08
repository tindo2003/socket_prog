from typing import List
import re


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # THE TRICK IS FOR EACH CELL IN THE OLD GRID, MAKE A NEW 3X3 GRID. MARK CELL VALUE 0=NO OBSTACLE 1=YES OBSTACLE
        pattern = r"(/)|(\\)|(\s)"

        N = len(grid)
        new_grid = []
        for r in range(N):
            cur_col = []
            cur_str = grid[r]

            matches = re.finditer(pattern, cur_str)
            for match in matches:
                if match.group(1):
                    cur_col.append(match.group(1))
                elif match.group(2):
                    cur_col.append(match.group(2))
                elif match.group(3):
                    cur_col.append(match.group(3))
            new_grid.append(cur_col)

        M = len(new_grid[0])
        bigger_matrix = [[0] * 3 * M for _ in range(3 * N)]
        for r in range(N):
            for c in range(M):
                if new_grid[r][c] == "/":
                    sr, sc = 3 * r, 3 * c + 2
                    for _ in range(3):
                        bigger_matrix[sr][sc] = 1
                        sr += 1
                        sc -= 1
                elif new_grid[r][c] == "\\":
                    sr, sc = 3 * r, 3 * c
                    for _ in range(3):
                        bigger_matrix[sr][sc] = 1
                        sr += 1
                        sc += 1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0] * 3 * M for _ in range(3 * N)]

        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # cell is empty and not visited yet and in bound
                if (
                    0 <= nr < 3 * N
                    and 0 <= nc < 3 * M
                    and not visited[nr][nc]
                    and bigger_matrix[nr][nc] == 0
                ):
                    dfs(nr, nc)

        cnt = 0
        for r in range(3 * N):
            for c in range(3 * M):
                if not visited[r][c] and bigger_matrix[r][c] == 0:
                    cnt += 1
                    dfs(r, c)
        return cnt
