from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # go straight down numerator/(n1/n2)
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{str(nums[1])}"
        my_str = "/".join(list(map(str, nums[1:])))
        return f"{nums[0]}/({my_str})"
