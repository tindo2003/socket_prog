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
