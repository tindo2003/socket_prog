from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        for idx in range(n-1, -1, -1):
            cur_ele = temperatures[idx]
            while stack:
                top = stack[-1]
                if cur_ele > temperatures[top]:
                    stack.pop()
                    continue 
                if cur_ele <= temperatures[top]:
                    break 
            if not stack:
                temperatures[idx] = -1
            else:
                temperatures[idx] = stack[-1]
        return temperatures
