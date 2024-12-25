from typing import List
from heapq import heappush, heappop


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Goal: Maximize the product of the sum of selected elements from nums1 and the smallest corresponding element in nums2.

        new_arr = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        new_arr.sort(key=lambda x: x[1], reverse=True)

        # Min heap to maintain the k largest elements from nums1.
        h = []
        total = 0  
        res = 0  

        for n1, n2 in new_arr:
            total += n1
            heappush(h, n1)

            if len(h) > k:
                tmp = heappop(h)
                total -= tmp

            # If the heap size is exactly k, calculate the product and update the result if it's the maximum so far.
            # The product is calculated using the current total from nums1 and the current n2 (the smallest in this subset of nums2).
            if len(h) == k:
                res = max(res, total * n2)

        return res
