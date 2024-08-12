from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
      # the grid is connected if we only have one island
      pass

def main():
   sol = Solution()
   grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
   res = sol.minDays(grid)
   print(res)

if __name__ == "__main__":
   main()
