from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        N, M = len(matrix), len(matrix[0])
        for c in range(M):
            r = 0
            cur_val = matrix[r][c]
            while True:
                nr, nc = r + 1, c + 1
                if 0 <= nr < N and 0 <= nc < M:
                    if matrix[nr][nc] != cur_val:
                        return False
                else:
                    break
                r, c = nr, nc
                
        for r in range(N):
            c = 0
            cur_val = matrix[r][c]
            while True:
                nr, nc = r + 1, c + 1
                if 0 <= nr < N and 0 <= nc < M:
                    if matrix[nr][nc] != cur_val:
                        return False
                else:
                    break
                r, c = nr, nc
        return True
