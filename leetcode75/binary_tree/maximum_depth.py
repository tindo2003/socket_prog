# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(cur):
            if not cur:
                return 0
            left = right = 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            return max(left + 1, right + 1)

        return dfs(root)
