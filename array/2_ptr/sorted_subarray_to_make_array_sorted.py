from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        n = len(arr)
        res = 0
        r = n - 1
        while r - 1 >= 0 and arr[r - 1] <= arr[r]:
            r -= 1
        res = max(res, n - r)

        while l < r:
            # move right ptr to the right. because we already exhausted going to the left. we know left ele can only increase from here
            while r < n and arr[r] < arr[l]:
                r += 1
            if r >= n:
                break

            res = max(res, l + 1 + n - r)
            if l + 1 < n and arr[l + 1] < arr[l]:
                break
            l += 1

        l = 0
        while l + 1 < n and arr[l + 1] >= arr[l]:
            l += 1
        res = max(res, l + 1)
        return n - res
