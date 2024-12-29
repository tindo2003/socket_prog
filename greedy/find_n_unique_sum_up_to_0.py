from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        half = n // 2
        res = []
        for i in range(1, half + 1):
            res.append(i)
            res.append(-i)
        if n % 2 == 1:
            res.append(0)
        return res
