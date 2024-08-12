from typing import List

class Solution:
  def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    # subarrays of length at most k
    n = len(arr)
    dp = [0] * (n + 1)
    for cur_idx in range(n - 1, -1, -1):
      best_val = 0
      max_val = 0
      tmp_len = 1
      for i in range(cur_idx, min(n, cur_idx + k), 1):
        max_val = max(max_val, arr[i])
        tmp = max_val * tmp_len
        cur = tmp + dp[i + 1]
        best_val = max(best_val, cur)
        tmp_len += 1
      dp[cur_idx] = best_val
    return dp[0]

def main():
  sol = Solution()
  arr = [1,4,1,5,7,3,6,1,9,9,3]
  k = 4
  res = sol.maxSumAfterPartitioning(arr, k)
  print(res)

if __name__ == "__main__":
   main()
