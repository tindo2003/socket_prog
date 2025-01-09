from collections import defaultdict


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # all possible dr,dc from one location
        directions = [
            [-2, -1],
            [-2, 1],
            [-1, -2],
            [-1, 2],
            [1, -2],
            [1, 2],
            [2, -1],
            [2, 1],
        ]
        my_dict = defaultdict(list)
        for r in range(n):
            for c in range(n):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        my_dict[(r, c)].append((nr, nc))

        cache = {}

        def dfs(r, c, k):
            if k <= 0:
                return 1
            if (r, c, k) in cache:
                return cache[(r, c, k)]
            total = 0
            for nr, nc in my_dict[(r, c)]:
                total += 1 / 8 * dfs(nr, nc, k - 1)
            cache[(r, c, k)] = total
            return total

        return dfs(row, column, k)
