# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        max_so_far = float("-inf")

        def dfs(cur, max_so_far):
            if not cur:
                return
            if cur.val >= max_so_far:
                res[0] += 1
                max_so_far = cur.val
            dfs(cur.left, max_so_far)
            dfs(cur.right, max_so_far)

        dfs(root, max_so_far)
        return res[0]
