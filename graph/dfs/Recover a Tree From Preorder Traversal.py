from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        idx = 0
        offset = 1
        while idx + offset <= n and traversal[idx : idx + offset].isnumeric():
            offset += 1
        offset -= 1

        root = TreeNode(int(traversal[0 : 0 + offset]))
        idx += offset
        s = [(root, 0)]
        while idx < n:
            dash_cnt = 0
            while traversal[idx] == "-":
                idx += 1
                dash_cnt += 1

            offset = 1
            while idx + offset <= n and traversal[idx : idx + offset].isnumeric():
                offset += 1
            offset -= 1
            val = int(traversal[idx : idx + offset])
            idx += offset

            while s and dash_cnt - s[-1][1] != 1:
                s.pop()

            new_node = TreeNode(val)
            parent = s[-1][0]
            if not parent.left:
                parent.left = new_node
            else:
                parent.right = new_node
            s.append((new_node, dash_cnt))
        return s[0][0]
