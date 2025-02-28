from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(cur_node):
            if not cur_node.left and not cur_node.right:
                if val > cur_node.val:
                    cur_node.right = TreeNode(val)
                else:
                    cur_node.left = TreeNode(val)
                return cur_node
            left = cur_node.left
            right = cur_node.right
            if val <= cur_node.val:
                if cur_node.left:
                    left = dfs(cur_node.left)
                else:
                    cur_node.left = TreeNode(val)
                    return TreeNode(cur_node.val, cur_node.left, right)
            else:
                if cur_node.right:
                    right = dfs(cur_node.right)
                else:
                    cur_node.right = TreeNode(val)
                    return TreeNode(cur_node.val, left, cur_node.right)
            return TreeNode(cur_node.val, left, right)

        return dfs(root)
