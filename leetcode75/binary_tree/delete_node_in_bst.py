from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return
            left = cur.left
            right = cur.right

            if cur.val == key:

                # no child
                if not cur.left and not cur.right:
                    return None
                # one child
                if cur.left and not cur.right:
                    return cur.left
                if cur.right and not cur.left:
                    return cur.right
                # two children
                to_replace = cur.right
                while to_replace.left:
                    to_replace = to_replace.left
                new_tree = self.deleteNode(cur.right, to_replace.val)
                to_replace.right = new_tree
                to_replace.left = cur.left
                return to_replace
            elif cur.val < key:
                right = dfs(cur.right)
            else:
                left = dfs(cur.left)
            cur.left = left
            cur.right = right
            return cur

        return dfs(root)
