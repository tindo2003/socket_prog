from typing import (
    List,
)
from collections import defaultdict
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        # right grandchild of the left child and 
        # left grandchild of the right child
        if not root:
            return []
        min_col = float("inf")
        max_col = float("-inf")
        my_dict = defaultdict(dict)
        def bfs():
            nonlocal min_col, max_col
            queue = [(root, 0, 0)]
            while queue:
                for _ in range(len(queue)):
                    cur, row, col = queue.pop(0)
                    min_col = min(min_col, col)
                    max_col = max(max_col, col)
                    if col not in my_dict[row]:
                        my_dict[row][col] = [cur.val]
                    else:
                        my_dict[row][col].append(cur.val)
                    new_row = row + 1
                    if cur.left:
                        queue.append((cur.left, new_row, col - 1))
                    if cur.right:
                        queue.append((cur.right, new_row, col + 1))
        bfs()
        
        sorted_dict = dict(sorted(my_dict.items()))
        
        res_length = max_col - min_col + 1
        
        res = [[] for _ in range(res_length)]
        for row, col_lst in sorted_dict.items():
            for col, lst in col_lst.items():
                res[col+abs(min_col)].extend(lst)
        return res