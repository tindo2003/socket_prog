from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int)
        res = 0

        # dire = 0 means right, dire = 1 means left
        def dfs(cur, cnt, dire):
            nonlocal res
            if not cur:
                return
            res = max(res, cnt)

            if dire == 0:  # Move to the right
                dfs(cur.right, cnt + 1, 1)
                dfs(cur.left, 1, 0)
            else:  # Move to the left
                dfs(cur.left, cnt + 1, 0)
                dfs(cur.right, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 0, 1)

        return res
