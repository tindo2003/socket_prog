class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(start):
            res = 0
            q = [start]
            my_set = set([start])
            while q:
                r, c = q.pop(0)
                res += grid[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < n
                        and 0 <= nc < m
                        and grid[nr][nc] != 0
                        and (nr, nc) not in my_set
                    ):
                        my_set.add((nr, nc))
                        q.append((nr, nc))
            return res

        ans = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] != 0:
                    tmp = bfs((r, c))
                    ans = max(ans, tmp)
        return ans
