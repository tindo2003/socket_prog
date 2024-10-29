# Definition for a binary tree node.
from typing import Optional 
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # min heap
        if not root:
            return -1
        h = [root.val]
        my_lst = [root]
        while True:
            new_lst = []
            for node in my_lst:
                if node.left:
                    new_lst.append(node.left)
                if node.right:
                    new_lst.append(node.right)
            my_lst = new_lst
            if len(my_lst) == 0:
                break
            my_sum = sum([item.val for item in my_lst])
            heapq.heappush(h, my_sum)
            if len(h) > k:
                heapq.heappop(h)
        if len(h) < k:
            return -1
        return h[0]
