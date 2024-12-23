class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {"a", "e", "o", "i", "u"}
        res = 0
        l = 0
        cnt = 0
        for idx in range(k):
            if s[idx] in vowel_set:
                cnt += 1
        res = cnt
        for r in range(k, len(s)):
            if s[r] in vowel_set:
                cnt += 1
            if s[l] in vowel_set:
                cnt -= 1
            l += 1
            res = max(res, cnt)
        return res
