from typing import List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst1, lst2 = [], []
        def dfs(cur, lst):
            if not cur:
                return 
            dfs(cur.left, lst)
            lst.append(cur.val)
            dfs(cur.right, lst)
        dfs(root1, lst1)
        dfs(root2, lst2)
        
        idx1, idx2 = 0, 0 
        res = []
        while idx1 < len(lst1) and idx2 < len(lst2):
            if lst1[idx1] <= lst2[idx2]:
                res.append(lst1[idx1])
                idx1 += 1
            else:
                res.append(lst2[idx2])
                idx2 += 1
        if idx1 < len(lst1):
            res += lst1[idx1:]
        if idx2 < len(lst2):
            res += lst2[idx2:] 

        return res 
