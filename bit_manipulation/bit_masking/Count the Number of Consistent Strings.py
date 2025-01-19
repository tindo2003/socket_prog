from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bit = 0
        for c in allowed:
            shift_amnt = ord(c) - ord("a")
            bit |= 1 << shift_amnt

        res = len(words)
        for word in words:
            for c in word:
                if (1 << (ord(c) - ord("a"))) & bit == 0:
                    res -= 1
                    break
        return res
