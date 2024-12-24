from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        for idx, x in enumerate(candies):
            if x + extraCandies >= max_candies:
                candies[idx] = True
            else:
                candies[idx] = False
        return candies
