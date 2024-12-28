from math import inf
from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        my_dict = defaultdict(int)

        def dfs(cur):
            if not cur:
                return 0
            cur_sum = cur.val + dfs(cur.left) + dfs(cur.right)
            my_dict[cur_sum] += 1
            return cur_sum

        dfs(root)
        maxi = -inf
        res = []
        for k, v in my_dict.items():
            if v > maxi:
                maxi = v
        for k, v in my_dict.items():
            if v == maxi:
                res.append(k)
        return res
