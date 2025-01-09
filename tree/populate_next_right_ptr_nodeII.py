from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        layer = [root]
        while layer:
            new_layer = []
            for node in layer:
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)
            layer = new_layer
            for idx in range(len(layer) - 1):
                cur_node = layer[idx]
                right_node = layer[idx + 1]
                cur_node.next = right_node
        return root

    # second approach
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # think about tranversing the tree like a linked list
        if not root:
            return root
        left_most_node = root
        while left_most_node.left:
            cur = left_most_node
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            left_most_node = left_most_node.left
        return root
