from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        voyage_ptr = 0
        res = []
        good = True

        def dfs(cur_node):
            nonlocal voyage_ptr, good
            if not cur_node:
                return
            if voyage[voyage_ptr] != cur_node.val:
                good = False
                return
            voyage_ptr += 1
            left = cur_node.left
            right = cur_node.right

            if left:
                if voyage[voyage_ptr] != left.val:
                    res.append(cur_node.val)
                    dfs(right)
                    dfs(left)
                else:
                    dfs(left)
                    dfs(right)
            else:
                dfs(right)

        dfs(root)
        if not good:
            return [-1]
        return res
