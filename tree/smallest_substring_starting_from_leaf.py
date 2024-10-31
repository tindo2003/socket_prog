from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        l = deque([])
        res = []
        def dfs(cur_node):
            if cur_node.left is None and cur_node.right is None:
                l.appendleft(chr(ord('a') + cur_node.val))
                cpy = list(l).copy()
                res.append("".join(cpy))
                l.popleft()
                return
            l.appendleft(chr(ord('a') + cur_node.val))
            if cur_node.left:
                dfs(cur_node.left)
            if cur_node.right:
                dfs(cur_node.right)
            l.popleft()
        dfs(root)
        res.sort()
        return res[0]

        

