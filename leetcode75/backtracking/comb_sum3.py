from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(cur_n, cur_sum, lst, cnt):
            if cnt >= k:
                if cur_sum == n:
                    res.append(lst.copy())
                else:
                    return
            if cur_sum > n:
                return

            for new_n in range(cur_n + 1, 10):
                lst.append(new_n)
                dfs(new_n, cur_sum + new_n, lst, cnt + 1)
                lst.pop()

        dfs(0, 0, [], 0)
        return res
