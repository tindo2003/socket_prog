from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        llen = len(str(low))
        linitial = int(str(low)[0])
        tmp = []
        res = 0
        linitial_cpy = linitial
        while res <= high:
            if res >= low:
                tmp.append(res)
            res = 0
            start = 0
            if linitial_cpy + llen > 10:
                llen += 1
                linitial_cpy = 1
            for i in range(llen - 1, -1, -1):
                res += 10**start * (linitial_cpy + i)
                start += 1
            linitial_cpy += 1
        return tmp
