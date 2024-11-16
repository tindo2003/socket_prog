from typing import List 
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        N = len(shifts)
        for i in range(N - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        res = []
        for idx in range(len(s)):
            c = s[idx]
            offset = ord("a")
            new_idx = (ord(c) - offset + (shifts[idx])) % 26
            new_char = chr(new_idx + offset)
            res.append(new_char)
        return "".join(res)
