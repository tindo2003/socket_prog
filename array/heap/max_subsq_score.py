import heapq
from typing import List 

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # MAIN IDEA: build a min heap of k elements in nums1.
        # we sort first because we know that at the current element in nums2 is guaranteed to be the minimum
        h = []
        ans = 0
        combined = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        combined.sort(key=lambda x: x[1], reverse=True)
        
        running_sum = 0
        for x1, x2 in combined:
            heapq.heappush(h, x1)
            running_sum += x1
            if len(h) == k:
                ans = max(running_sum * x2, ans)
                popped = heapq.heappop(h)
                running_sum -= popped
        return ans