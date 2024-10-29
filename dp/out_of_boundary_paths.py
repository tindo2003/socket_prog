from collections import defaultdict


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        my_dict = defaultdict(int)
        MOD = 10**9 + 7

        def recur(x, y, num_moves):
            if (x, y, num_moves) in my_dict:
                return my_dict[(x, y, num_moves)]
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if num_moves <= 0:
                return 0

            total = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                total = (total + recur(nx, ny, num_moves - 1)) % MOD

            my_dict[(x, y, num_moves)] = total
            return total

        return recur(startRow, startColumn, maxMove)
