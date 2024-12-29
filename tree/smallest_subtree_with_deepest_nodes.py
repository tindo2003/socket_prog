from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs():
            current_level = [root]
            while 1:
                new_level = []
                for node in current_level:
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                if not new_level:
                    break
                current_level = new_level
            return current_level

        deepest_nodes = bfs()
        deepest_nodes = set(deepest_nodes)
        res = None

        def dfs(cur):
            nonlocal res
            """ check which EARLIEST node containing all the deepest nodes. post order"""
            if not cur:
                return 0
            total = 0
            if cur in deepest_nodes:
                total += 1
            left_cnt = dfs(cur.right)
            right_cnt = dfs(cur.left)
            total += left_cnt
            total += right_cnt
            if total == len(deepest_nodes):
                # IMPORTANT
                if res is None:
                    res = cur
            return total

        dfs(root)
        return res
