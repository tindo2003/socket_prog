from typing import Optional
from collections import defaultdict


# Definition for singly-linked list.
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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # DIVIDE AND CONQUER
        my_dict = defaultdict(ListNode)

        def occupyDict() -> int:
            cur = head
            idx = 0
            while cur:
                my_dict[idx] = cur
                cur = cur.next
                idx += 1
            return idx

        def dfs(l, r):
            if r < l:
                return None
            m = (l + r) // 2
            new_node = TreeNode(my_dict[m].val)
            new_node.left = dfs(l, m - 1)
            new_node.right = dfs(m + 1, r)
            return new_node

        n = occupyDict()

        return dfs(0, n - 1)
