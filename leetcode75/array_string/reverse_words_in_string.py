import re


# the trick is regular expression
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = re.split(r"\s+", s)
        N = len(s)
        l, r = 0, N - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
        return " ".join(s)
