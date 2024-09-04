from typing import List 
class Solution:
  # union find
  def equationsPossible(self, equations: List[str]) -> bool:
    parents = [i for i in range(26)]
    def find_parent(x):
      while parents[x] != x:
        x = parents[x]
      return x
    
    for equation in equations:
      x, sign, y = equation[0], equation[1:3], equation[3]
      x = ord(x) - 97
      y = ord(y) - 97
      if sign == "==":
        parents[find_parent(y)] = find_parent(x)

    for equation in equations:
      x, sign, y = equation[0], equation[1:3], equation[3]
      x = ord(x) - 97
      y = ord(y) - 97
      if sign == "!=":
        if find_parent(x) == find_parent(y):
          return False 
    return True

def main():
  sol = Solution()
  equations = ["b==a","a==b"]
  res = sol.equationsPossible(equations)
  print(res)

if __name__ == "__main__":
  main()