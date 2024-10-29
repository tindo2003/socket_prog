from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        first_instance_of_1 = (-1, -1)
        found = False
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    first_instance_of_1 = (r, c)
                    found = True
                    break
            if found:
                break
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = [first_instance_of_1]
        first_island = set([first_instance_of_1])
        while q:
            x, y = q.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    nx >= 0
                    and nx < N
                    and ny >= 0
                    and ny < M
                    and (nx, ny) not in first_island
                    and grid[nx][ny] != 0
                ):
                    q.append((nx, ny))
                    first_island.add((nx, ny))
        best = {}

        for x, y in first_island:
            best[(x, y)] = 0

        layer = list(first_island)
        res_lst = []
        cnt = 1
        while True:
            cnt += 1
            new_layer = []
            for x, y in layer:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        nx >= 0
                        and nx < N
                        and ny >= 0
                        and ny < M
                        and (nx, ny) not in best
                    ):
                        if grid[nx][ny] != 1:
                            best[(nx, ny)] = best[(x, y)] + 1
                            new_layer.append((nx, ny))
                        else:
                            res_lst.append(best[(x, y)])
            layer = new_layer
            if not layer:
                break

        return min(res_lst)
