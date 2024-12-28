from collections import Counter
from heapq import heappush, heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        h = []
        for k, v in freq.items():
            heappush(h, (-v, k))
        res = []
        while h:
            v, k = heappop(h)
            res.append(k * (-v))
        return "".join(res)
