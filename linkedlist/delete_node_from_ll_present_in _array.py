# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next is not None:
            if cur.next.val in nums_set:
                cur.next = cur.next.next
                continue
            cur = cur.next 

        return dummy.next