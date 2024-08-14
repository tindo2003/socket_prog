from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        queue = [(sr, sc)]
        n = len(image), m = len(image[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        while queue:
            x, y = queue.pop(0)
            image[x][y] = color
            for dx, dy in directions:
                nx, ny = x + dx, y + dy 
                if 0 <= nx <= n and 0 <= ny <= m and image[nx][ny] == c and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return image



def main():
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr, sc, color = 1, 1, 2
    res = sol.floodFill()
    print(res)

if __name__ == "__main__":
    main()