from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while stack:
                idx = stack[-1]
                if t >= temperatures[idx]:
                    stack.pop()
                else:
                    break
            if stack:
                res[i] = stack[-1]
            stack.append(i)

        tmp = [v - i if v != -1 else 0 for i, v in enumerate(res)]
        return tmp
