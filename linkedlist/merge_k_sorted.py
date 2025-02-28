# include "linkedlist.h"
# include <stdio.h>
import heapq
from typing import List, Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(self, lists):
    heap = []
    for ll in lists:
        temp = ll
        while temp:
            heapq.heappush(heap, temp.val)
            temp = temp.next

    dummy = ListNode()
    while heap:
        cur_val = heapq.heappop(heap)
        dummy.next = ListNode(cur_val)
        dummy = dummy.next
    return dummy.next


# merge sort version
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lsts(lst1, lst2):
            new_lst = ListNode()
            cur_node = new_lst
            while lst1 and lst2:

                if lst1.val < lst2.val:
                    cur_node.next = lst1
                    lst1 = lst1.next
                else:
                    cur_node.next = lst2
                    lst2 = lst2.next
                cur_node = cur_node.next
            if lst1:
                cur_node.next = lst1
            if lst2:
                cur_node.next = lst2
            return new_lst.next

        def recur(l, r):
            if l == r:
                return lists[l]
            m = (l + r) // 2
            left_half = recur(l, m)
            right_half = recur(m + 1, r)
            return merge_two_lsts(left_half, right_half)

        if not lists:
            return None
        l, r = 0, len(lists) - 1
        return recur(l, r)
