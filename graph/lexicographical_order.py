from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(cur_num: int) -> int:
            if cur_num != 0:
                for i in range(10):
                    tmp_num = cur_num * 10 + i 
                    if tmp_num > n: break
                    if tmp_num <= n:
                        res.append(tmp_num)
                        dfs(tmp_num)
            else:
                for i in range(1, 10):
                    tmp_num = cur_num * 10 + i 
                    if tmp_num > n: break
                    if tmp_num <= n:
                        res.append(tmp_num)
                        dfs(tmp_num)
        dfs(0)
        return res 
