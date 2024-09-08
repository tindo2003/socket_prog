from typing import Optional, List 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0 
        cur = head 
        while cur is not None:
            length += 1
            cur = cur.next
        res = []
        mod = length % k
        each_bucket = length // k 
        cur = head
        prev = None
        for i in range(k):
            subhead = cur
            counter = 0
            while counter < each_bucket:
                prev = cur
                cur = cur.next
                counter += 1
            if mod > 0:
                prev = cur
                cur = cur.next
                mod -= 1
            res.append(subhead)
            if prev:
                prev.next = None
        return res