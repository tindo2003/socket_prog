from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        res = -1
        maxi = -inf
        cur_level = 1
        while q:
            s = 0
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                s += cur.val
            if s > maxi:
                maxi = s
                res = cur_level
            cur_level += 1
        return res
