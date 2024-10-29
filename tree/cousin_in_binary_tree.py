# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_sum = {}
        cur_lst = [root]
        depth_cnt = 0
        while True:
            new_lst = []
            for node in cur_lst:
                if node.left:
                    new_lst.append(node.left)
                if node.right:
                    new_lst.append(node.right)
            cur_lst = new_lst
            if not cur_lst:
                break
            s = sum([item.val for item in cur_lst])
            depth_cnt += 1
            depth_sum[depth_cnt] = s

        def dfs(cur, my_depth=1):
            if not cur:
                return
            lc = cur.left
            rc = cur.right
            old_l, old_r = 0, 0
            if lc:
                old_l = lc.val
            if rc:
                old_r = rc.val
            if lc:
                if rc:
                    lc.val = depth_sum[my_depth] - old_l - old_r
                else:
                    lc.val = depth_sum[my_depth] - old_l
            if rc:
                if lc:
                    rc.val = depth_sum[my_depth] - old_l - old_r
                else:
                    rc.val = depth_sum[my_depth] - old_r

            dfs(cur.left, my_depth + 1)
            dfs(cur.right, my_depth + 1)

        dfs(root)
        root.val = 0
        return root
