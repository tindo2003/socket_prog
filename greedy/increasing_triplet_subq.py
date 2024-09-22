from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left, middle, right = inf, inf, inf
        for num in nums:
            if num > middle: return True
            else:
                if num < left: 
                    left = num
                else: # num is not between current middle and current elft
                    middle = num 
        return False 