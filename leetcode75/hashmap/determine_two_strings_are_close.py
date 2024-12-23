from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        a = Counter(word1)
        b = Counter(word2)
        a_vals = list(a.values())
        b_vals = list(b.values())
        a_keys = list(a.keys())
        b_keys = list(b.keys())
        return sorted(a_vals) == sorted(b_vals) and sorted(a_keys) == sorted(b_keys)
