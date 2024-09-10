from typing import List 
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # too hard. need to revisit
        N = len(mat)
        M = len(mat[0])
        
        for c in range(M):
            for r in range(1, N):
                mat[r][c] += mat[r-1][c]
        
        for r in range(N):
            for c in range(1, M):
                mat[r][c] += mat[r][c-1]
        
        print(mat)
