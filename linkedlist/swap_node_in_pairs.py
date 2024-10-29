from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        prev = ListNode(next=head)
        cur = head
        while cur and cur.next:
            fast = cur.next
            cur.next = fast.next
            fast.next = cur
            prev.next = fast
            # get the new head so I know what to return.
            if cur == head:
                new_head = fast
            prev = cur
            cur = cur.next
        return new_head
