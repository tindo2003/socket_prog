from collections import Counter
from typing import List 

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ones, twos, threes = Counter(), Counter(), Counter()
        for num in nums:
            # print(ones, twos, threes)
            prev_num = num - 1
            if ones[prev_num] > 0:
                ones[prev_num] -= 1
                twos[num] += 1
                continue
            if twos[prev_num] > 0:
                twos[prev_num] -= 1
                threes[num] += 1
                continue
            # the invariant is keep expanding the long subsequence if possible
            if threes[prev_num] > 0:
                threes[prev_num] -= 1
                threes[num] += 1
                continue
            ones[num] += 1
        if ones.total() > 0 or twos.total() > 0:
            return False
        return True
