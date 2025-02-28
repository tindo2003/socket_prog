from math import inf


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = inf
        n = len(blocks)
        cnt = 0
        for r in range(n):
            if blocks[r] != "B":
                cnt += 1
            if r - l + 1 == k:
                res = min(res, cnt)
                if blocks[l] == "W":
                    cnt -= 1
                l += 1
        return res
