from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        N = len(arr)
        arr[0] = 1
        res = arr[0]
        for i in range(1, N):
            prev_ele = arr[i-1]
            cur_ele = arr[i]
            if cur_ele >= prev_ele + 1:
                res = max(res, prev_ele + 1)
                arr[i] = prev_ele + 1
        return res
        