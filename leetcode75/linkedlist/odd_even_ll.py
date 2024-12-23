# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        if not head.next:
            return head
        even = head
        odd_head = head.next
        odd = head.next
        # THE TRICK HERE IS TO REARRANGING ODD AND EVEN FIRST
        while even.next and odd.next:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        even.next = odd_head
        return head
