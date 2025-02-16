from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.my_set = set()

        def change_the_tree(cur_node, parent_val):
            if not cur_node:
                return
            cur_node.val = parent_val + 1
            self.my_set.add(cur_node.val)
            change_the_tree(cur_node.left, 2 * cur_node.val)
            change_the_tree(cur_node.right, 2 * cur_node.val + 1)

        change_the_tree(root, -1)

    def find(self, target: int) -> bool:
        return target in self.my_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
