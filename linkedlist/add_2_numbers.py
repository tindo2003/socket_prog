from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def get_length(head):
            length = 0
            cur = head
            while cur:
                length += 1
                cur = cur.next
            return length

        n1 = get_length(l1)
        n2 = get_length(l2)
        if n1 > n2:
            list_to_iter = l1
            secondary = l2

        else:
            list_to_iter = l2
            secondary = l1

        ptr2 = secondary
        ptr1 = list_to_iter
        prev1 = None
        remember = 0
        while ptr1 and ptr2:
            tmp = ptr1.val + ptr2.val + remember
            ptr1.val = tmp % 10
            remember = tmp // 10
            prev1 = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            tmp = ptr1.val + remember
            ptr1.val = tmp % 10
            remember = tmp // 10
            prev1 = ptr1
            ptr1 = ptr1.next

        if remember > 0:
            prev1.next = ListNode(remember)
        return list_to_iter
