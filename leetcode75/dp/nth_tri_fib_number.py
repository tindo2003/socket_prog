from collections import defaultdict


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)

        def dfs(cur):
            if cur == 0:
                return 0
            if cur == 1:
                return 1
            if cur == 2:
                return 1
            if cur in memo:
                return memo[cur]
            res = dfs(cur - 2) + dfs(cur - 1) + dfs(cur - 3)
            memo[cur] = res
            return res

        return dfs(n)
