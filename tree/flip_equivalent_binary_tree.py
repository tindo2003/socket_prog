from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        node_dict1 = defaultdict(list)
        node_dict2 = defaultdict(list)
        if (root1 and not root2) or (not root1 and root2):
            return False
        if not root1 and not root2:
            return True

        def dfs(cur_node, node_dict):
            if not cur_node:
                return
            if cur_node.left:
                node_dict[cur_node.val].append(cur_node.left.val)
            if cur_node.right:
                node_dict[cur_node.val].append(cur_node.right.val)
            dfs(cur_node.left, node_dict)
            dfs(cur_node.right, node_dict)

        dfs(root1, node_dict1)
        dfs(root2, node_dict2)

        for key, lst1 in node_dict1.items():
            lst2 = node_dict2[key]
            lst1.sort()
            lst2.sort()
            if lst1 != lst2:
                return False
        return True
