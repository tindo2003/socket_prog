from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def dfs(idx):
            if idx == 0:
                return [1]
            if idx == 1:
                return [1, 1]
            prev_lst = dfs(idx - 1)
            new_lst = [1] * (len(prev_lst) + 1)
            for i in range(1, len(new_lst) - 1):
                new_lst[i] = prev_lst[i - 1] + prev_lst[i]
            return new_lst

        return dfs(rowIndex)
