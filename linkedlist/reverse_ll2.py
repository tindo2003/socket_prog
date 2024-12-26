from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        left_out_range = None
        cur = head
        pos = 1
        while pos != left:
            left_out_range = cur
            cur = cur.next
            pos += 1

        prev = right_range = cur

        cur = cur.next
        while pos != right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            pos += 1

        if left_out_range:
            left_out_range.next = prev
        if right_range:
            right_range.next = cur
        if not left_out_range:
            return prev
        return head
