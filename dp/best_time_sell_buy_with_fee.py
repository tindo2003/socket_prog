from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cache = {}
        def dfs(cur_idx, buy: bool) -> int: 
            if cur_idx >= len(prices): return 0
            if (cur_idx, buy) in cache:
                return cache[(cur_idx, buy)]
            if buy:
                pick = -prices[cur_idx] + dfs(cur_idx + 1, False)
                skip = dfs(cur_idx + 1, True) # skip this one and potentially buy the next one
                cache[(cur_idx, buy)] = max(pick, skip)
                return cache[(cur_idx, buy)]
            else:
                sell = prices[cur_idx] - fee + dfs(cur_idx + 1, True)
                skip = dfs(cur_idx + 1, False)
                cache[(cur_idx, buy)] = max(sell, skip) 
                return cache[(cur_idx, buy)]

        return dfs(0, True)