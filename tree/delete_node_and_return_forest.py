from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def dfs(cur):
            if not cur:
                return 
            left_tree = dfs(cur.left)
            right_tree = dfs(cur.right) 
            if cur.val in to_delete:
                # check in case we deleting leaf node
                if left_tree:
                    res.append(left_tree)
                if right_tree:
                    res.append(right_tree)
                return None 
            else:
                cur.left = left_tree
                cur.right = right_tree
                return cur
    
        tmp = dfs(root)
        # if root is not deleted
        if tmp:
            res.append(root)
        return res
        