from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        res = 0
        while q:
            mini, maxi = inf, -inf
            for _ in range(len(q)):
                cur, val = q.pop(0)
                if cur.left:
                    q.append((cur.left, 2 * val))
                if cur.right:
                    q.append((cur.right, 2 * val + 1))
                mini = min(mini, val)
                maxi = max(maxi, val)
                res = max(res, maxi - mini + 1)
        return res
