from typing import List 

class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    n = len(matrix)
    for i in range(1, n):
      for j in range(n):
        # 3 choices
        directions = [-1, 0, 1]
        new_min = float("inf")
        for direction in directions:
          new_j = j + direction
          if new_j >= 0 and new_j < n:
            new_min = min(new_min, matrix[i-1][new_j])
        matrix[i][j] += new_min 
    return min(matrix[n-1])

def main():
  sol = Solution()
  matrix = [[-19,57],[-40,-5]]
  res = sol.minFallingPathSum(matrix)
  print(res)


if __name__ == "__main__":
  main()