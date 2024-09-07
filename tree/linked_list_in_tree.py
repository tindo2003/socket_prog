# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def string_matching(ll_ptr, tree_ptr) -> bool:
            if ll_ptr is None:
                return True
            if tree_ptr is None:
                return False
            if ll_ptr.val != tree_ptr.val:
               return False 
            left = string_matching(ll_ptr.next, tree_ptr.left)
            right = string_matching(ll_ptr.next, tree_ptr.right)
            return left or right 

        def dfs(cur) -> bool:
            if not cur:
                return False
            tmp_head = head
            tmp_root = cur
            if string_matching(tmp_head, tmp_root):
                return True 
            if dfs(cur.left) or dfs(cur.right):
                return True 
            else:
                return False
            
        return dfs(root)