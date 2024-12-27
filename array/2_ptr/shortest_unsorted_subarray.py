from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        another_num = sorted(nums)
        N = len(nums)

        for l in range(N):
            cur = nums[l]
            if cur != another_num[l]:
                break
        for r in range(N - 1, -1, -1):
            cur = nums[r]
            if cur != another_num[r]:
                break
        if r <= l:
            return 0
        return r - l + 1
