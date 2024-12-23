from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        sum_so_far = 0
        res = 0

        def dfs(cur, sum_so_far, cnt):
            nonlocal res
            if not cur:
                return
            sum_so_far += cur.val
            if sum_so_far == targetSum:
                cnt[0] += 1
            dfs(cur.left, sum_so_far, cnt)
            dfs(cur.right, sum_so_far, cnt)

        q = [root]
        while q:
            cur = q.pop(0)
            cnt = [0]
            dfs(cur, 0, cnt)
            res += cnt[0]
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res
