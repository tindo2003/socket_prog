from typing import List 
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        N = len(matrix)
        M = len(matrix[0])
        new_matrix = [[0 for _ in range(N)] for _ in range(M)]
        for r in range(N):
            for c in range(M):
                new_matrix[c][r] = matrix[r][c]
        return new_matrix
        