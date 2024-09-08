from typing import List 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = []
        for item in intervals:
            if not stack or stack[-1][1] < item[0]:
                stack.append(item)
            else:
                old_start, old_end = stack.pop()
                stack.append([old_start,  max(old_end, item[1])])
        return stack