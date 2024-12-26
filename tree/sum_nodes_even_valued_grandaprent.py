from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def dfs(cur, parent):
            nonlocal cnt
            if not cur:
                return
            if cur.left and parent and parent.val % 2 == 0:
                cnt += cur.left.val
            if cur.right and parent and parent.val % 2 == 0:
                cnt += cur.right.val
            dfs(cur.left, cur)
            dfs(cur.right, cur)

        dfs(root, None)
        return cnt
