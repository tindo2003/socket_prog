
from typing import List 

class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = []
    def helper(cur_num: int, cur_lst: List[int], cur_sum: int):
      if cur_sum == n and len(cur_lst) == k:
        res.append(cur_lst.copy())
        return 
      if cur_sum > n or len(cur_lst) > k:
        return 

      for num in range(cur_num + 1, 10):
        cur_lst.append(num)
        helper(num, cur_lst, cur_sum + num)
        cur_lst.pop()
    helper(0, [], 0)
    return res

def main():
  sol = Solution()
  res = sol.combinationSum3(3, 9)
  print(res)


if __name__ == "__main__":
  main()
