import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []
        cnt = 0
        while cnt < k:
            res.append(sorted_freq[cnt][0])
            cnt += 1
        return res
