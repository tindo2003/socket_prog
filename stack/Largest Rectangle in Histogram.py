from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        previous_smaller_ele_l = [0] * n
        next_smaller_ele_l = [0] * n
        stack = []
        for i in range(n):
            while stack and heights[i] <= stack[-1][0]:
                stack.pop()
            if stack:
                previous_smaller_ele_l[i] = stack[-1][1]
            else:
                previous_smaller_ele_l[i] = -1
            stack.append(((heights[i], i)))

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= stack[-1][0]:
                stack.pop()
            if stack:
                next_smaller_ele_l[i] = stack[-1][1]
            else:
                next_smaller_ele_l[i] = -1
            stack.append(((heights[i], i)))

        # the objective is to see how much curernt column can expand both to the lef tand right
        res = 0
        for idx, num in enumerate(heights):
            prev_smaller_idx = previous_smaller_ele_l[idx]
            next_smaller_idx = next_smaller_ele_l[idx]
            dst = 1
            if next_smaller_idx != -1:
                dst += next_smaller_idx - idx - 1
            else:
                dst += n - idx - 1

            if prev_smaller_idx != -1:
                dst += idx - prev_smaller_idx - 1
            else:
                dst += idx

            res = max(res, dst * num)
        return res
