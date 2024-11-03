class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur = [float(poured)]
        for r in range(1, query_row + 1):
            nxt = [0] * (r + 1)
            for c in range(r):
                overflow_amnt = max((cur[c] - 1) / 2, 0)
                nxt[c] += overflow_amnt
                nxt[c + 1] += overflow_amnt
            cur = nxt
            
        return min(cur[query_glass], 1)

