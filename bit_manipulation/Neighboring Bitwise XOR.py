from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # derived = [1,1,0]
        # 0 xor 1, 1 xor 0, 0 xor 0
        # the tips are very helpful
        tmp = 0
        for ele in derived:
            tmp ^= ele
        return tmp == 0
