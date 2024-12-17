from collections import Counter 
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)

        h = []
        res = ""
        for k, v in c.items():
            heapq.heappush(h, (-ord(k), v))

        while h:
            v, freq = heapq.heappop(h)
            res += chr(-v) * min(freq, repeatLimit)
            if freq > repeatLimit:
                if not h:
                    break
                v1, freq1 = heapq.heappop(h)
                res += chr(-v1)
                heapq.heappush(h, (v, freq - repeatLimit))
                if freq1 - 1 > 0:
                    heapq.heappush(h, (v1, freq1 - 1))

        return res
