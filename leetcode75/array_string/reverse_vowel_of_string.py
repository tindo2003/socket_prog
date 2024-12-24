class Solution:
    def reverseVowels(self, s: str) -> str:

        N = len(s)
        vowel_set = {"A", "a", "E", "e", "I", "i", "o", "O", "u", "U"}
        s = list(s)
        l, r = 0, N - 1
        while 1:
            while l < N and s[l] not in vowel_set:
                l += 1
            while r >= 0 and s[r] not in vowel_set:
                r -= 1
            if l >= r:
                break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
