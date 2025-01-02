from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        res = []

        def dfs(cur) -> Optional[TreeNode]:
            if not cur:
                return
            if cur.val in to_delete:
                left = dfs(cur.left)
                right = dfs(cur.right)
                if left:
                    res.append(left)
                if right:
                    res.append(right)
                return None
            else:
                left = dfs(cur.left)
                right = dfs(cur.right)
                cur.left = left
                cur.right = right
                return cur

        tmp = dfs(root)
        if tmp:
            res.append(tmp)
        return res
