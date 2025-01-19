from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        tmp = 0

        def dfs(cur):
            # THE OBJECTIVE OF THIS FUNCTION IS TO FIND HEIGHT. BUT WE GETTING DIAMETER AS A SIDE JOB
            nonlocal tmp
            if not cur:
                return -1
            left = right = -1
            if cur.left and cur.left.val == cur.val:
                left = dfs(cur.left)
            if cur.right and cur.right.val == cur.val:
                right = dfs(cur.right)
            tmp = max(tmp, 2 + left + right)
            return 1 + max(left, right)

        def another_dfs(cur):
            if not cur:
                return
            nonlocal res, tmp
            tmp = 0
            # FIND "DIAMETER" AT EACH STEP
            dfs(cur)
            res = max(res, tmp)
            another_dfs(cur.left)
            another_dfs(cur.right)

        another_dfs(root)
        return res
