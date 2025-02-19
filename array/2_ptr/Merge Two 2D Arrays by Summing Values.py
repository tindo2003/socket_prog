from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            id1, num1 = nums1[ptr1]
            id2, num2 = nums2[ptr2]
            if id1 == id2:
                res.append([id1, num1 + num2])
                ptr1 += 1
                ptr2 += 1
            elif id1 < id2:
                res.append([id1, num1])
                ptr1 += 1
            else:
                res.append([id2, num2])
                ptr2 += 1

        if ptr1 < len(nums1):
            res.extend(nums1[ptr1:])
        if ptr2 < len(nums2):
            res.extend(nums2[ptr2:])
        return res
