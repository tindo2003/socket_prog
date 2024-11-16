from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # PREFIX AND SUFFIX SUM tricks
        p_s = [0] * N
        cur_sum = 0 
        for idx, num in enumerate(nums):
            cur_sum += num
            p_s[idx] = cur_sum

        s_s = [0] * N
        cur_sum = 0
        for idx in range(N -1, -1, -1):
            num = nums[idx] 
            cur_sum += num
            s_s[idx] = cur_sum
        res = [0] * N

        for i in range(N):
            after_mult = N - i - 1
            tmp_pref = 0
            if i - 1 >= 0: tmp_pref = p_s[i-1]
            tmp_suf = 0
            if i + 1 < N: tmp_suf = s_s[i+1]
            res[i] = nums[i] * i - tmp_pref  + tmp_suf - nums[i] * after_mult
        return res