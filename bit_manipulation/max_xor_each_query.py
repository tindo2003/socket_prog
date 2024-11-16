from typing import List 
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
       # we want k to be inverse of the cur product because 1 xor 0 = 1 and 0 xor 1 = 1. and we want all to be 1
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        N = len(nums)
        for i in range(1, N):
            prefix[i] = prefix[i-1] ^ nums[i]
        mask = (1 << maximumBit) - 1 # all 1's
        ans = [0] * N
        for i in range(N):
            pref = prefix[N - 1 - i]
            ans[i] = pref ^ mask # finding the inverse. xor with all 1s will give the inverse of a number. 
        return ans
        
    