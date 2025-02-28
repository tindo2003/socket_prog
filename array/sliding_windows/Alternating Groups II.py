from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[0 : k - 1])
        """
        once a sequence fails to maintain the alternating pattern at a certain index, any longer sequence containing that point is also invalid. 
        """
        l = 0
        res = 0
        for r in range(len(colors)):
            # if the invariant breaks
            if colors[r] == colors[r - 1]:
                l = r
            else:
                if r - l + 1 == k:
                    res += 1
                    l += 1
        return res
