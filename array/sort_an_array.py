from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       # merge sort
        def sort_arr(l, r) -> List[int]:
            if l == r: 
                return [nums[l]]
            mid = (l + r) // 2
            left = sort_arr(l, mid) 
            right = sort_arr(mid + 1, r)
            res = merge(left, right)
            return res
        
        def merge(arr1, arr2):
            out = []
            ptr1, ptr2 = 0, 0
            while ptr1 < len(arr1) and ptr2 < len(arr2):
                if arr1[ptr1] < arr2[ptr2]:
                    out.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    out.append(arr2[ptr2])
                    ptr2 += 1
            if ptr1 < len(arr1):
                out.extend(arr1[ptr1:])
            if ptr2 < len(arr2):
                out.extend(arr2[ptr2:])
            return out
        
        return sort_arr(0, len(nums) - 1)