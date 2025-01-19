from typing import List
from collections import defaultdict


class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        # THINK ABOUT SLIDING WINDOW OF FIXED SIZE X. sort queries and sort logs helps
        logs.sort(key=lambda x: x[1])
        N = len(logs)
        my_dict = defaultdict(int)
        queries = sorted(list(enumerate(queries)), key=lambda x: x[1])

        res = [0] * len(queries)
        l = r = 0
        for idx, upper_bound in queries:
            lower_bound = upper_bound - x

            while r < N and logs[r][1] <= upper_bound:
                my_dict[logs[r][0]] += 1
                r += 1

            while l < N and logs[l][1] < lower_bound:
                my_dict[logs[l][0]] -= 1
                if my_dict[logs[l][0]] == 0:
                    del my_dict[logs[l][0]]
                l += 1

            res[idx] = n - len(my_dict.keys())
        return res
