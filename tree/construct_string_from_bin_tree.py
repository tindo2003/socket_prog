from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(cur_node) -> str:
            if not cur_node.left and not cur_node.right:
                return str(cur_node.val)
            left = ""
            right = ""
            if cur_node.left:
                left = dfs(cur_node.left)
            if cur_node.right:
                right = dfs(cur_node.right)
            
            if right:
                return f"{cur_node.val}({left})({right})"
            else:
                return f"{cur_node.val}({left})"
        return dfs(root)