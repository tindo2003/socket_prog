from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0 
        def dfs(cur): 
            if not cur:
                return
            dfs(cur.right)
            self.sum += cur.val
            cur.val = self.sum 
            dfs(cur.left)
        dfs(root)
        return root

            
        
