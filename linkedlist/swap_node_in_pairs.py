from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # KEEP A PREV PTR
        dummy = ListNode(next=head)
        prev = dummy
        cur = head
        while cur and cur.next:
            neighbor = cur.next
            cur.next = neighbor.next
            neighbor.next = cur
            # ~~~~~~~~~
            prev.next = neighbor
            prev = cur
            cur = cur.next
        return dummy.next
