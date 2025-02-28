from typing import (
    List,
)


"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """

    def boundary_of_binary_tree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # write your code here
        left = []
        right = []
        leaves = []

        
        def get_left(cur_node):
            while cur_node and (cur_node.left or cur_node.right):
                left.append(cur_node.val)
                if cur_node == root:
                    cur_node = cur_node.left
                else:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node = cur_node.right

        def get_right(cur_node):
            while cur_node and (cur_node.left or cur_node.right):
                right.append(cur_node.val)
                if cur_node == root:
                    cur_node = cur_node.right
                else:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left

        def dfs(cur_node):
            if not cur_node.left and not cur_node.right:
                leaves.append(cur_node.val)
                return
            if cur_node.left:
                dfs(cur_node.left)
            if cur_node.right:
                dfs(cur_node.right)

        get_left(root)
        get_right(root)
        dfs(root)
        return left + leaves + right[::-1][:-1]
