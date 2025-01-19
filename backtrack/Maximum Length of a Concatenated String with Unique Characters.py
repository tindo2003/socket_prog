from typing import List
from collections import Counter


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        res = 0

        def dfs(idx, lst):
            nonlocal res
            if idx >= N:
                cur_str = "".join(lst)
                freq = Counter(cur_str)
                good = True
                for v in freq.values():
                    if v > 1:
                        good = False
                        break
                if good:
                    res = max(res, len(cur_str))
                return
            lst.append(arr[idx])
            dfs(idx + 1, lst)
            lst.pop()
            dfs(idx + 1, lst)

        dfs(0, [])
        return res
