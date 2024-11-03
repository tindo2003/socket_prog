from typing import List
from math import inf
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # sort by age first, then by score
        combined = [(ages[idx], scores[idx]) for idx in range(len(scores))]
        sorted_lst = sorted(combined, key=lambda x: (x[0], x[1]))
        values = [item[1] for item in sorted_lst]
        #longest increasing subsequence
        cache = {}
        def dfs(cur_idx: int):
            if cur_idx in cache: return cache[cur_idx]
            res = values[cur_idx]
            for new_idx in range(cur_idx + 1, len(scores)):
                if values[new_idx] >= values[cur_idx]:
                    res = max(res, values[cur_idx] + dfs(new_idx))
            cache[cur_idx] = res
            return cache[cur_idx]
        val = -inf
        for i in range(len(scores)):
            val = max(val, dfs(i))
        return val
