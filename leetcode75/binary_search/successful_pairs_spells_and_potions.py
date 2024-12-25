from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        N_p = len(potions)

        def binary_search(tgt) -> int:
            l, r = 0, N_p - 1
            idx = -1
            while l <= r:
                middle = (l + r) // 2
                if tgt <= potions[middle]:
                    idx = middle
                    r = middle - 1
                else:
                    l = middle + 1
            return idx

        res = []
        for s in spells:
            cnt = binary_search(success / s)
            if cnt == -1:
                res.append(0)
            else:
                res.append(N_p - cnt)
        return res
