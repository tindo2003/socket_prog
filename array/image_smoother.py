from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        N, M = len(img), len(img[0])
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
            [-1, -1],
            [1, 1],
            [-1, 1],
            [1, -1],
        ]
        new_img = [[0] * M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                s = img[r][c]
                cnt = 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M:
                        s += img[nr][nc]
                        cnt += 1
                avg = s // cnt
                new_img[r][c] = avg
        return new_img
