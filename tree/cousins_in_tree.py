class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from typing import Optional

class Solution:
  def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [root]
        while queue:
            found = False
            queue_size = len(queue)
            for _ in range(queue_size):
                cur_node = queue.pop(0)
                if cur_node.val == x or cur_node.val == y:
                    if found: 
                        return True 
                    else: 
                        found = True
                left = 0
                right = 0
                if cur_node.left:
                    queue.append(cur_node.left)
                    left = cur_node.left.val 
                if cur_node.right:
                    queue.append(cur_node.right)
                    right = cur_node.right.val
                if left != 0 and right != 0 and ((left == x and right == y) or (left == y and right == x)):
                    return False
        return False