from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        res = 0
        for idx, g in enumerate(gain):
            s += g
            gain[idx] = s
            res = max(res, gain[idx])
        return res
