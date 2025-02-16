from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        my_set = set()
        freq = Counter(s)
        N = len(s)
        for m in range(N):
            freq[s[m]] -= 1
            for item in my_set:
                if freq[item] > 0:
                    res.add(f"{item}{s[m]}{item}")
            my_set.add(s[m])
        return len(res)
