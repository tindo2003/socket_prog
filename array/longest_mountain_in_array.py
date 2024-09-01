from typing import List 
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        res = 0
        for top in range(1, N-1):
            if arr[top-1] < arr[top] and arr[top + 1] < arr[top]:   
                right_idx = top + 1
                while right_idx + 1 < N and arr[right_idx + 1] < arr[right_idx]:
                    right_idx += 1
                left_idx = top - 1
                while left_idx - 1 >= 0 and arr[left_idx - 1] < arr[left_idx]:
                    left_idx -= 1
                res = max(res, right_idx - left_idx + 1)
        return res