from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_depth = 0 
        ancestor = None

        def dfs(cur, depth) -> bool:
            nonlocal cur_depth
            nonlocal ancestor
            if not cur.left and not cur.right:
                if depth >= cur_depth:
                    ancestor = cur
                    cur_depth = depth
                return depth
            left, right = 0, 0
            if cur.left:
                left = dfs(cur.left, depth + 1)
            if cur.right:
                right = dfs(cur.right, depth + 1)
            if left == cur_depth and right == cur_depth:
                ancestor = cur
            return max(left, right)

        dfs(root, 0)
        return ancestor