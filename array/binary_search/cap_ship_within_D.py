from typing import List 

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = inf
        n = len(weights)
        while l <= r:
            mid = (l + r) // 2
            
            total_days = 0 
            cur_weight = 0        
            for idx in range(n):
                if cur_weight + weights[idx] > mid:
                    total_days += 1
                    cur_weight = weights[idx]
                else:
                    cur_weight += weights[idx]
            total_days += 1

            if total_days <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res 
    