from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        res = len(s)
        for k, v in freq.items():
            if v > 2:
                res -= ((v - 1) // 2) * 2
        return res
