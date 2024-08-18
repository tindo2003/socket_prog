from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(cur) -> int:
            if not cur: return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            val = cur.val 
            self.ans += (abs(left) + abs(right))
            return val - 1 + left + right 

        dfs(root)
        return self.ans
