from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_to(num) -> int:
            res = 0
            start = 0
            if num == 0: return mapping[0]
            while num:
                div, remain = divmod(num, 10)
                num = div
                new_num = mapping[remain] 
                res += 10 ** start * new_num 
                start += 1
            return res
        tmp = []
        for idx, num in enumerate(nums):
            tmp.append((map_to(num), idx))
        tmp.sort()
        return [nums[item[1]] for item in tmp]