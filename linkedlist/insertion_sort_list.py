from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = head
        cur = head.next
        while cur:
            nxt = cur.next
            ptr = dummy
            inserted = False
            while ptr.next:
                if ptr == cur:
                    break
                if cur.val < ptr.next.val:
                    prev.next = cur.next
                    cur.next = ptr.next
                    ptr.next = cur
                    inserted = True
                    break
                ptr = ptr.next
            if not inserted:
                prev = cur
            cur = nxt
        return dummy.next
