from typing import List
from collections import defaultdict


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        my_dict = defaultdict(int)
        res = [0] * len(A)
        for idx in range(len(A)):
            if idx > 0:
                res[idx] = res[idx - 1]
            a = A[idx]
            b = B[idx]
            my_dict[a] += 1
            my_dict[b] += 1
            if my_dict[a] == 2:
                res[idx] += 1
            if a != b:
                if my_dict[b] == 2:
                    res[idx] += 1
        return res
