# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # idea: reverse later half of the linkedlist

        # 1: find length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 2: get the middle node
        middle = head
        for _ in range(length // 2):
            middle = middle.next

        # 3: reverse later half
        prev = None
        cur = middle
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # (0, 5), (1, 4), (2, 3). compare the nodes in first half to nodes in second half
        res = float("-inf")
        ptr1 = head
        ptr2 = prev
        for _ in range(length // 2):
            s = ptr1.val + ptr2.val
            res = max(s, res)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return res
