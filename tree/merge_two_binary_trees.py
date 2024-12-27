from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 or node2:
                new_node = TreeNode()
                if node1:
                    new_node.val += node1.val
                if node2:
                    new_node.val += node2.val
                node1_left = node1.left if node1 else None
                node1_right = node1.right if node1 else None
                node2_left = node2.left if node2 else None
                node2_right = node2.right if node2 else None
                new_node.left = dfs(node1_left, node2_left)
                new_node.right = dfs(node1_right, node2_right)
                return new_node
            else:
                return None

        return dfs(root1, root2)
