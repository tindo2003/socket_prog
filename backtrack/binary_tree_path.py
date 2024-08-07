from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
       
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []
    def helper(cur, path):
      if not cur:
          return
      path += str(cur.val)
      if not cur.left and not cur.right:
        res.append(path)
        return  
      path += "->"
      helper(cur.left, path)
      helper(cur.right, path)
      
    helper(root, "")
    return res
