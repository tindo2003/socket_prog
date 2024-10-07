class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        # look for idx <= tgt
        def binary_search(tgt):
            l = 0
            r = len(potions) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] < tgt:
                    l = mid + 1
                    res = mid
                else:
                    r = mid - 1
            return res
        res = []
        for spell in spells:
            wanted_number = math.ceil(success / spell)
            idx = binary_search(wanted_number)
            res.append(len(potions) - 1 - idx)
        return res
