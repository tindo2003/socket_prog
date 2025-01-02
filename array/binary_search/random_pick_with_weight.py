from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.pref_sum = []
        self.s = 0
        for item in w:
            self.s += item
            self.pref_sum.append(self.s)

    def pickIndex(self) -> int:
        """
        Example: [3, 5, 8]
        Prefix sum: [3, 8, 16]
        Element 0 corresponds to the range [0, 3) (3 elements).
        Element 1 corresponds to the range [3, 8) (5 elements).
        Element 2 corresponds to the range [8, 16) (8 elements).
        Hence why random.randint(0, s-1) (non inclusive at right end)
        randint is inclusive both ends
        """
        random_number = random.randint(0, self.s - 1)

        def binary_search(tgt):
            res = 0
            l, r = 0, len(self.pref_sum) - 1
            while l <= r:
                m = (l + r) // 2
                if self.pref_sum[m] <= tgt:
                    l = m + 1
                else:
                    r = m - 1
                    res = m
            return res

        tmp = binary_search(random_number)
        return tmp


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
