from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    row = 0
    col = m - 1
    while (row >= 0 and col <= m-1):
      if matrix[row][col] == target:
        return True 
      elif matrix[row][col] < target:
        col -= 1
      else:
        row -= 1
    return False


def main():
  sol = Solution()
  matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
  target = 5
  res = sol.searchMatrix(matrix, target)
  print(res)

if __name__ == "__main__":
  main()
