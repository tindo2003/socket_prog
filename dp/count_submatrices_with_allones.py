from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        res = 0
        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 1:
                    upr, upc = r - 1, c
                    leftr, leftc = r, c - 1
                    diagleftr, diagleftc = r - 1, c - 1
                    if upr >= 0:
                        matrix[r][c] = matrix[upr][upc]
                    else:
                        matrix[r][c] = 0
                    if leftr >= 0:
                        matrix[r][c] = min(matrix[r][c], matrix[leftr][leftc])
                    else:
                        matrix[r][c] = 0
                    if diagleftr >= 0 and diagleftc >= 0:
                        matrix[r][c] = min(matrix[r][c], matrix[diagleftr][diagleftc])
                    else:
                        matrix[r][c] = 0
                    matrix[r][c] += 1
                    res += matrix[r][c]
        return res
