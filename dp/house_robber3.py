from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def helper(cur, picked_prev: bool) -> int:
            if not cur:
                return 0
            if (cur, picked_prev) in cache:
                return cache[(cur, picked_prev)]
            #pick
            picked = 0
            if not picked_prev:
                picked = cur.val + helper(cur.left, True) + helper(cur.right, True)
            #not picked 
            unpicked = helper(cur.left, False) + helper(cur.right, False) 

            cache[(cur, picked_prev)] = max(picked, unpicked) 
            return cache[(cur, picked_prev)]
        
        return helper(root, False)
