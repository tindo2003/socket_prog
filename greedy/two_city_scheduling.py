from typing import List
class Solution:    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
            new_arr = [(b-a, idx) for idx, (a,b) in enumerate(costs)]
            new_arr.sort(reverse=False)
            ans = 0
            N = len(costs)
            for i in range(N):
                idx = new_arr[i][1]
                if i < N // 2:
                    ans += costs[idx][1] 
                else:
                    ans += costs[idx][0]
            return ans 