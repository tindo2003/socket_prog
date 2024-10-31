from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        my_set = set(nums)
        n = len(nums)
        res = []
        def dfs(cur_lst):
            nonlocal n
            if len(cur_lst) == n:
                tmp_str = "".join(cur_lst)
                if tmp_str not in nums: 
                    return tmp_str
                else: 
                    return 
            cur_lst.append("0")
            res1 =  dfs(cur_lst)
            cur_lst.pop()
            cur_lst.append("1")
            res2 = dfs(cur_lst)
            cur_lst.pop()
            if res1: return res1
            if res2: return res2
            return
        return dfs([])
