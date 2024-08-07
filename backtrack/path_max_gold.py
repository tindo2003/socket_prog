from typing import List 

class Solution:
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    '''
    1) You can't visit the same cell more than once.
    2) Never visit a cell with 0 gold.
    '''
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

 
    n, m = len(grid), len(grid[0])
    max_gold = 0

    def dfs(i: int, j: int, visited: set, cur_sum: int) -> None:
      nonlocal max_gold
      max_gold = max(max_gold, cur_sum)

      for dx, dy in directions:
        new_i, new_j = i + dx, j + dy
        if (0 <= new_i < n and 0 <= new_j < m and 
          (new_i, new_j) not in visited and grid[new_i][new_j] != 0):
          visited.add((new_i, new_j))
          dfs(new_i, new_j, visited, cur_sum + grid[new_i][new_j])
          visited.remove((new_i, new_j))

    for i in range(n):
      for j in range(m):
        if grid[i][j] != 0:
          dfs(i, j, {(i, j)}, grid[i][j])

    return max_gold

def main():
  sol = Solution()
  grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
  res = sol.getMaximumGold(grid)
  print(res)

if __name__ == "__main__":
  main()