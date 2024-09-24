# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def get_middle():
            slow, fast = head, head 
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next 
            return slow
        
        def reverse(cur):
            prev, next = None, None 
            while cur is not None:
                next = cur.next 
                cur.next = prev 
                prev = cur 
                cur = next 
            return prev

        middle = get_middle()
        # reverse the later half
        head1 = reverse(middle.next)        
        cur1, cur = head, head1 
        ans = 0
        while cur1 and cur:
            cur_sum = cur1.val + cur.val 
            ans = max(ans, cur_sum)
            cur1 = cur1.next
            cur = cur.next
        return ans
