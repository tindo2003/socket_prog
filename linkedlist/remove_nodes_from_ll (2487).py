from typing import Optional
from math import inf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            new_head = prev
            return new_head

        new_head = reverse(head)

        max_so_far = -inf
        tmp = prev = new_head
        while tmp:
            if max_so_far > tmp.val:
                prev.next = tmp.next
            else:
                prev = tmp
            max_so_far = max(max_so_far, tmp.val)
            tmp = tmp.next

        return reverse(new_head)
