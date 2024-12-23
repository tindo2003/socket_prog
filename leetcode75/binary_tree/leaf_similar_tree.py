# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        lst1 = []
        lst2 = []
        self.dfs(root1, lst1)
        self.dfs(root2, lst2)
        return lst1 == lst2

    def dfs(self, cur, node_lst):
        # is a leaf
        if not cur.left and not cur.right:
            node_lst.append(cur.val)
        if cur.left:
            self.dfs(cur.left, node_lst)
        if cur.right:
            self.dfs(cur.right, node_lst)
