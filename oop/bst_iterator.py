from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def get_lst(self, cur, lst):
        if not cur:
            return
        self.get_lst(cur.left, lst)
        lst.append(cur.val)
        self.get_lst(cur.right, lst)

    def __init__(self, root: Optional[TreeNode]):
        lst = []
        self.get_lst(root, lst)
        self.lst = lst
        self.idx = 0

    def next(self) -> int:
        val = self.lst[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.lst)
