from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(cur) -> Optional[TreeNode]:
            if not cur.left and not cur.right:
                if cur.val == startValue or cur.val == destValue:
                    return cur 
                return None 
            left = None 
            if cur.left:
                left = lca(cur.left)
            right = None 
            if cur.right:
                right = lca(cur.right)
            # cur is lca
            if left and right:
                return cur 
            elif left:
                if left.val == startValue and cur.val == destValue:
                    return cur 
                if left.val == destValue and cur.val == startValue:    
                    return cur 
                return left 
            elif right:
                if right.val == startValue and cur.val == destValue:
                    return cur 
                if right.val == destValue and cur.val == startValue:
                    return cur 
                return right 
            else:
                if cur.val == startValue or cur.val == destValue:
                    return cur
                return None 
        my_lca = lca(root)
        
        
        parents = {my_lca.val : (None, None)}
        def dfs(cur):
            if not cur: return 
            if cur.left:
                parents[cur.left.val] = (cur.val, "L")
            dfs(cur.left)
            if cur.right:
                parents[cur.right.val] = (cur.val, "R")
            dfs(cur.right)
        dfs(my_lca)
        
        first_str, second_str = "", ""
        start = startValue
        end = destValue
        while True:
            parent, direction = parents[start]
            if not parent:
                break
            first_str += "U"
            start = parent
        while True:
            parent, direction = parents[end]
            if not parent:
                break
            second_str = direction + second_str
            end = parent
    
        return first_str + second_str