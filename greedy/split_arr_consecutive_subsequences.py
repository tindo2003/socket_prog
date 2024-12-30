from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        H = defaultdict(list)
        for num in nums:
            if H[num - 1]:
                shortest_length = heappop(H[num - 1])
                heappush(H[num], shortest_length + 1)
            else:
                heappush(H[num], 1)
        return all(item >= 3 for k, v in H.items() for item in v)
