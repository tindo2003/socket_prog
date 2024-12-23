from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        my_set = set(counter.values())
        return len(my_set) == len(counter)
