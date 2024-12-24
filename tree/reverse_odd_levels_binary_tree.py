from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        even = False 
        while q:
            if not even:
                #reverse
                l, r = 0, len(q) - 1
                while l < r:
                    tmp = q[l]
                    q[l] = q[r]
                    q[r] = tmp 
                    l += 1
                    r -= 1
            even = not even 
            cur = q.pop(0)
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right) 
        return root

            

