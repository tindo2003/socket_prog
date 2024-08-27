from typing import List 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        N = len(coins)
        cache = {}

        def helper(idx, cur_sum):
            if cur_sum > amount:
                return -1
            if cur_sum == amount:
                return 0
            if idx >= N:
                if cur_sum != amount:
                    return -1
                else:
                    return 0
            if (idx, cur_sum) in cache:
                return cache[(idx, cur_sum)]
            
            pick = helper(idx, cur_sum + coins[idx]) 
            unpick = helper(idx + 1, cur_sum)


            if pick == -1:
                cache[(idx, cur_sum)] = unpick
                return unpick
            if unpick == -1:
                cache[(idx, cur_sum)] = pick + 1
                return pick + 1
            
            cache[(idx, cur_sum)] = min(pick + 1, unpick)        
            return cache[(idx, cur_sum)]
        
        return helper(0, 0)