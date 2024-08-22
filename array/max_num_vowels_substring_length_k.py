class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0 
        N = len(s)
        res = -inf
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        for idx in range(k):
            if s[idx] in vowel_set:
                count += 1
        res = max(res, count)
        for r in range(k, N):
            if s[l] in vowel_set:
                count -= 1
            if s[r] in vowel_set:
                count += 1
            l += 1
            res = max(res, count)
        return res