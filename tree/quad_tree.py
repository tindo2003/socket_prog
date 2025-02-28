from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)
        top_row, bottom_row = 0, n - 1
        left_col, right_col = 0, n - 1

        def dfs(top_row, bottom_row, left_col, right_col):
            if top_row == bottom_row and left_col == right_col:
                cur_val = grid[top_row][left_col]
                return Node(cur_val, True, None, None, None, None)

            middle_row = (top_row + bottom_row) // 2
            middle_col = (left_col + right_col) // 2
            top_left = dfs(top_row, middle_row, left_col, middle_col)
            top_right = dfs(top_row, middle_row, middle_col + 1, right_col)
            bottom_left = dfs(middle_row + 1, bottom_row, left_col, middle_col)
            bottom_right = dfs(middle_row + 1, bottom_row, middle_col + 1, right_col)

            if (
                top_left.val == top_right.val == bottom_left.val == bottom_right.val
                and top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
            ):
                if top_left.val == 1:
                    return Node(1, True, None, None, None, None)
                else:
                    return Node(0, True, None, None, None, None)
            else:
                return Node(1, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(top_row, bottom_row, left_col, right_col)
