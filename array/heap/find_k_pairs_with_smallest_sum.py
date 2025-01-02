from typing import List
from heapq import heappop, heappush


class Solution:
    # This is very very similar to kth smallest num in sorted matrix
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        h = []
        res = []
        for i, num in enumerate(nums1):
            s = num + nums2[0]
            # store the sum, the corresponding pair that makes up the sum, and the index of the second element.
            heappush(h, (s, num, nums2[0], 0))
        while k > 0:
            _, v1, v2, cur_idx = heappop(h)
            res.append([v1, v2])
            if cur_idx + 1 < len(nums2):
                s = v1 + nums2[cur_idx + 1]
                heappush(h, (s, v1, nums2[cur_idx + 1], cur_idx + 1))
            k -= 1
        return res
