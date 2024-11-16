from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        l, r = 0, N - 1
        for idx in range(N - 1, 0, -1):
            prev_ele = arr[idx - 1]
            cur_ele = arr[idx]
            if prev_ele > cur_ele:
                break
            r -= 1
        res = r
        while l < r:
            while r < N and arr[r] < arr[l]:
                r += 1
            res = min(res, r - l - 1)
            if l + 1 >= N or arr[l + 1] < arr[l]:
                break
            l += 1
        return res
