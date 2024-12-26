from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left_level = 0
        right_level = 0
        cur_left = root
        cur_right = root
        while cur_left:
            cur_left = cur_left.left
            left_level += 1
        while cur_right:
            cur_right = cur_right.right
            right_level += 1

        if right_level == left_level:
            return 2**right_level - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
