from typing import Optional
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        # use a hashmap: idx -> ListNode helped me to perform MergeSort
        my_map = defaultdict(ListNode)

        def get_length(cur):
            global my_map
            l = 0
            while cur:
                my_map[l] = cur
                l += 1
                cur = cur.next
            return l

        def merge(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next

        def dfs(l, r):
            if l == r:
                # return node at l
                return my_map[l]
            middle = (l + r) // 2
            middle_node = my_map[middle]
            middle_node.next = None
            left_list = dfs(l, middle)
            right_list = dfs(middle + 1, r)
            # merge
            tmp = merge(left_list, right_list)
            return tmp

        cur = head
        N = get_length(cur)
        return dfs(0, N - 1)
