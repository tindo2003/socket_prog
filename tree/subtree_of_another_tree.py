from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1, node2) -> bool:
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2):
                return False
            first_check = node1.val == node2.val
            second_check = dfs(node1.left, node2.left)
            third_check = dfs(node1.right, node2.right)
            return first_check and second_check and third_check

        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                if dfs(cur, subRoot):
                    return True
                stack.append(cur.left)
                stack.append(cur.right)
        return False
