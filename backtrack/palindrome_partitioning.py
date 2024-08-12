from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
      res = []
      def helper(cur_str: str, cur_lst: List[str]):
        if not cur_str:
          res.append(cur_lst.copy())
        for i in range(len(cur_str)):
          palindrome = palindrome_checker(cur_str, i)
          if palindrome:
            cur_lst.append(cur_str[0:i+1])
            helper(cur_str[i + 1:], cur_lst)
            cur_lst.pop()
        
      def palindrome_checker(cur_str: str, cur_idx: int):
        l = 0
        r = cur_idx
        while l <= r:
          if cur_str[l] != cur_str[s]:
            return False 
          l += 1
          r -= 1
        return True
      
      helper(s, [])
      return res
