from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def to_bin(n):
            cnt = 0
            while n != 0:
                div, mod = divmod(n, 2)
                n = div
                if mod == 1:
                    cnt += 1
            return cnt

        res = []
        for i in range(n + 1):
            tmp = to_bin(i)
            res.append(tmp)
        return res
