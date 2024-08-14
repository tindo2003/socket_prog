from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        arr = []
        cur_sum = 0
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next 
        my_dict = {0 : -1}
        n = len(arr)
        res = [1] * n
        sums = [0] * n
        for idx, num in enumerate(arr):
            cur_sum += num 
            sums[idx] = cur_sum
            if cur_sum not in my_dict:
                my_dict[cur_sum] = idx
            else:
                prev_idx = my_dict[cur_sum]
                for idx in range(prev_idx + 1, idx):
                    if res[idx]:
                        del my_dict[idx]
                for idx in range(prev_idx + 1, idx + 1):
                    res[idx] = 0
        dummy = ListNode()
        tmp = dummy
        for idx, val in enumerate(res):
            if val == 1: 
                tmp.next = ListNode(arr[idx])
                tmp = tmp.next
        return dummy.next

        #  1 2 3 -3 2 -> 1 3 6 3 1