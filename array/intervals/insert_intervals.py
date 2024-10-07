from typing import List 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # step 1: find the start time less than or equal than new start time, so we can insert there
        def binary_search(tgt):
            l = 0 
            r = len(intervals) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                start, end = intervals[mid]
                if start == tgt:
                    return mid 
                elif start < tgt: 
                    l = mid + 1
                    ans = mid 
                else:
                    r = mid - 1
            return ans 
        idx = binary_search(newInterval[0])
        new_lst = intervals[0:idx+1] + [newInterval] + intervals[idx+1:]
        # now it is time to merge 
        stack = []
        for item in new_lst:
            # current start time greater than previous end time
            if not stack or stack[-1][1] < item[0]:
                stack.append(item)
            else:
                old_start, old_end = stack.pop()
                stack.append([old_start, max(old_end, item[1])])
        return stack 
