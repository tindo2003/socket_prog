from collections import defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_lst = defaultdict(list)

        def build_tree(cur_node):
            if not cur_node:
                return
            if cur_node.left:
                adj_lst[cur_node.val].append(cur_node.left.val)
                adj_lst[cur_node.left.val].append(cur_node.val)
            if cur_node.right:
                adj_lst[cur_node.val].append(cur_node.right.val)
                adj_lst[cur_node.right.val].append(cur_node.val)
            build_tree(cur_node.left)
            build_tree(cur_node.right)

        build_tree(root)

        dst = 0
        res = []
        q = [target.val]
        visited = set([target.val])
        while q:
            new_lst = []
            if dst == k:
                return q

            for node in q:
                for neighbor in adj_lst[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_lst.append(neighbor)

            dst += 1
            q = new_lst
        return res
