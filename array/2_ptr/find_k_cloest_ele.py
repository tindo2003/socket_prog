from typing import List 
from bisect import bisect
from collections import deque 
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        r = bisect.bisect(arr, x)
        l = r - 1
        res = deque()

        while l >= 0 and r < N and k > 0:
            left_diff = x - arr[l]
            right_diff = arr[r] - x
            if left_diff <= right_diff:
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1

        while k > 0:
            if l >= 0:
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        return list(res)
