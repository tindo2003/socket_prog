from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(cur):
            my_str = ""
            if not cur.left and not cur.right:
                return str(cur.val)
            if cur.left and not cur.right:
                left = dfs(cur.left)
                my_str = f"{cur.val}({left})"
            elif cur.right and not cur.left:
                right = dfs(cur.right)
                my_str = f"{cur.val}()({right})"
            else:
                left = dfs(cur.left)
                right = dfs(cur.right)
                my_str = f"{cur.val}({left})({right})"
            return my_str

        return dfs(root)
