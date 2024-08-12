class Solution:
  def minimumSteps(self, s: str) -> int:
    res = 0
    num_ones = 0
    n = len(s)
    for i in range(n):
      if s[i] == '1':
        num_ones += 1
      elif s[i] == '0':
        res += num_ones
    return res
     

def main():
  sol = Solution()
  s = "100"
  res = sol.minimumSteps(s)
  print(res)

if __name__ == "__main__":
  main()
