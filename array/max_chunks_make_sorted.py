from math import inf
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        max_so_far = -inf
        res = 0
        for idx in range(N):
            max_so_far = max(max_so_far, arr[idx])
            if max_so_far == idx:
                max_so_far = -inf
                res += 1
        return res
