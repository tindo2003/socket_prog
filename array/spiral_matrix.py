from typing import List 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        N = len(matrix)
        M = len(matrix[0])
        first_row, first_col = 0, 0
        last_row, last_col = N - 1, M - 1
        while first_row <= last_row and first_col <= last_col:
            for i in range(first_col, last_col):
                res.append(matrix[first_row][i])
            first_row += 1
            for i in range(first_row, last_row):
                res.append(matrix[i][last_col])
            last_col -= 1
            if first_row <= last_row:
                for i in range(last_col, first_col, -1):
                    res.append(matrix[last_row][i])
                last_row -= 1
            if first_col <= last_col:
                for i in range(last_row, first_row, -1):
                    res.append(matrix[i][0])
                first_col += 1 
        return res