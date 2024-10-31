from typing import List
from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0 
        freq_counter = Counter(nums)
        
        for val, freq in freq_counter.items():
            if freq == 1: return -1
            div, remain = divmod(freq, 3)
            if remain == 0:
                res += div
            elif remain == 1:
                res += (div - 1) + 2 
            elif remain == 2:
                res += div + 1

        return res