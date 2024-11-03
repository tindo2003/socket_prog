from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # the differenrece betqeen 2 consecutive is always the smallest
        nums.sort()
        res = []
        if len(nums) % 3 != 0: return []
        for idx in range(0, len(nums), 3):
            d1 = nums[idx + 1] - nums[idx]
            d2 = nums[idx + 2] - nums[idx + 1]
            d3 = nums[idx + 2] - nums[idx]
            if d1 <= k and d2 <= k and d3 <= k:
                res.append(nums[idx:idx+3])
            else: return []
        return res
