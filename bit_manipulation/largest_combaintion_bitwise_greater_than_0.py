from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # The longest combination will be given by the numbers that have 1 on the same position.
        count = [0] * 25
        for cand in candidates:
            for i in range(25):
                tmp = cand & (1 << i)
                if tmp > 0: count[i] += 1

        return max(count)