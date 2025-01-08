from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # THINK ABOUT WHEN THE RECTANGLES WON'T OVERLAP
        lx1, ly1, rx1, ry1 = rec1
        lx2, ly2, rx2, ry2 = rec2

        if lx2 >= rx1 or lx1 >= rx2:
            return False
        if ly1 >= ry2 or ly2 >= ry1:
            return False
        return True
