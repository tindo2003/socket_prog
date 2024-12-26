from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_sum = 0

        def dfs(cur):
            nonlocal cur_sum
            if not cur:
                return

            dfs(cur.right)

            tmp = cur.val
            cur.val += cur_sum
            cur_sum += tmp

            dfs(cur.left)

        dfs(root)
        return root
