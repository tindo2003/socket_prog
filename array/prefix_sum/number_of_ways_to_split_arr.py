from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sl = []
        csl = csr = 0
        N = len(nums)
        sr = [0] * N
        for num in nums:
            csl += num
            sl.append(csl)
        for idx in range(N - 1, -1, -1):
            num = nums[idx]
            csr += num
            sr[idx] = csr
        cnt = 0
        for i in range(N - 1):
            if sl[i] >= sr[i + 1]:
                cnt += 1
        return cnt
