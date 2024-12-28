from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        num_open = num_close = n
        res = []

        def dfs(cur_open, cur_close, cur_str):
            if cur_close >= n:
                res.append(cur_str)
                return
            if cur_open > cur_close:
                if cur_open < n:
                    dfs(cur_open + 1, cur_close, cur_str + "(")
                dfs(cur_open, cur_close + 1, cur_str + ")")
            else:
                dfs(cur_open + 1, cur_close, cur_str + "(")

        dfs(0, 0, "")
        return res
