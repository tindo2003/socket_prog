from collections import defaultdict
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_map = defaultdict(int)
        def hash_maker(cur, lst):
            if not cur:
                lst.append("N,")
                return 
            lst.append(f"{str(cur.val)},")
            hash_maker(cur.left, lst)
            hash_maker(cur.right, lst)
        q = [root]
        res = []
        
        while q:
            cur_node = q.pop(0)
            hsh = []
            hash_maker(cur_node, hsh)
            hash_str = "".join(hsh)
            
            hash_map[hash_str] += 1
            if hash_map[hash_str] == 2:
                res.append(cur_node)
            left_child = cur_node.left
            right_child = cur_node.right
            if left_child: q.append(left_child)
            if right_child: q.append(right_child)
        
        return res

        

        

        

        