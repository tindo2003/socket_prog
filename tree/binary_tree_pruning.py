from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(cur):
            if not cur.left and not cur.right:
                return cur.val == 0
            
            l = True
            if cur.left:
                l = helper(cur.left)
            r = True
            if cur.right:
                r = helper(cur.right)
            
            if l:
                cur.left = None 
            if r:
                cur.right = None
            if l and r and cur.val == 0:
                return True 
            return False
        
        helper(root)
        if not root.left and not root.right and root.val == 0:
            return None
        return root