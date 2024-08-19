
# 692 (harder version of 347)
from collections import defaultdict
from typing import List

class HeapItem:
    def __init__(self, word: str, count: str) -> None:
        self.word = word
        self.count = count

    def __lt__(self, to_compare) -> bool:
        if self.count == to_compare.count:
            # lexigrapphy lesser word have priority since bigger word are viewed as "less than" 
            return self.word > to_compare.word

        return self.count < to_compare.count

from collections import Counter, heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        heap = []
        for key, val in word_counts:
            item = HeapItem(key, val)
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        while heap:
            popped = heapq.heappop()
            ans.append(popped)
        return ans[::-1]

