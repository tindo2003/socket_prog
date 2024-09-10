from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_gcd(a, b):
            c = a % b 
            if c == 0:
                return b 
            return find_gcd(b, c) 
    
        cur = head
        while cur.next is not None:
            current_val = cur.val 
            next_node = cur.next
            next_val = next_node.val
            new_val = find_gcd(current_val, next_val)
            new_node = ListNode(new_val)
            cur.next = new_node
            new_node.next = next_node
            cur = next_node
        return head
