from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # objective: sliding window of FIXED SIZED = len(p)
        freq = Counter(p)
        l = 0
        N = len(s)
        keep_track = defaultdict(int)
        res = []

        def check():
            for k, v in freq.items():
                if keep_track[k] != v:
                    return False
            return True

        for r in range(N):
            keep_track[s[r]] += 1
            # fixed size of length p
            if r >= len(p) - 1:
                if check():
                    res.append(l)
                keep_track[s[l]] -= 1
                l += 1
        return res
