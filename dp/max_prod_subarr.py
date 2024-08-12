from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    prefix = 1
    suffix = 1
    res = float("-inf")
    for i in range(n):
      if prefix == 0: prefix = 1
      if suffix == 0: suffix = 1

      prefix *= nums[i]
      suffix *= nums[n-1-i]
      res = max(res, prefix)
      res = max(res, suffix)
    return res




def main():
  sol = Solution()
  nums = [2,3,-2,4]
  res = sol.maxProduct(nums)
  print(res)

if __name__ == "__main__":
  main()