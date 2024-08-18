from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def get_middle():
            slow, fast = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        tmp = get_middle()

        def reverse(begin):
            prev, nxt = None, None 
            cur = begin 
            while cur:
                nxt = cur.next
                cur.next = prev 
                prev = cur
                cur = nxt
            return prev

        head1 = reverse(tmp.next)
        tmp.next = None
        
        while head1 and head:
            if head1.val != head.val:
                return False 
            head1 = head1.next
            head = head.next
            
        return True