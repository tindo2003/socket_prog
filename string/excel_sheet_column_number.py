class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lst = list(columnTitle)
        multiplier = len(columnTitle) - 1
        m = {chr(i + 65): (i + 1) for i in range(26)}
        res = 0
        for c in lst:
            offset = m[c]
            res += (26**multiplier) * offset
            multiplier -= 1
        return res
