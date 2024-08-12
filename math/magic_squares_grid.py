from typing import List

class Solution:
  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    def check_magic_square(x: int, y: int) -> bool:
      my_set = set()
      for dx in range(3):
        for dy in range(3):
          nx = x + dx 
          ny = y + dy
          my_set.add(grid[nx][ny])
      if len(my_set) != 9:
        return False

      for dx in range(3):
        row_sum = 0
        nx = x + dx
        for dy in range(3):
          row_sum += grid[nx][y + dy]
        if row_sum != 15:
          return False 
      
      for dy in range(3):
        col_sum = 0 
        ny = y + dy 
        for dx in range(3):
          col_sum += grid[dx + x][ny]
        if col_sum != 15:
          return False 
      
      diag1 = 0 
      diag2 = 0 
      for d in range(3):
        diag1 += grid[x + d][y + d]
        diag2 += grid[x + 2 - d][y + d]
      if diag1 != 15 or diag2 != 15:
        return False 

      return True
    
    n = len(grid)
    m = len(grid[0])
    res = 0
    for i in range(n - 2):
      for j in range(m - 2):
        if check_magic_square(i, j):
          res += 1
    
    return res 

def main():
  sol = Solution()
  grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
  res = sol.numMagicSquaresInside()
  print(res)

if __name__ == "__main__":
  main()