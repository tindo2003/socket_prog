from collections import deque
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lst_l = []
        lst_r = deque([])
        s_l = s_r = 0
        for idx in range(len(nums)):
            s_l += nums[idx]
            lst_l.append(s_l)

        for idx in range(len(nums) - 1, -1, -1):
            s_r += nums[idx]
            lst_r.appendleft(s_r)

        for idx in range(len(nums)):
            if lst_l[idx] == lst_r[idx]:
                return idx

        return -1
