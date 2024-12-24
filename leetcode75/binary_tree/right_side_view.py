from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = [[root.val]]
        q = [root]
        while q:
            lst = []
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                    lst.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    lst.append(cur.right.val)
            if not lst:
                break
            levels.append(lst)
        tmp = [item[-1] for item in levels]
        return tmp
