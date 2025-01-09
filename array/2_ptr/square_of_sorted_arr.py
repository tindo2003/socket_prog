from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = 0, N - 1
        res = [0] * N
        idx = N - 1
        while l <= r:
            square_left = nums[l] * nums[l]
            square_right = nums[r] * nums[r]
            if square_left > square_right:
                l += 1
                res[idx] = square_left
            else:
                res[idx] = square_right
                r -= 1
            idx -= 1
        return res
