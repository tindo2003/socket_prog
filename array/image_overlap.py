from typing import List
from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        arr1_coors = []
        arr2_coors = []
        for r in range(N):
            for c in range(N):
                if img1[r][c] == 1:
                    arr1_coors.append((r, c))
                if img2[r][c] == 1:
                    arr2_coors.append((r, c))
        my_dict = defaultdict(int)
        for (r1, c1) in arr1_coors:
            for (r2, c2) in arr2_coors:
                dx = r2 - r1 
                dy = c2 - c1 
                my_dict[(dx, dy)] += 1
        best_freq = 0
        for key, val in my_dict.items():
            if val > best_freq:
                best_freq = val
        return best_freq
                