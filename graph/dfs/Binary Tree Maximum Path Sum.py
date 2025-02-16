from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf

        def dfs(cur_node):
            nonlocal res
            if not cur_node:
                return 0
            left = dfs(cur_node.left)
            right = dfs(cur_node.right)
            take_left_only = cur_node.val + left
            take_right_only = cur_node.val + right
            take_both = cur_node.val + left + right
            take_neither = cur_node.val
            res = max(res, take_left_only, take_right_only, take_both, take_neither)
            return max(take_left_only, take_right_only, take_neither)

        dfs(root)
        return res
