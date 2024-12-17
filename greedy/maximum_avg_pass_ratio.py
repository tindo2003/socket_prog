from typing import List 
import heapq 

class HeapItem:
    def __init__(self, p, n):
        self.p = p
        self.n = n

    def __lt__(self, other):
        cur_gain = ((self.p + 1) / (self.n + 1)) - (self.p / self.n)
        other_gain = ((other.p + 1) / (other.n + 1)) - (other.p / other.n)
        return cur_gain > other_gain

    def __str__(self):
        return f"{self.p}, {self.n}"


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for p, n in classes:
            heapq.heappush(h, HeapItem(p, n))
        while extraStudents > 0 and h:
            top = heapq.heappop(h)
            p, n = top.p, top.n
            heapq.heappush(h, HeapItem(p + 1, n + 1))
            extraStudents -= 1
        res = sum([item.p / item.n for item in h])
        res /= len(classes)
        return res
