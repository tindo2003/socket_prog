from typing import List
import heapq 

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
        for idx, val in enumerate(nums):
            heapq.heappush(h, (val, idx))
        while k:
            x, i = h[0]
            heapq.heapreplace(h, (x*multiplier, i))
            k -= 1
        
        for val, i in h:
            nums[i] = val 
        return nums