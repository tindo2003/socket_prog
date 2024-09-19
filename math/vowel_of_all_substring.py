class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        my_set = set(['a', 'o', 'u', 'e', 'i'])
        N = len(word)
        for i, val in enumerate(word):
            if val in my_set:
                res += (i + 1) * (N - i)
        return res