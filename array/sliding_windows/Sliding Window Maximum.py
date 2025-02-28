from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque([])
        l = 0
        res = []
        for r in range(len(nums)):
            # pretty much a stack lol
            while d and nums[r] > d[-1][0]:
                d.pop()
            d.append((nums[r], r))
            if r - l + 1 == k:
                res.append(d[0][0])
                if l == d[0][1]:
                    d.popleft()
                l += 1
        return res
