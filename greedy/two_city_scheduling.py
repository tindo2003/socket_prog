from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [item[0] - item[1] for item in costs]
        diff_lst = list(enumerate(diff))
        diff_lst.sort(key=lambda x: x[1])
        cnt = 0
        for idx, item in enumerate(diff_lst):
            i, _ = item
            if idx < len(costs) // 2:
                cnt += costs[i][0]
            else:
                cnt += costs[i][1]
        return cnt
