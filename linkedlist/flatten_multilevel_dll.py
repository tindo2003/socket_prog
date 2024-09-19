"""
# Definition for a Node.
"""
from typing import Optional
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        cur = head
        if not cur: return head
        while True: 
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child 
                cur.child.prev = cur 
                cur.child = None
            if cur.next is None:
                if not stack:
                    break 
                top = stack.pop()
                top.prev = cur 
                cur.next = top
            cur = cur.next 
        return head 
