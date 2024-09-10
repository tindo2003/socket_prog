from typing import List
from collections import defaultdict, deque
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        N = len(mat)
        M = len(mat[0])
        my_dict = defaultdict(deque)
        for r in range(N):
            for c in range(M):
                diff = r - c 
                my_dict[diff].append(mat[r][c])
        for key, vals in my_dict.items():
            my_dict[key] = deque(sorted(vals))
        
        for r in range(N):
            for c in range(M):
                diff = r - c 
                lst = my_dict[diff]
                mat[r][c] = lst[0]
                lst.popleft()

        return mat 
