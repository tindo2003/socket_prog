from heapq import heappop, heappush
from typing import List
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        res = []
        h = []
        for k, f in freq.items():
            heappush(h, (-f, k))

        while h:
            freq, key = heappop(h)
            res.append(key)
            if not h:
                break
            freq1, key1 = heappop(h)
            res.append(key1)
            if freq + 1 < 0:
                heappush(h, (freq + 1, key))
            if freq1 + 1 < 0:
                heappush(h, (freq1 + 1, key1))
        return res
