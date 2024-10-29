from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0
        layer = deque([root])
        res = []
        while layer:
            level += 1
            val = [i.val for i in layer]
            if level % 2 == 1:
                res.append(val)
            else:
                res.append(val[::-1])
            for _ in range(len(layer)):
                cur_node = layer.popleft()
                l = cur_node.left
                r = cur_node.right
                if l:
                    layer.append(l)
                if r:
                    layer.append(r)
        return res
