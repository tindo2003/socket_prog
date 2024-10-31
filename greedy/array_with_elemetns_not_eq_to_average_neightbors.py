from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        # make sure the divsion is even-ish. 
        # for example, [1,2,3,4,5] -> [1,2,3] [4,5] and [1, 2, 3, 4] -> [1,2] [3,4]
        if l % 2 == 0:
            division = l // 2    
            l_nums = nums[0 : division]
            r_nums = nums[division : ]
        else:
            division = l // 2
            l_nums = nums[0 : division + 1]
            r_nums = nums[division + 1 : ]

        l_idx = 0
        r_idx = 0
        res = []
        while l_idx < len(l_nums) and r_idx < len(r_nums):
            res.append(l_nums[l_idx])
            l_idx += 1
            res.append(r_nums[r_idx])
            r_idx += 1
        if l_idx < len(l_nums):
            res.append(l_nums[l_idx])
        if r_idx < len(r_nums):
            res.append(r_nums[r_idx])
        return res



