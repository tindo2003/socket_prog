from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        l = 0
        my_set = set()
        for r in range(1, N):
            while l < r and nums[r] - nums[l] > k:
                l += 1
            if nums[r] - nums[l] == k and l != r:
                my_set.add((nums[l], nums[r]))
        return len(my_set)
