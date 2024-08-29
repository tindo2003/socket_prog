from typing import List 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for d in range(N):
            for offset in range(1, N):
                # same row diff col or diff row same col
                nr = d - offset 
                nc = d - offset 
                if nr < 0 or nc < 0:
                    break 
                tmp = matrix[d][nc]
                matrix[d][nc] = matrix[nr][d]
                matrix[nr][d] = tmp 

        for r in range(N):
            lc = 0 
            rc = N - 1
            while lc <= rc:
                tmp = matrix[r][lc]
                matrix[r][lc] = matrix[r][rc]
                matrix[r][rc] = tmp 
                lc += 1
                rc -= 1
        