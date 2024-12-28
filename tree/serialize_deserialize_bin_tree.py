from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(cur):
            if not cur:
                res.append(str("None"))
                return
            res.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)

        dfs(root)
        return " ".join(res)

    def deserialize(self, data) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = [int(item) if item != "None" else None for item in data.split(" ")]
        # keep a global cnt to index into the data array
        idx = 0

        def dfs():
            nonlocal idx
            if data[idx] is None:
                return None
            if idx >= len(data):
                return None
            new_node = TreeNode(data[idx])
            idx += 1
            new_node.left = dfs()
            idx += 1
            new_node.right = dfs()
            return new_node

        res = dfs()
        return res


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# ans = deser.deserialize(ser.serialize(root))
