from typing import List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_l = []
        p_r = deque([])
        s_l = s_r = 0
        N = len(nums)
        for i in range(N):
            s_l *= nums[i]
            p_l.append(s_l)
        for i in range(N - 1, -1, -1):
            s_r *= nums[i]
            p_r.appendleft(s_r)
        for i in range(N):
            tmp = 1
            if i - 1 >= 0:
                tmp *= p_l[i - 1]
            if i + 1 < N:
                tmp *= p_r[i + 1]
            nums[i] = tmp
        return nums
