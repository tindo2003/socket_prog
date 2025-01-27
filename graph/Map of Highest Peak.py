class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        q = deque([])
        res = [[-1] * m for _ in range(n)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(n):
            for c in range(m):
                if isWater[r][c] == 1:
                    res[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and res[nr][nc] < 0:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))
        return res
