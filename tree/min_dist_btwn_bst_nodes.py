from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []
        res = inf
        def dfs(cur):
            if not cur: return 
            dfs(cur.left)
            nodes.append(cur.val)
            dfs(cur.right)
        dfs(root)
        for i in range(1, len(nodes)):
            res = min(res, nodes[i] - nodes[i-1])
        return res
