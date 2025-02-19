from typing import Optional
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # min heap of size k
        q = [root]
        h = []
        while q:
            new_lst = []
            cur_sum = 0
            for cur in q:
                cur_sum += cur.val
                if cur.left:
                    new_lst.append(cur.left)
                if cur.right:
                    new_lst.append(cur.right)
            heapq.heappush(h, cur_sum)
            if len(h) > k:
                heapq.heappop(h)
            if not new_lst:
                break
            q = new_lst
        if len(h) < k:
            return -1
        return h[0]
