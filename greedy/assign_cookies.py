from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_g = sorted(g, reverse=True)
        N1 = len(g)
        sorted_s = sorted(s, reverse=True)
        N2 = len(s)
        res = 0
        greed_idx = 0
        size_idx = 0
        while greed_idx < N1 and size_idx < N2:
            if sorted_s[size_idx] < sorted_g[greed_idx]:
                greed_idx += 1
            else:
                res += 1
                size_idx += 1
                greed_idx += 1
        return res