# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        def find_tail(cur):
            length = 0
            while cur.next:
                cur = cur.next 
                length += 1
            return cur, length
        tail, length = find_tail(head)

        if length == 1: 
            return head
        cur = head
        while length > 0:
            even = cur.next
            cur.next = cur.next.next
            cur = cur.next
            even.next = None 
            tail.next = even 
            tail = tail.next
            length -= 2
        return head

