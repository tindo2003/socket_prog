from typing import List 
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [-1, 0], [0,-1], [1,0]]
        x, y = 0, 0
        direction = 0
        obs = set()
        for i, j in obstacles:
          obs.add((i, j))
        res = float("inf") 
        for c in commands:
            if c == -2:
                direction = (direction + 1) % 4
            elif c == -1:
                direction = (direction + 3) % 4
            else:
                dx, dy = directions[direction]
                
                for _ in range(c):
                    nx, ny = x + dx, y + dy 
                    #
                    if (nx, ny) in obs:
                        break 
                
                    x, y = nx, ny 
                res = max(res, x**2 + y**2)
        return res 