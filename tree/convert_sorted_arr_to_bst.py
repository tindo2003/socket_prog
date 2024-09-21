from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            ''' return tree node '''
            if l > r: return None
            if l == r: return TreeNode(nums[l])
            mid = (l + r) // 2
            left_node = dfs(l, mid - 1)
            right_node = dfs(mid + 1, r)
            return TreeNode(nums[mid], left_node, right_node)
        return dfs(0, len(nums) - 1)

