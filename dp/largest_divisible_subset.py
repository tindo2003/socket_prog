from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
         
        # largest subset ending with i
        dp = [1] * n 
        prev = [-1] * n 
        
        max_val = -inf 
        max_idx = 0

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j 

            if dp[i] > max_val:
                max_val = dp[i]
                max_idx = i 
        
        ans = []
        while(max_idx != -1):
            ans.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        ans.reverse()
        return ans