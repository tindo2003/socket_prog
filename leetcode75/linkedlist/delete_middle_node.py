# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        length = 0

        cur = head
        while cur:
            length += 1
            cur = cur.next

        if length == 1:
            return None
        if length == 2:
            head.next = None
            return head

        pred = head
        times_to_iter = length // 2 - 1
        for _ in range(times_to_iter):
            pred = pred.next

        pred.next = pred.next.next
        return head
