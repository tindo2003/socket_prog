from math import inf


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "ueoai"
        my_dict = {"u": 4, "e": 3, "o": 2, "a": 1, "i": 0}
        state = 0
        pos = [inf] * 32
        pos[state] = -1
        res = 0
        for idx, c in enumerate(s):
            # only update state when a vowel is encountered
            if c in vowels:
                state ^= 1 << my_dict[c]
                # update pos only first occurence
                if idx < pos[state]:
                    pos[state] = idx
            # we can always extend
            res = max(res, idx - pos[state])
        return res
