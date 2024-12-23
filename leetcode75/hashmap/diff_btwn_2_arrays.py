from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        lst1 = list(filter(lambda x: x not in set_2, set_1))
        lst2 = list(filter(lambda x: x not in set_1, set_2))
        return lst1, lst2
