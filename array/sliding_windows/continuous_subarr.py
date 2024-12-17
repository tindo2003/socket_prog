from typing import List 
from math import inf 

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        N = len(nums)
        cnt = 0
        mini = inf
        maxi = -inf
        for r in range(N):
            cur_ele = nums[r]
            mini = min(cur_ele, mini)
            maxi = max(cur_ele, maxi)
            if maxi - mini > 2:
                mini = cur_ele
                maxi = cur_ele
                d = r - l
                cnt += (d * (d + 1)) // 2

                l = r
                for new_l in range(r - 1, -1, -1):
                    if nums[new_l] - mini > 2 or maxi - nums[new_l] > 2:
                        break
                    l = new_l
                    mini = min(mini, nums[l])
                    maxi = max(maxi, nums[l])

                tmp_d = r - l
                cnt -= (tmp_d * (tmp_d + 1)) // 2

        d = r - l + 1
        cnt += (d * (d + 1)) // 2
        return cnt
