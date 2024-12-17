from typing import List 

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        def f(target) -> bool:
            i = 0
            tmp = 0
            while i < len(nums) - 1:
                if (nums[i + 1] - nums[i]) <= target:
                    tmp += 1
                    i += 1
                if tmp == p:
                    return True
                i += 1
            return False

        nums.sort()
        l, r = 0, 10**9
        res = -1
        while l <= r:
            middle = (l + r) // 2
            # question to answer
            if f(middle):
                res = middle
                r = middle - 1
            else:
                l = middle + 1
        return res
