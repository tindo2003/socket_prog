from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    my_set = set(wordDict)
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = True 
    for idx in range(n - 1, -1, -1):
      tmp = False
      for i in range(idx + 1, len(s) + 1):
        if s[idx:i] in my_set:
          tmp = tmp or dp[i]
      dp[idx] = tmp 
    return dp[0]

def main():
  sol = Solution()
  s = "abcd"
  d = ["a","abc","b","cd"]
  res = sol.wordBreak(s, d)
  print(res)

if __name__ == "__main__":
  main()