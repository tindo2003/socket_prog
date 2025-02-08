# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        potential_res = None
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if i == 0:
                    potential_res = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return potential_res.val
