from typing import Optional
from collections import deque

"""
# Definition for a Node.
"""


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root
        q = deque([root])
        while q:
            new_level = deque([])
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    new_level.append(cur.left)
                if cur.right:
                    new_level.append(cur.right)
            if not new_level:
                break
            for idx, node in enumerate(new_level):
                new_level[idx - 1].next = node
            new_level[len(new_level) - 1].next = None
            q = new_level
        return root
