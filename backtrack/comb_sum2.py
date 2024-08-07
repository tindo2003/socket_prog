from typing import List
import argparse


class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    '''
    - Each number in candidates may only be used once in the combination.
    - The solution set must not contain duplicate combinations.
    '''
    candidates = sorted(candidates)
    res = []
    def helper(cur_idx: int, cur_sum: int, cur_lst: List[int]) -> None:
      if cur_sum == target:
        res.append(cur_lst.copy())
        return
      if cur_sum > target:
        return
      
      prev = -1
      for new_idx in range(cur_idx + 1, len(candidates)):
        new_ele = candidates[new_idx]
        if new_ele == prev:
          continue 
        prev = new_ele
        cur_lst.append(new_ele)
        helper(new_idx, cur_sum + new_ele, cur_lst)
        cur_lst.pop()
    helper(-1, 0, [])
    return res
  
def main():
  parser = argparse.ArgumentParser(description='Find combinations that sum to a target.')
  parser.add_argument('--candidates', type=int, nargs='+', required=True, 
                      help='List of candidate numbers')
  parser.add_argument('--target', type=int, required=True, 
                      help='Target sum')
  
  args = parser.parse_args()
  sol = Solution()
  res = sol.combinationSum2(candidates=args.candidates, target=args.target)
  print(res)

if __name__ == "__main__":
    main()